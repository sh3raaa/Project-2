import tkinter as tk
from tkinter import ttk

class EntryForm:
    def __init__(self, parent, bg="#E9F6FB"):
        self.parent = parent
        self.bg = bg
        self.build()

    def build(self):
        #food label
        tk.Label(self.parent, text="Food Name:", bg=self.bg, font=("Arial", 12, "bold")).grid(row=0, column=1, sticky="w", padx=10)
        self.foodEntry = tk.Entry(self.parent, width=28, font=("Arial", 11))
        self.foodEntry.grid(row=0, column=2, columnspan=2, sticky="w", padx=5)

        #calories labell
        tk.Label(self.parent, text="Calories:", bg=self.bg, font=("Arial", 12, "bold")).grid(row=0, column=4, sticky="w", padx=10)
        self.calEntry = tk.Entry(self.parent, width=10, font=("Arial", 11))
        self.calEntry.grid(row=0, column=5, sticky="w", padx=5)

        #the meal type
        tk.Label(self.parent, text="Meal type:", bg=self.bg, font=("Arial", 12, "bold")).grid(row=1, column=2, sticky="e", padx=10)
        self.mealCombo = ttk.Combobox(self.parent, values=["Breakfast", "Lunch", "Dinner", "Snack"], width=18, state="readonly")
        self.mealCombo.grid(row=1, column=3, sticky="w", padx=5)
        self.mealCombo.set("Breakfast")

    def clearFields(self):
        self.foodEntry.delete(0, "end")
        self.calEntry.delete(0, "end")
        self.mealCombo.set("")

        