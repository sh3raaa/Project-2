import tkinter as tk
from tkinter import ttk, END

#VARIABLES
totalCalories = 0
listBoxList = []
foodEntry = None
listBox = None
listBoxWidget= None

#ROOT
root = tk.Tk()
root.title("Calorie App")
root.geometry("700x500")

#FRAMES
titleFrame = tk.Frame(root, bg= "blue")
titleFrame.pack(fill="x")

mainFrame = tk.Frame(root, bg= "lightblue")
mainFrame.pack(fill= "both", expand= True)

bottomFrame = tk.Frame(root,bg="red")
bottomFrame.pack(fill="x", side="bottom")

# Create grid of cells here
for r in range(3):
    mainFrame.rowconfigure(r, weight=1, uniform= "row")

for c in range(5):
    mainFrame.columnconfigure(c, weight=1, uniform = "column")

# for r in range(5):
#         for c in range(5):
#             cell = tk.Label(mainFrame, text=f"{r},{c}", borderwidth=1, relief="solid")
#             cell.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)



def title():

    title = tk.Label(titleFrame, text="Welcome to ourCal",background="lightgrey", fg = "black", font=("Arial", 15, "bold") )
    title.pack()

def totalCal():
    totalCalLabel = tk.Label(bottomFrame, text=f"Total Calories: {totalCalories}", fg = "black", font=("Arial", 15, "bold underline") )
    totalCalLabel.pack(pady=10)

def food():
    global foodEntry

    food = tk.Label(mainFrame, text="Food Name:",background="lightblue", fg = "black", font=("Arial", 12, "bold") )
    food.grid(row=0, column=0, sticky="")

    foodEntry = tk.Entry(mainFrame, bd= 1, relief="solid")
    foodEntry.grid(row=0, column= 1)

def calorie():

    calorie = tk.Label(mainFrame, text="Calories:",background="lightblue", fg = "black", font=("Arial", 12, "bold") )
    calorie.grid(row=0, column=3)

    caloEntry = tk.Entry(mainFrame, bd = 1, relief="solid" )
    caloEntry.grid(row=0, column= 4, sticky="")

def meal ():

    meal = tk.Label(mainFrame, text="Meal type:", bg = "lightblue", fg= "black", font=("Arial", 12, "bold") )
    meal.grid(row=1,column=1)
    mealCombo = ttk.Combobox(mainFrame, values = ["Breakfast", "Lunch", "Dinner", "Snack"])
    mealCombo.grid(row=1, column= 2)

def menu ():
    menuBar = tk.Menu(root)
    fileOpt = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Choices", menu=fileOpt)

def add():
    addBtn = tk.Button(mainFrame, text = "Add Entry", command=addEntry)
    addBtn.grid(row=2, column=0)

def update():
    updateBtn = tk.Button(mainFrame, text = "Update Entry", command= updateEntry)
    updateBtn.grid(row=2, column=2)

def delete():
    deleteBtn = tk.Button(mainFrame, text = "Delete Entry", command=deleteEntry)
    deleteBtn.grid(row=2, column=4)

def listBox():
    global listBoxWidget
    listBoxWidget = tk.Listbox(mainFrame)
    listBoxWidget.bind("<<ListboxSelect>>", onSelect)
    listBoxWidget.grid(row=3, column=2)

def addEntry():
    foodText = foodEntry.get()
    listBoxWidget.insert(END, foodText)  #f string ts

#shows/adds what is selected in the listbox to the entry box
def onSelect(event):

        index = listBoxWidget.curselection()[0]
        foodEntry.delete(0, END)
        foodEntry.insert(0, listBoxWidget.get(index))


def updateEntry():

        index = listBoxWidget.curselection()[0]
        listBoxWidget.delete(index)
        listBoxWidget.insert(index, foodEntry.get())

def deleteEntry():
        
        index = listBoxWidget.curselection()[0]
        listBoxWidget.delete(index)

#WINDOWS (OPENING NEW/CLOSING WINDOWS)
def CreateWindow():
    statsWindow = tk.Toplevel()
    statsWindow.geometry("500x500")
    statsWindow.title("Stats data")

# statsButton = tk.Button(mainFrame, text = "Stats window", command= CreateWindow)
# statsButton.grid(row=0, column=0)

def menu ():
    menuBar = tk.Menu(root)
    fileOpt = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Choices", menu=fileOpt)
    return menuBar

title()
food()
calorie()
add()
update()
delete()
meal()
totalCal()
listBox()
root.config(menu=menu(), background= "lightblue") #to display the menu bar with its options, background color
root.mainloop()
