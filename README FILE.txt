README FILE:

Project Title: Python Project Calculator (Coursework 3)

Running Instruction:
	1. python3 calculator.py

Project Description:
	The class "Calculator" creates a scientific calculator with a graphical user interface using the tkinter library. It sets up the calculator window, display, and buttons for various mathematical operations. When a button is clicked, the corresponding calculation or action is performed. The calculator supports functions like factorial, square root, logarithm, trigonometric functions, exponentiation, and basic arithmetic operations. It also has options to toggle decimal places and clear the display. 
	
	The function "select_unit_type" creates a window for selecting a unit type. The function creates a new tkinter window and sets its title, dimensions, and background color. Inside the window, it adds a label asking the user to select a unit type and a dropdown menu with options for unit types such as length, mass, and temperature. There is also a "Select" button that, when clicked, retrieves the selected unit type, closes the unit type selection window, and opens a unit converter window with the selected unit type.
	
	The function "unit_converter(unit_type)" sets up a window for unit conversion. The window includes an input field, buttons for numbers and special actions, comboboxes for selecting source and target units, a "Convert" button, and a label for displaying the converted result. The code performs the conversion based on the selected unit type and updates the result accordingly.

	The function "number_converter" creates a user-friendly number converter using the tkinter library. It sets up a GUI window with an input field, buttons for number input, a combobox for selecting the conversion type, buttons for conversion and clearing, and a label for displaying the result. The nested convert() function handles the actual conversion based on the user's input and selected conversion type, while the clear() function clears the input field and result label. 

	The function "calculate_area" creates a graphical area calculator using the tkinter library. It sets up a window with input fields for length/radius and width/height, a combobox for selecting the shape, buttons for numeric input and calculations, a button for clearing the input, and a label for displaying the calculated area. The code handles different shape calculations based on the user's selection, rounds the result to 2 decimal places, and provides functionality to insert button values into the active entry field.

	The function "calculate_quadratic" creates a graphical quadratic calculator using the tkinter library. It sets up a window with input fields for coefficients a, b, and c, buttons for numeric input and calculations, a button for clearing the input, and a label for displaying the roots of the quadratic equation. The code calculates the roots based on the quadratic formula and displays them accordingly. It also provides functionality to insert button values into the active entry field.

	The function "open_calculator" creates an instance of the Calculator class and assigns it to the variable calculator. It then calls the run() method of the calculator instance, which starts the execution of a calculator application.

	The function "open_unit_converter" calls the select_unit_type() function, which presumably prompts the user to select a unit type. After that, it creates a new thread using the threading.Thread class. The target of the thread is set to a function called unit_converter(), and the argument passed to the unit_converter() function is the string "Length". Finally, the thread is started by calling its start() method, which initiates the execution of the unit_converter() function in the background while allowing the main program to continue running concurrently.

	The function "open_calculate_area" invokes another function called "calculate_area" in other words the purpose of this function is to open a user interface related to calculating areas.

	The function "open_number_converter"  creates a new thread using the threading.Thread class. The target function for the thread is set to "number_converter". The number_converter_thread.start() statement starts the execution of the thread, allowing the number conversion process to run concurrently with the main program.

	The function "open_calculate_quadratic"  invokes the "calculate_quadratic" function in other words the purpose of this function to open the functionality related to quadratic equation calculations.

	The function "main_menu"  creates a graphical user interface window using the tkinter library. The window is titled "Main Menu" and has a fixed size of 900x450 pixels with a white background. The GUI window displays an image label and a heading label at the top. It also includes buttons for "Calculator," "Unit Converter," "Number Converter," "Area Calculator," and "Quadratic Equation Solver." Each button is styled with a specific appearance and executes a corresponding function when clicked. There is an "Exit" button to close the GUI window and terminate the program. 

	The function "open_window" creates a GUI window using the tkinter library. The window is titled "Calculator App" and has a fixed size of 780x400 pixels with a white background. The GUI window displays a heading label with the text "Calculator" and a subheading label with the text "App." An image label is also included in the window. The main feature is an "OPEN" button, styled with a purple background and white text, which triggers the open function when clicked. The open function closes the current window and opens the main menu.