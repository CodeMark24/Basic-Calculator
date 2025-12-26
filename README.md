Basic Calculator (Tkinter)
This is a simple graphical user interface (GUI) calculator built using Python's built-in Tkinter library. It provides basic arithmetic functionality including addition, subtraction, multiplication, and division.

Features
Clean Interface: Uses a grid layout for organized button placement.

Basic Arithmetic: Supports operations for addition (+), subtraction (-), multiplication (*), and division (/).

Clear Function: Includes a 'C' button to reset the display entry.

Error Handling: Displays an "Error" message if an invalid mathematical expression is entered.

Dynamic Button Creation: Buttons are generated programmatically for cleaner code.

Prerequisites
To run this application, you only need:

Python 3.x: Tkinter is usually included with standard Python installations.

How to Run
Save the code: Copy the provided code and save it as calculator.py.

Open Terminal/Command Prompt: Navigate to the directory where you saved the file.

Execute the script:

Bash

python calculator.py
Code Logic Overview
Display: Uses a tk.Entry widget to show both input and results.

Calculation: Utilizes the eval() function to parse and calculate the string expression from the entry field.

Layout Management: Uses the .grid() method to arrange buttons in a structured 4-column format.

Lambda Functions: Implements lambda in the button command to pass specific values to the button_click function without executing them immediately upon startup.

Important Note
This calculator uses the eval() function to compute results. While efficient for simple desktop applications, eval() executes string input as Python code. In a local GUI environment, this is generally acceptable, but it should be used with caution in web-based or production environments involving untrusted user input.
