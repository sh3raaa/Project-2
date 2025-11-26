import tkinter as tk
from tkinter import Toplevel, font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#a class for the stats window that will pop up and contains the graph
class StatsWindow:
    def __init__(self, master, entriesList):
        self.top = Toplevel(master)
        self.top.title("Calorie Stats")
        self.top.geometry("640x420")

        #define a named font for labels
        self.labelFont = font.Font(family="Arial", size=12, weight="bold")

        if not entriesList:
            tk.Label(self.top, text="No data available.", font=self.labelFont).pack(pady=20)
            return

        #extract  the calories
        calories = []
        for e in entriesList:
            try:
                calories.append(int(e.get("calories", 0)))
            except:
                pass

        average = sum(calories) / len(calories)

        #bar chart showing the avg versus each entry
        fig, ax = plt.subplots(figsize=(7,3.5))
        ax.axhline(average, color='red', linestyle='--', label=f"Average: {average:.1f}")
        ax.bar(range(len(calories)), calories, label="Entry Calories")

        ax.set_title("Calories per Entry + Average Line")
        ax.set_ylabel("Calories")
        ax.set_xlabel("Entry Number")
        ax.legend()
        ax.grid(axis='y')

        canvas = FigureCanvasTkAgg(fig, master=self.top)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)
