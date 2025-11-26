OurCal – Calorie Tracking App

CCT211 Project 2: Persistent Form

📌 Overview

OurCal is a simple and beginner-friendly Tkinter desktop application that allows users to track their daily food intake and calorie totals.
The program focuses on being easy to use and visually clean, while also demonstrating Python fundamentals:
	•	Tkinter GUI
	•	JSON file storage
	•	Simple data handling
	•	Basic matplotlib statistics
	•	Clear input validation
	•	Organized multi-file structure

⸻

📁 Project Features

1. Add Food Entries

Users can input:
	•	Food name
	•	Calorie amount
	•	Meal type (Breakfast/Lunch/Dinner/Snack)

Entries are displayed in a listbox.

⸻

2. Update & Delete Entries

Selecting an item fills the input fields automatically.
User can:
	•	Edit it and click Update
	•	Or delete it

The total calories update instantly after each change.

⸻

3. Total Daily Calories

A label at the bottom shows the total calories based on all entries in the list.

⸻

4. Clear All

A confirmation popup appears before deleting everything.

⸻

5. Quit Button

A yes/no confirmation window prevents accidental quitting.

⸻

6. Stats Window (Matplotlib)

A simple bar chart showing:
	•	The average calories per meal type
OR
	•	A clean visualization of calorie distribution

⸻

7. JSON Saving

Data is automatically saved in calories_data.json AND a manual “Save” option is available from the menu.

⸻

📂 Project Structure
MainApp.py            # Main application window
entryForm.py          # Handles UI for input fields
caloriesDatabase.py   # JSON loading & saving
statsWindow.py        # Matplotlib stats window
calories_data.json    # Saved data
README.md             # Documentation

⸻

▶️ How to Run the Program
	1.	Ensure Python is installed (3.13.1)
	2.	Install matplotlib (if not installed): pip install matplotlib
	3.	Run the app: python3 MainApp.py

⸻

🧠 Skills Demonstrated
	•	Tkinter layout/grid system
	•	OOP structure for cleaner code
	•	JSON persistence
	•	Basic data visualization
	•	Event handling (listbox select, button commands)
	•	User validation & confirmation dialogs

⸻

👥 Group Contributions

All four group members contributed equally to the design, coding, and testing of this project.
We worked on the assignment together, both in-person and online, often using the Visual Studio Code extension (Live Share) and passing code back-and-forth through email when needed.

Our collaboration included:
	•	Debugging the update feature together
	•	Deciding the layout, fonts, and color scheme
	•	Reviewing each other’s code for clarity
	•	Adding comments and cleaning the structure
	•	Running tests and fixing small issues
	•	Meeting in person to code live and solve UI problems

This project represents shared teamwork and equal participation from all members.

⸻

📜 License

This project is for academic purposes only (CCT211 – University of Toronto Mississauga).
