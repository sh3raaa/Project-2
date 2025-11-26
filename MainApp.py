import tkinter as tk
from tkinter import ttk, messagebox, END, filedialog
from entryForm import EntryForm
from caloriesDatabase import CalorieDatabase
from statsWindow import StatsWindow
import json
from tkinter import font


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Tracker - OurCal")
        self.root.geometry("900x600")
        self.root.resizable(True, True)

        #colors
        self.darkColor = "#34495E"
        self.lightColor = "#E9F6FB"
        self.buttonColor = "#2E86C1"
        self.buttonActiveColor = "#1B4F72"

        #fonts (named fonts)
        self.titleFont = font.Font(family="Arial", size=18, weight="bold")
        self.labelFont = font.Font(family="Arial", size=12, weight="bold")
        self.buttonFont = font.Font(family="Arial", size=10, weight="bold")
        self.entryFont = font.Font(family="Arial", size=11)

        #ttk style for Combobox
        style = ttk.Style()
        style.configure("My.TCombobox", font=self.entryFont)

        #the database connection
        self.database = CalorieDatabase()
        self.entriesList = self.database.loadData()
        self.totalCalories = 0
        self.calculateTotalCalories()

        #frames
        self.titleFrame = tk.Frame(root, bg=self.darkColor)
        self.titleFrame.pack(fill="x")

        self.mainFrame = tk.Frame(root, bg=self.lightColor)
        self.mainFrame.pack(fill="both", expand=True)

        self.bottomFrame = tk.Frame(root, bg=self.darkColor)
        self.bottomFrame.pack(fill="x", side="bottom")

        #main grid spacing
        for r in range(5):
            self.mainFrame.rowconfigure(r, weight=1)
        for c in range(7):
            self.mainFrame.columnconfigure(c, weight=1)

        self.createTitle()
        self.entryForm = EntryForm(self.mainFrame, bg=self.lightColor)
        self.createButtons()
        self.createListbox()
        self.createTotalCaloriesLabel()
        self.populateListbox()

        #create menu
        self.root.config(menu=self.createMenu())

    #title of aapp
    def createTitle(self):
        titleLabel = tk.Label(
            self.titleFrame,
            text="Welcome to OurCal - Calorie Tracker",
            bg=self.darkColor,
            fg="white",
            font=self.titleFont,  # replaced font
            pady=8
        )
        titleLabel.pack()

    #function of the buttons
    def createButtons(self):
        #add button
        addButton = tk.Button(
            self.mainFrame, text="Add Entry", command=self.addEntry,
            bg=self.buttonColor, fg="white", font=self.buttonFont,  # replaced font
            activebackground=self.buttonActiveColor
        )
        addButton.grid(row=2, column=1, padx=10, pady=8, sticky="nsew")

        #update button
        updateButton = tk.Button(
            self.mainFrame, text="Update Entry", command=self.updateEntry,
            bg=self.buttonColor, fg="white", font=self.buttonFont,  # replaced font
            activebackground=self.buttonActiveColor
        )
        updateButton.grid(row=2, column=3, padx=10, pady=8, sticky="nsew")

        #delete button
        deleteButton = tk.Button(
            self.mainFrame, text="Delete Entry", command=self.deleteEntry,
            bg=self.buttonColor, fg="white", font=self.buttonFont,  # replaced font
            activebackground=self.buttonActiveColor
        )
        deleteButton.grid(row=2, column=5, padx=10, pady=8, sticky="nsew")

        #the clear and quit buttons
        clearButton = tk.Button(
            self.bottomFrame, text="Clear All", command=self.clearAll,
            bg="#E74C3C", fg="white", font=self.buttonFont,  # replaced font
            activebackground="#C0392B"
        )
        clearButton.pack(side="right", padx=10, pady=10)

        quitButton = tk.Button(
            self.bottomFrame, text="Quit", command=self.confirmQuit,
            bg="#95A5A6", fg="white", font=self.buttonFont,  # replaced font
            activebackground="#7F8C8D"
        )
        quitButton.pack(side="right", padx=10, pady=10)

    #listbox that has the entries
    def createListbox(self):
        self.listbox = tk.Listbox(self.mainFrame, font=self.entryFont, exportselection=False)  # replaced font
        self.listbox.grid(row=3, column=1, columnspan=5,
                        sticky="nsew", padx=20, pady=12)
        self.listbox.bind("<<ListboxSelect>>", self.onSelect)
        scrollbar = tk.Scrollbar(self.mainFrame, orient="vertical",
                                command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=3, column=6, sticky="ns", pady=12)

    def populateListbox(self):
        self.listbox.delete(0, END)
        for entry in self.entriesList:
            item = f"{entry['food']} - Cal: {entry['calories']} - Meal: {entry['meal']}"
            self.listbox.insert(END, item)

    #the total calo label
    def createTotalCaloriesLabel(self):
        self.totalLabel = tk.Label(
            self.bottomFrame,
            text=f"Total Calories: {self.totalCalories}",
            fg="white", bg=self.darkColor,
            font=self.labelFont  # replaced font
        )
        self.totalLabel.pack(pady=10)

    def updateTotalLabel(self):
        self.totalLabel.config(text=f"Total Calories: {self.totalCalories}")

    def calculateTotalCalories(self):
        total = 0
        for e in self.entriesList:
            try:
                total += int(e.get("calories", 0))
            except:
                pass
        self.totalCalories = total

    def addEntry(self):
        food = self.entryForm.foodEntry.get().strip()
        cal = self.entryForm.calEntry.get().strip()
        meal = self.entryForm.mealCombo.get().strip()

        if not food or not cal or not meal:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            cal_int = int(cal)
        except ValueError:
            messagebox.showerror("Error", "Calories must be a number.")
            return

        self.entriesList.append({
            "food": food,
            "calories": str(cal_int),
            "meal": meal
        })

        self.database.saveData(self.entriesList)
        self.calculateTotalCalories()
        self.updateTotalLabel()
        self.populateListbox()
        self.entryForm.clearFields()

    #this function handles listbox selection and fills the input fields with the selected entry's data
    def onSelect(self, event):
        try:
            index = self.listbox.curselection()[0]
            entry = self.entriesList[index]

            self.entryForm.foodEntry.delete(0, END)
            self.entryForm.foodEntry.insert(0, entry["food"])

            self.entryForm.calEntry.delete(0, END)
            self.entryForm.calEntry.insert(0, entry["calories"])

            # DO NOT auto-select/highlight combobox text
            self.entryForm.mealCombo.set(entry["meal"])
            self.entryForm.mealCombo.event_generate('<FocusOut>')
            self.entryForm.mealCombo.selection_clear()

        except:
            pass

    #a function that updates the currently selected listbox entry using the form inputs
    def updateEntry(self):
        try:
            index = self.listbox.curselection()[0]
        except:
            messagebox.showerror("Error", "Pick an entry to update.")
            return

        food = self.entryForm.foodEntry.get().strip()
        cal = self.entryForm.calEntry.get().strip()
        meal = self.entryForm.mealCombo.get().strip()

        if not food or not cal or not meal:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            cal_int = int(cal)
        except:
            messagebox.showerror("Error", "Calories must be a number.")
            return

        #update data list
        self.entriesList[index] = {
            "food": food,
            "calories": str(cal_int),
            "meal": meal
        }

        #save & refresh
        self.database.saveData(self.entriesList)
        self.calculateTotalCalories()
        self.updateTotalLabel()
        self.populateListbox()

        self.listbox.select_set(index)
        self.listbox.activate(index)
        self.entryForm.clearFields()

    #a function to delete a selectred entry and it shows a pop window (message box) up asking if u actually want to delete
    def deleteEntry(self):
        try:
            index = self.listbox.curselection()[0]
        except:
            messagebox.showerror("Error", "Pick an entry to delete.")
            return

        if messagebox.askyesno("Confirm", "Delete this entry?"):
            del self.entriesList[index]
            self.database.saveData(self.entriesList)
            self.calculateTotalCalories()
            self.updateTotalLabel()
            self.populateListbox()
            self.entryForm.clearFields()

    #a func for the clear all button, it clears all entries added  and also shows a message box to confirm
    def clearAll(self):
        if messagebox.askyesno("Confirm", "Clear ALL entries?"):
            self.entriesList = []
            self.database.saveData(self.entriesList)
            self.calculateTotalCalories()
            self.updateTotalLabel()
            self.populateListbox()
            self.entryForm.clearFields()

    #a function to quit the whole calo app
    def confirmQuit(self):
        if messagebox.askyesno("Quit", "Exit the program?"):
            self.root.quit()

    #a function to save the entries as a JSON file
    def saveAs(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json")]
        )

        if not filename:
            return

        try:
            with open(filename, "w") as f:
                json.dump(self.entriesList, f, indent=2)

            messagebox.showinfo("Saved", "File saved successfully")
        except:
            messagebox.showerror("Error", "Could not save file")

    #opens the statistics window with the current entries
    def openStats(self):
        StatsWindow(self.root, self.entriesList)

    #a function for the menu bar at the top
    def createMenu(self):
        menuBar = tk.Menu(self.root)
        menu = tk.Menu(menuBar, tearoff=0)

        menu.add_command(label="View Stats", command=self.openStats)
        menu.add_command(label="Save As...", command=self.saveAs)

        menuBar.add_cascade(label="Options", menu=menu)
        return menuBar

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
