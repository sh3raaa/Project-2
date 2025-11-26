import tkinter as tk
from tkinter import ttk
from tkinter import font

class EntryForm:
    def __init__(self, parent, bg="#E9F6FB"):
        self.parent = parent
        self.bg = bg

        #named fonts to be used so it doesnt look different on diifferent devices like OS , mac
        self.labelFont = font.Font(family="Arial", size=12, weight="bold")
        self.entryFont = font.Font(family="Arial", size=11)

        #ttk style for the Combobox
        style = ttk.Style()
        style.configure("My.TCombobox", font=self.entryFont)

        self.build()

    def build(self):
        #food labels
        tk.Label(self.parent, text="Food Name:", bg=self.bg, font=self.labelFont)\
            .grid(row=0, column=1, sticky="w", padx=10)

        self.foodEntry = tk.Entry(self.parent, width=28, font=self.entryFont)
        self.foodEntry.grid(row=0, column=2, columnspan=2, sticky="w", padx=5)

        #calories labels
        tk.Label(self.parent, text="Calories:", bg=self.bg, font=self.labelFont)\
            .grid(row=0, column=4, sticky="w", padx=10)

        self.calEntry = tk.Entry(self.parent, width=10, font=self.entryFont)
        self.calEntry.grid(row=0, column=5, sticky="w", padx=5)

        #the meal types
        tk.Label(self.parent, text="Meal type:", bg=self.bg, font=self.labelFont)\
            .grid(row=1, column=2, sticky="e", padx=10)

        self.mealCombo = ttk.Combobox(
            self.parent,
            values=["Breakfast", "Lunch", "Dinner", "Snack"],
            width=18,
            state="readonly",
            style="My.TCombobox"     # apply custom font
        )
        self.mealCombo.grid(row=1, column=3, sticky="w", padx=5)
        self.mealCombo.set("Breakfast")

    def clearFields(self):
        self.foodEntry.delete(0, "end")
        self.calEntry.delete(0, "end")
        self.mealCombo.set("")
