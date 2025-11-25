import tkinter as tk
from tkinter import ttk, END

#VARIABLES
totalCalories = 0
foodEntry = None
caloEntry = None
mealCombo = None
listBoxWidget = None

#ROOT
root = tk.Tk()
root.title("Calorie App")
root.geometry("700x500")

# ----- COLOR PALETTE -----
DARK = "#2C3E50"        # Header/footer
LIGHT = "#ECF0F1"       # Main area
BUTTON = "#3498DB"      # Button background
BUTTON_ACTIVE = "#2980B9"  # Button when clicked

#FRAMES
titleFrame = tk.Frame(root, bg=DARK)
titleFrame.pack(fill="x")

mainFrame = tk.Frame(root, bg=LIGHT)
mainFrame.pack(fill="both", expand=True)

bottomFrame = tk.Frame(root, bg=DARK)
bottomFrame.pack(fill="x", side="bottom")


# GRID SETUP
for r in range(3):
   mainFrame.rowconfigure(r, weight=1, uniform="row")

for c in range(5):
   mainFrame.columnconfigure(c, weight=1, uniform="column")


# TITLE
def title():
   title = tk.Label(
       titleFrame,
       text="Welcome to ourCal",
       background=DARK,
       fg="white",
       font=("Arial", 16, "bold")
   )
   title.pack(pady=8)


# TOTAL CALORIES
def totalCal():
   totalCalLabel = tk.Label(
       bottomFrame,
       text=f"Total Calories: {totalCalories}",
       fg="white",
       bg=DARK,
       font=("Arial", 15, "bold underline")
   )
   totalCalLabel.pack(pady=10)

# FOOD LABEL + ENTRY
def food():
   global foodEntry
   foodLabel = tk.Label(
       mainFrame, text="Food Name:",
       bg=LIGHT, fg="black",
       font=("Arial", 12, "bold")
   )
   foodLabel.grid(row=0, column=0)

   foodEntry = tk.Entry(mainFrame, bd=1, relief="solid")
   foodEntry.grid(row=0, column=1)


# CALORIE LABEL + ENTRY
def calorie():
   global caloEntry
   calLabel = tk.Label(
       mainFrame, text="Calories:",
       bg=LIGHT, fg="black",
       font=("Arial", 12, "bold")
   )
   calLabel.grid(row=0, column=3)

   caloEntry = tk.Entry(mainFrame, bd=1, relief="solid")
   caloEntry.grid(row=0, column=4)


# MEAL TYPE COMBOBOX
def meal():
   global mealCombo
   mealLabel = tk.Label(
       mainFrame, text="Meal type:",
       bg=LIGHT, fg="black",
       font=("Arial", 12, "bold")
   )
   mealLabel.grid(row=1, column=1)

   mealCombo = ttk.Combobox(mainFrame, values=["Breakfast", "Lunch", "Dinner", "Snack"])
   mealCombo.grid(row=1, column=2)


# BUTTONS
def add():
   addBtn = tk.Button(
       mainFrame, text="Add Entry", command=addEntry,
       bg=BUTTON, fg="white",
       activebackground=BUTTON_ACTIVE,
       activeforeground="white"
   )
   addBtn.grid(row=2, column=0)


def update():
   updateBtn = tk.Button(
       mainFrame, text="Update Entry", command=updateEntry,
       bg=BUTTON, fg="white",
       activebackground=BUTTON_ACTIVE,
       activeforeground="white"
   )
   updateBtn.grid(row=2, column=2)


def delete():
   deleteBtn = tk.Button(
       mainFrame, text="Delete Entry", command=deleteEntry,
       bg=BUTTON, fg="white",
       activebackground=BUTTON_ACTIVE,
       activeforeground="white"
   )
   deleteBtn.grid(row=2, column=4)


# LISTBOX
def listBox():
   global listBoxWidget
   listBoxWidget = tk.Listbox(mainFrame, bg="white", fg="black")
   listBoxWidget.bind("<<ListboxSelect>>", onSelect)
   listBoxWidget.grid(row=3, column=2, sticky="nsew")


# LOGIC: ADD ENTRY
def addEntry():
   food = foodEntry.get()
   cal = caloEntry.get()
   meal = mealCombo.get()

   item = f"{food} Cal: {cal} Meal: {meal}"
   listBoxWidget.insert(END, item)


# LOGIC: WHEN SELECTED
def onSelect(event):
   try:
       index = listBoxWidget.curselection()[0]
       item = listBoxWidget.get(index)

       parts = item.split(" Cal: ")
       food = parts[0]

       cal_and_meal = parts[1].split(" Meal: ")
       cal = cal_and_meal[0]
       meal = cal_and_meal[1]

       foodEntry.delete(0, END)
       foodEntry.insert(0, food)

       caloEntry.delete(0, END)
       caloEntry.insert(0, cal)

       mealCombo.set(meal)

   except:
       pass


# LOGIC: UPDATE
def updateEntry():
   try:
       index = listBoxWidget.curselection()[0]

       updated_food = foodEntry.get()
       updated_cal = caloEntry.get()
       updated_meal = mealCombo.get()

       new_item = f"{updated_food} Cal: {updated_cal} Meal: {updated_meal}"

       listBoxWidget.delete(index)
       listBoxWidget.insert(index, new_item)
       listBoxWidget.select_set(index)

   except:
       pass


# LOGIC: DELETE
def deleteEntry():
   try:
       index = listBoxWidget.curselection()[0]
       listBoxWidget.delete(index)
   except:
       pass


# MENU (unchanged)
def menu():
   menuBar = tk.Menu(root)
   fileOpt = tk.Menu(menuBar, tearoff=0)
   menuBar.add_cascade(label="Choices", menu=fileOpt)
   return menuBar


# INIT
title()
food()
calorie()
meal()
add()
update()
delete()
totalCal()
listBox()

root.config(menu=menu(), bg=LIGHT)
root.mainloop()
