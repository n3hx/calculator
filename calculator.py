import tkinter as tk
from tkinter import ttk
import math
from tkinter import *
import threading
from threading import Thread, Semaphore

# Create a lock object
lock = threading.Lock()

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('642x760')
        self.root.resizable(False, False)
        self.root.configure(bg='black')
        self.root.title("Scientific Calculator")

        # Create the display entry
        self.display = tk.Entry(self.root, width=40, fg='white', bg='#00CED1', font=("Arial", 18))
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Create buttons
        self.buttons = [
            '!', 'sqrt', 'x^2', 'x^3', 'log', 'ln',
            'e', '1/x', 'sin', 'cos', 'tan', 'exp',
            '(', ')', ',',
            '7', '8', '9', 'C', 'AC',
            '4', '5', '6', '*', '/',
            '1', '2', '3', '+', '-',
            '0', '.', 'π', '2dp', '='
        ]

        self.row = 1
        self.col = 0
        # Semaphore to synchronize button clicks
        self.semaphore = Semaphore(1)
        # Flag to toggle decimal places
        self.display_two_decimal = False

        # Turquoise shades
        colors = ['#00FFFF', '#00EBEB', '#00D7D7', '#00C3C3', '#00AFAF']
        # Font colors (purple shades)
        font_colors = ['#8B008B', '#7B008B', '#6A5ACD', '#483D8B', '#4B0082']
        # Background colors (lively turquoise shades)
        bg_colors = ['#00FFD1', '#00FFB6', '#00FF9B', '#00FF80',
                     '#00FF65']

        # Create buttons dynamically based on the list
        for button in self.buttons:
            if button == '2dp':
                # Create a special button for decimal places
                btn = tk.Button(
                    self.root, text=button, width=10, height=4, bg=bg_colors[0], fg=font_colors[0],
                    activeforeground=font_colors[0], activebackground=bg_colors[0], font=("Arial", 12, 'bold'),
                    command=lambda btn=button: self.handle_button_click(btn)
                )
                # Rotate background colors to create variation
                bg_colors.append(bg_colors.pop(0))
                # Rotate font colors to create variation
                font_colors.append(font_colors.pop(0))
            elif button == 'C':
                # Create a button for clearing the display
                btn = tk.Button(
                    self.root, text=button, width=10, height=4, bg='#008080', fg='white',
                    font=("Arial", 12, 'bold'), activebackground='#008080', activeforeground='white',
                    command=lambda btn=button: self.handle_button_click(btn)
                )
            elif button == 'AC':
                # Create a button for clearing all
                btn = tk.Button(
                    self.root, text=button, width=10, height=4, bg='#006565', fg='white', activebackground='#006565',
                    activeforeground='white',font=("Arial", 12, 'bold'),
                    command=lambda btn=button: self.handle_button_click(btn)
                )
            else:
                # Create regular buttons
                btn = tk.Button(
                    self.root, text=button, width=10, height=4, bg=bg_colors[0], fg=font_colors[0],
                    activeforeground=font_colors[0], activebackground=bg_colors[0], font=("Arial", 12, 'bold'),
                    command=lambda btn=button: self.handle_button_click(btn)
                )
                # Rotate background colors to create variation
                bg_colors.append(bg_colors.pop(0))
                # Rotate font colors to create variation
                font_colors.append(font_colors.pop(0))

            # Position the button on the grid
            btn.grid(row=self.row, column=self.col, padx=5, pady=5)

            # Update row and column counters for the next button
            self.col += 1
            if self.col > 4:
                self.col = 0
                self.row += 1

    def handle_button_click(self, button):
        # Handle button clicks in a separate thread to avoid freezing the UI
        Thread(target=self.calculate, args=(button,)).start()

    def calculate(self, button):
        # Acquire semaphore to prevent multiple button clicks
        self.semaphore.acquire()

        if button == '=':
            try:
                expression = self.display.get()
                result = eval(expression)
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'C':
            self.display.delete(0, tk.END)
        elif button == 'AC':
            self.display.delete(0, tk.END)
        elif button == 'sin':
            # Handle the 'sin' button separately
            try:
                value = float(self.display.get())
                result = math.sin(math.radians(value))
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'cos':
            # Handle the 'cos' button separately
            try:
                value = float(self.display.get())
                result = math.cos(math.radians(value))
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'tan':
            # Handle the 'tan' button separately
            try:
                value = float(self.display.get())
                result = math.tan(math.radians(value))
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'log':
            # Handle the 'log' button separately
            try:
                value = float(self.display.get())
                result = math.log10(value)
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'sqrt':
            # Handle the 'sqrt' button separately
            try:
                value = float(self.display.get())
                result = math.sqrt(value)
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'exp':
            # Handle the 'exp' button separately
            try:
                value = float(self.display.get())
                result = math.exp(value)
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == '!':
            # Handle the '!' button separately
            try:
                value = int(self.display.get())
                result = math.factorial(value)
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'x^2':
            # Handle the 'x^2' button separately
            try:
                value = float(self.display.get())
                result = math.pow(value, 2)
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'x^3':
            # Handle the 'x^3' button separately
            try:
                value = float(self.display.get())
                result = math.pow(value, 3)
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == '1/x':
            # Handle the '1/x' button separately
            try:
                value = float(self.display.get())
                result = 1 / value
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ZeroDivisionError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Division by zero")
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'ln':
            # Handle the 'ln' button separately
            try:
                value = float(self.display.get())
                result = math.log(value, math.e)
                if self.display_two_decimal:
                    result = round(result, 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'π':
            # Handle the 'π' button separately
            self.display.insert(tk.END, str(math.pi))
        elif button == 'e':
            # Handle the 'e' button separately
            self.display.insert(tk.END, str(math.e))
        elif button == '2dp':
            # Toggle decimal places button
            self.toggle_decimal_places()
        else:
            self.display.insert(tk.END, button)

        self.semaphore.release()  # Release semaphore to allow next button click

    def toggle_decimal_places(self):
        self.display_two_decimal = not self.display_two_decimal

    def run(self):
        self.root.mainloop()


def select_unit_type():
    def open_unit_converter():
        # Get the selected unit type from the combobox
        unit_type = unit_type_combobox.get()
        # Close the unit type selection window
        root.destroy()
        # Open the unit converter with the selected unit type
        unit_converter(unit_type)

    # Create a new Tkinter window for unit type selection
    root = tk.Tk()
    root.title("Unit Type Selection")
    root.geometry("300x150")
    root.configure(bg="white")

    # Create a label for unit type selection
    label = tk.Label(root, text="Select Unit Type:", bg='white', fg='purple', font=("Times New Romans", 14, 'bold'),
                     pady=10)
    label.pack()

    # Create a combobox for selecting the unit type
    unit_type_combobox = ttk.Combobox(root, values=['Length', 'Mass', 'Temperature'], font=("Arial", 12))
    # Set the default value
    unit_type_combobox.current(0)
    unit_type_combobox.pack(pady=10)

    # Create a button to confirm the unit type selection
    select_button = tk.Button(root, text="Select", width=10, bg='purple', fg='white', activebackground='purple',
                              activeforeground='white', font=("Arial", 12),
                              command=open_unit_converter)
    select_button.pack()

    root.mainloop()


def unit_converter(unit_type):
    def convert():
        try:
            # Acquire the lock before accessing shared resources
            lock.acquire()
            
            # Conversion logic based on the unit type
            # Get the value to convert from the entry field
            value = float(entry.get())
            # Get the selected source unit from the combobox
            from_unit = from_combobox.get()
            # Get the selected target unit from the combobox
            to_unit = to_combobox.get()

            # Conversion rates for different unit types
            conversion_rates = {
                'Length': {
                    'Meter': {'Meter': 1, 'Foot': 3.28084, 'Inch': 39.3701, 'Centimeter': 100},
                    'Foot': {'Meter': 0.3048, 'Foot': 1, 'Inch': 12, 'Centimeter': 30.48},
                    'Inch': {'Meter': 0.0254, 'Foot': 0.0833333, 'Inch': 1, 'Centimeter': 2.54},
                    'Centimeter': {'Meter': 0.01, 'Foot': 0.0328084, 'Inch': 0.393701, 'Centimeter': 1}
                },
                'Mass': {
                    'Kilogram': {'Kilogram': 1, 'Pound': 2.20462, 'Ounce': 35.274, 'Gram': 1000},
                    'Pound': {'Kilogram': 0.453592, 'Pound': 1, 'Ounce': 16, 'Gram': 453.59237},
                    'Ounce': {'Kilogram': 0.0283495, 'Pound': 0.0625, 'Ounce': 1, 'Gram': 28.3495231},
                    'Gram': {'Kilogram': 0.001, 'Pound': 0.00220462, 'Ounce': 0.03527396, 'Gram': 1}
                },
                'Temperature': {
                    'Celsius': {'Celsius': 1, 'Fahrenheit': 33.8, 'Kelvin': 274.15},
                    'Fahrenheit': {'Celsius': -17.2222, 'Fahrenheit': 1, 'Kelvin': 255.928},
                    'Kelvin': {'Celsius': -272.15, 'Fahrenheit': -457.87, 'Kelvin': 1}
                }
            }

            # Perform the conversion calculation
            result = value * conversion_rates[unit_type][from_unit][to_unit]
            # Update the converted label with the result
            converted_label.config(text=str(result))

        except ValueError:
            # Display an error message for invalid input
            converted_label.config(text='Invalid input')
        except Exception as e:
            # Display a generic error message
            converted_label.config(text='Error: {}'.format(str(e)))
        finally:
            # Release the lock to allow other threads to access shared resources
            lock.release()
            

    def clear():
        # Clear the entry field
        entry.delete(0, tk.END)
        # Clear the converted label
        converted_label.config(text='')

    def round_up():
        try:
            # Acquire the lock before accessing shared resources
            lock.acquire()
            
            # Get the value to convert from the entry field
            value = float(entry.get())
            # Get the selected source unit from the combobox
            from_unit = from_combobox.get()
            # Get the selected target unit from the combobox
            to_unit = to_combobox.get()

            # Conversion rates for different unit types
            conversion_rates = {
                'Length': {
                    'Meter': {'Meter': 1, 'Foot': 3.28084, 'Inch': 39.3701, 'Centimeter': 100},
                    'Foot': {'Meter': 0.3048, 'Foot': 1, 'Inch': 12, 'Centimeter': 30.48},
                    'Inch': {'Meter': 0.0254, 'Foot': 0.0833333, 'Inch': 1, 'Centimeter': 2.54},
                    'Centimeter': {'Meter': 0.01, 'Foot': 0.0328084, 'Inch': 0.393701, 'Centimeter': 1}
                },
                'Mass': {
                    'Kilogram': {'Kilogram': 1, 'Pound': 2.20462, 'Ounce': 35.274, 'Gram': 1000},
                    'Pound': {'Kilogram': 0.453592, 'Pound': 1, 'Ounce': 16, 'Gram': 453.59237},
                    'Ounce': {'Kilogram': 0.0283495, 'Pound': 0.0625, 'Ounce': 1, 'Gram': 28.3495231},
                    'Gram': {'Kilogram': 0.001, 'Pound': 0.00220462, 'Ounce': 0.03527396, 'Gram': 1}
                },
                'Temperature': {
                    'Celsius': {'Celsius': 1, 'Fahrenheit': 33.8, 'Kelvin': 274.15},
                    'Fahrenheit': {'Celsius': -17.2222, 'Fahrenheit': 1, 'Kelvin': 255.928},
                    'Kelvin': {'Celsius': -272.15, 'Fahrenheit': -457.87, 'Kelvin': 1}
                }
            }

            # Perform the conversion calculation
            result = value * conversion_rates[unit_type][from_unit][to_unit]
            # Round the result to 2 decimal places
            result = round(result, 2)
            # Update the converted label with the rounded result
            converted_label.config(text=str(result))

        except ValueError:
            # Display an error message for invalid input
            converted_label.config(text='Invalid input')
        except Exception as e:
            # Display a generic error message
            converted_label.config(text='Error: {}'.format(str(e)))
        finally:
            # Release the lock to allow other threads to access shared resources
            lock.release()

    # Create a new Tkinter window for unit conversion
    root = tk.Tk()
    root.title("Unit Converter")
    root.geometry("570x575")
    root.resizable(False, False)
    root.configure(bg='black')

    entry = tk.Entry(root, width=44, font=("Arial", 14), fg='white', bg='MediumSlateBlue')
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Define the buttons for the calculator
    buttons = [
        {'text': '7', 'row': 3, 'column': 0, 'width': 12, 'height': 5, 'bg': '#8DF3DD', 'fg': '#6A0DAD'},
        {'text': '8', 'row': 3, 'column': 1, 'width': 12, 'height': 5, 'bg': '#7BE6C2', 'fg': '#8C26C3'},
        {'text': '9', 'row': 3, 'column': 2, 'width': 12, 'height': 5, 'bg': '#5EE1A1', 'fg': '#AB47BC'},
        {'text': 'C', 'row': 3, 'column': 3, 'width': 12, 'height': 5, 'bg': 'MediumSlateBlue', 'fg': '#FFFFFF',
         'command': clear},
        {'text': '4', 'row': 4, 'column': 0, 'width': 12, 'height': 5, 'bg': '#8DF3DD', 'fg': '#6A0DAD'},
        {'text': '5', 'row': 4, 'column': 1, 'width': 12, 'height': 5, 'bg': '#7BE6C2', 'fg': '#8C26C3'},
        {'text': '6', 'row': 4, 'column': 2, 'width': 12, 'height': 5, 'bg': '#5EE1A1', 'fg': '#AB47BC'},
        {'text': 'AC', 'row': 4, 'column': 3, 'width': 12, 'height': 5, 'bg': 'MediumSlateBlue', 'fg': '#FFFFFF',
         'command': clear},
        {'text': '1', 'row': 5, 'column': 0, 'width': 12, 'height': 5, 'bg': '#8DF3DD', 'fg': '#6A0DAD'},
        {'text': '2', 'row': 5, 'column': 1, 'width': 12, 'height': 5, 'bg': '#7BE6C2', 'fg': '#8C26C3'},
        {'text': '3', 'row': 5, 'column': 2, 'width': 12, 'height': 5, 'bg': '#5EE1A1', 'fg': '#AB47BC'},
        {'text': '0', 'row': 4, 'column': 0, 'width': 12, 'height': 5, 'bg': '#8DF3DD', 'fg': '#6A0DAD',
         'command': lambda: entry.insert(tk.END, '0')},
        {'text': '.', 'row': 5, 'column': 3, 'width': 12, 'height': 5, 'bg': '#7BE6C2', 'fg': '#8C26C3'},
        {'text': ',', 'row': 6, 'column': 3, 'width': 12, 'height': 5, 'bg': '#7BE6C2', 'fg': '#8C26C3'},
        {'text': '2dp', 'row': 6, 'column': 2, 'width': 12, 'height': 5, 'bg': '#5EE1A1', 'fg': '#AB47BC',
         'command': round_up}
    ]

    for button in buttons:
        btn = tk.Button(root, text=button['text'], width=button['width'], height=button['height'],
                        bg=button['bg'], fg=button['fg'], font=("Arial", 12, 'bold'), activebackground=button['bg'],
                        activeforeground=button['fg'],
                        command=button.get('command', lambda btn=button['text']: entry.insert(tk.END, btn)))
        btn.grid(row=button['row'], column=button['column'], columnspan=button.get('columnspan', 1), padx=2, pady=2)

    from_combobox = ttk.Combobox(root, values=[], font=("Arial", 12), state="readonly")
    from_combobox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    to_combobox = ttk.Combobox(root, values=[], font=("Arial", 12), state="readonly")
    to_combobox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Set the values for the comboboxes based on the selected unit type
    if unit_type == "Length":
        from_combobox['values'] = ['Meter', 'Foot', 'Inch', 'Centimeter']
        to_combobox['values'] = ['Foot', 'Meter', 'Inch', 'Centimeter']
    elif unit_type == "Mass":
        from_combobox['values'] = ['Kilogram', 'Gram', 'Ounce', 'Pound']
        to_combobox['values'] = ['Kilogram', 'Gram', 'Ounce', 'Pound']
    else:
        from_combobox['values'] = ['Celsius', 'Kelvin', 'Fahrenheit']
        to_combobox['values'] = ['Celsius', 'Kelvin', 'Fahrenheit']

    # Set the default value for the source unit combobox
    from_combobox.current(0)
    # Set the default value for the target unit combobox
    to_combobox.current(0)

    convert_button = tk.Button(root, text='Convert', width=28, height=5, bg='MediumAquaMarine', fg='MediumPurple',
                               font=("Arial", 12, 'bold'), command=convert, activeforeground='MediumPurple',
                               activebackground='MediumAquaMarine')
    convert_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    converted_label = tk.Label(root, text='', font=("Arial", 14), fg='white', bg='MediumSlateBlue')
    converted_label.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

    root.mainloop()


def number_converter():
    def convert():
        # Get the value and conversion type from the user input
        value = entry.get()
        conversion_type = conversion_combobox.get()

        try:
            # Acquire the lock before accessing shared resources
            lock.acquire()
            
            # Convert binary to decimal
            if conversion_type == 'Binary to Decimal':
                result = int(value, 2)
            # Convert decimal to binary
            elif conversion_type == 'Decimal to Binary':
                result = bin(int(value))[2:]
            # Convert decimal to hexadecimal
            elif conversion_type == 'Decimal to Hexadecimal':
                result = hex(int(value))[2:]
            # Convert hexadecimal to decimal
            elif conversion_type == 'Hexadecimal to Decimal':
                result = int(value, 16)
            else:
                # No conversion needed, return the input as it is
                result = value

            converted_label.config(text=str(result))
        except ValueError:
            # Display error message for invalid input
            converted_label.config(text='Invalid input')
        except Exception as e:
            # Display generic error message
            converted_label.config(text='Error: {}'.format(str(e)))
        finally:
            # Release the lock to allow other threads to access shared resources
            lock.release()
       	
	
	
    def clear():
        # Clear the input field and the converted label
        entry.delete(0, tk.END)
        converted_label.config(text='')

    root = tk.Tk()
    root.title("Number Converter")
    root.geometry("582x665")
    root.resizable(False, False)
    root.configure(bg="black")

    entry = tk.Entry(root, width=47, font=("Arial", 14), bg="DarkTurquoise")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Define the buttons with their properties
    buttons = [
        {'text': '1', 'row': 5, 'column': 0, 'width': 12, 'height': 5, 'bg': '#8DF3DD', 'fg': '#6A0DAD'},
        {'text': '2', 'row': 5, 'column': 1, 'width': 12, 'height': 5, 'bg': '#7BE6C2', 'fg': '#8C26C3'},
        {'text': '3', 'row': 5, 'column': 2, 'width': 12, 'height': 5, 'bg': '#5EE1A1', 'fg': '#AB47BC'},
        {'text': 'A', 'row': 5, 'column': 3, 'width': 12, 'height': 5, 'bg': '#00CC99', 'fg': '#6A0DAD'},
        {'text': '4', 'row': 6, 'column': 0, 'width': 12, 'height': 5, 'bg': '#8DF3DD', 'fg': '#6A0DAD'},
        {'text': '5', 'row': 6, 'column': 1, 'width': 12, 'height': 5, 'bg': '#7BE6C2', 'fg': '#8C26C3'},
        {'text': '6', 'row': 6, 'column': 2, 'width': 12, 'height': 5, 'bg': '#5EE1A1', 'fg': '#AB47BC'},
        {'text': 'B', 'row': 6, 'column': 3, 'width': 12, 'height': 5, 'bg': '#00BFA5', 'fg': '#8C26C3'},
        {'text': '7', 'row': 7, 'column': 0, 'width': 12, 'height': 5, 'bg': '#8DF3DD', 'fg': '#6A0DAD'},
        {'text': '8', 'row': 7, 'column': 1, 'width': 12, 'height': 5, 'bg': '#7BE6C2', 'fg': '#8C26C3'},
        {'text': '9', 'row': 7, 'column': 2, 'width': 12, 'height': 5, 'bg': '#5EE1A1', 'fg': '#AB47BC'},
        {'text': 'C', 'row': 7, 'column': 3, 'width': 12, 'height': 5, 'bg': '#009688', 'fg': '#AB47BC'},
        {'text': '0', 'row': 8, 'column': 0, 'width': 12, 'height': 5, 'bg': '#8DF3DD', 'fg': '#6A0DAD',
         'command': lambda: entry.insert(tk.END, '0')},
        {'text': 'D', 'row': 8, 'column': 1, 'width': 12, 'height': 5, 'bg': '#7BE6C2', 'fg': '#8C26C3'},
        {'text': 'E', 'row': 8, 'column': 2, 'width': 12, 'height': 5, 'bg': '#5EE1A1', 'fg': '#AB47BC'},
        {'text': 'F', 'row': 8, 'column': 3, 'width': 12, 'height': 5, 'bg': '#009688', 'fg': '#AB47BC'}
    ]

    for button in buttons:
        # Create buttons dynamically based on the list
        btn = tk.Button(root, text=button['text'], width=button['width'], height=button['height'],
                        bg=button['bg'], fg=button['fg'], font=("Arial", 12, 'bold'), activeforeground=button['fg'],
                        activebackground=button['bg'],
                        command=lambda btn=button: entry.insert(tk.END, btn['text']))
        btn.grid(row=button['row'], column=button['column'], padx=3, pady=3)

    convert_button = tk.Button(root, text='Convert', width=28, height=5, bg='#8DF3DD', fg='MediumPurple',
                               font=("Arial", 12, 'bold'), activebackground='#8DF3DD', activeforeground='MediumPurple',
                               command=convert)
    convert_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    clear_button = tk.Button(root, text='Clear', width=28, height=5, bg='#009688', fg='#8C26C3',
                             activebackground='#009688', activeforeground='#8C26C3',font=("Arial", 12, 'bold'),
                             command=clear)
    clear_button.grid(row=9, column=2, columnspan=2, padx=5, pady=5)

    conversion_combobox = ttk.Combobox(root, values=['Binary to Decimal', 'Decimal to Binary', 'Decimal to Hexadecimal',
                                                     'Hexadecimal to Decimal'], font=("Arial", 12))
    conversion_combobox.current(0)
    conversion_combobox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    converted_label = tk.Label(root, text='', font=("Arial", 14), bg="DarkTurquoise")
    converted_label.grid(row=3, column=2, columnspan=3, padx=5, pady=5)

    root.mainloop()


def calculate_area():
    def calculate():
        # Retrieve the input values and selected shape
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        shape = shape_combobox.get()

        # Calculate area of a rectangle
        if shape == 'Rectangle':
            result = value1 * value2
        # Calculate area of a triangle
        elif shape == 'Triangle':
            result = 0.5 * value1 * value2
        # Calculate area of a circle
        elif shape == 'Circle':
            result = math.pi * value1 ** 2
        else:
            result = 0

        # Display the calculated area
        area_label.config(text=str(result))

    def round_result():
        result = float(area_label.cget("text"))
        # Round the result to 2 decimal places
        result = round(result, 2)
        # Update the label with the rounded result
        area_label.config(text=str(result))

    def insert_button_value(btn):
        # Insert the button value at the end of the active entry field
        active_entry.insert(tk.END, btn)

    def set_active_entry(entry):
        global active_entry
        # Set the active entry field to the one that received focus
        active_entry = entry

    def clear():
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        area_label.config(text='')

    root = tk.Tk()
    root.title("Area Calculator")
    root.geometry("530x665")
    root.resizable(False, False)
    root.configure(bg="black")

    style = ttk.Style()
    style.configure('TEntry', font=("Arial", 20))
    style.configure('TLabel', font=("Arial", 20))

    shape_combobox = ttk.Combobox(root, values=['Rectangle', 'Triangle', 'Circle'], font=("Arial", 12))
    shape_combobox.current(0)
    shape_combobox.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    label1 = tk.Label(root, text='Length/Radius:', font=("Arial", 12), bg='black', fg='#69F0AE')
    label1.grid(row=1, column=0, padx=10, pady=10)

    entry1 = ttk.Entry(root, width=15)
    entry1.grid(row=1, column=1, padx=10, pady=10)

    label2 = tk.Label(root, text='Width/Height:', font=("Arial", 12), bg='black', fg='#69F0AE')
    label2.grid(row=2, column=0, padx=10, pady=10)

    entry2 = ttk.Entry(root, width=15)
    entry2.grid(row=2, column=1, padx=10, pady=10)

    calculate_button = tk.Button(root, text='=', width=10, height=18,
                                 font=("Arial", 12, 'bold'), command=calculate,
                                 bg='#00C853', fg='#512DA8', activebackground='#00C853', activeforeground='#512DA8')
    calculate_button.grid(row=6, column=3, rowspan=3, padx=5, pady=5)

    clear_button = tk.Button(root, text='Clear', width=10, height=5,
                             font=("Arial", 12, 'bold'), command=clear,
                             bg='#1DE9B6', fg='#9C27B0', activebackground='#1DE9B6', activeforeground='#9C27B0')
    clear_button.grid(row=5, column=3, padx=5, pady=5)

    area_label = tk.Label(root, text='', font=("Arial", 14), bg='#69F0AE', fg='white')
    area_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Define the buttons with their properties
    buttons = [
        {'text': '7', 'row': 5, 'column': 0, 'width': 10, 'height': 5, 'active-foreground': '#69F0AE', 'bg': '#69F0AE',
         'fg': '#9C27B0'},
        {'text': '8', 'row': 5, 'column': 1, 'width': 10, 'height': 5, 'bg': '#00E676', 'fg': '#673AB7'},
        {'text': '9', 'row': 5, 'column': 2, 'width': 10, 'height': 5, 'bg': '#00C853', 'fg': '#512DA8'},
        {'text': '4', 'row': 6, 'column': 0, 'width': 10, 'height': 5, 'bg': '#69F0AE', 'fg': '#9C27B0'},
        {'text': '5', 'row': 6, 'column': 1, 'width': 10, 'height': 5, 'bg': '#00E676', 'fg': '#673AB7'},
        {'text': '6', 'row': 6, 'column': 2, 'width': 10, 'height': 5, 'bg': '#00C853', 'fg': '#512DA8'},
        {'text': '1', 'row': 7, 'column': 0, 'width': 10, 'height': 5, 'bg': '#69F0AE', 'fg': '#9C27B0'},
        {'text': '2', 'row': 7, 'column': 1, 'width': 10, 'height': 5, 'bg': '#00E676', 'fg': '#673AB7'},
        {'text': '3', 'row': 7, 'column': 2, 'width': 10, 'height': 5, 'bg': '#00C853', 'fg': '#512DA8'},
        {'text': '0', 'row': 8, 'column': 1, 'width': 10, 'height': 5, 'bg': '#69F0AE', 'fg': '#9C27B0',
         'command': lambda: insert_button_value('0')},
        {'text': '.', 'row': 8, 'column': 2, 'width': 10, 'height': 5, 'bg': '#00E676', 'fg': '#673AB7'},
        {'text': '2dp', 'row': 8, 'column': 0, 'width': 10, 'height': 5, 'bg': '#1DE9B6', 'fg': '#512DA8',
         'command': round_result},
    ]

    for button in buttons:
        # Create buttons dynamically based on the list
        btn = tk.Button(root, text=button['text'], width=button['width'], height=button['height'],
                        activebackground=button['bg'], bg=button['bg'], fg=button['fg'], font=("Arial", 12, 'bold'),
                        activeforeground=button['fg'],
                        command=button.get('command', lambda btn=button['text']: insert_button_value(btn)))
        btn.grid(row=button['row'], column=button['column'], padx=2, pady=2)

    entry1.bind("<FocusIn>", lambda event: set_active_entry(entry1))
    entry2.bind("<FocusIn>", lambda event: set_active_entry(entry2))

    root.mainloop()


def calculate_quadratic():
    def calculate():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())

            discriminant = (b ** 2) - (4 * a * c)

            if discriminant > 0:
                root1 = (-b + math.sqrt(discriminant)) / (2 * a)
                root2 = (-b - math.sqrt(discriminant)) / (2 * a)
                result.config(text="Roots: {} and {}".format(root1, root2))
            elif discriminant == 0:
                root = -b / (2 * a)
                result.config(text="Root: {}".format(root))
            else:
                result.config(text="No real roots")
        except ValueError:
            result.config(text="Invalid input. Please enter valid numeric values.")
        except Exception as e:
            result.config(text="Error: " + str(e))

    def round_result():
        result_text = result.cget("text")

        if result_text:
            result_value = float(result_text)
            result_value = round(result_value, 2)
            result.config(text=str(result_value))

    def insert_button_value(btn):
        active_entry.insert(tk.END, btn)

    def set_active_entry(entry):
        global active_entry
        active_entry = entry

    def clear():
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        entry_c.delete(0, tk.END)
        result.config(text='')

    root = tk.Tk()
    root.title("Quadratic Calculator")
    root.geometry("1040x780")
    root.resizable(False, False)
    root.configure(bg="black")

    # Creating the labels for coefficients
    label_a = tk.Label(root, text='Input a:', font=("Arial", 12), bg='black', fg='#69F0AE')
    label_a.grid(row=0, column=0, padx=10, pady=10, sticky="E")

    label_b = tk.Label(root, text='Input b:', font=("Arial", 12), bg='black', fg='#69F0AE')
    label_b.grid(row=1, column=0, padx=10, pady=10, sticky="E")

    label_c = tk.Label(root, text='Input c:', font=("Arial", 12), bg='black', fg='#69F0AE')
    label_c.grid(row=2, column=0, padx=10, pady=10, sticky="E")

    # Creating the Entry widgets for coefficients
    entry_a = tk.Entry(root, width=30, justify="center")
    entry_a.grid(row=0, column=1, padx=10, pady=10)

    entry_b = tk.Entry(root, width=30, justify="center")
    entry_b.grid(row=1, column=1, padx=10, pady=10)

    entry_c = tk.Entry(root, width=30, justify="center")
    entry_c.grid(row=2, column=1, padx=10, pady=10)

    # Creating the Calculate Quadratic button
    calculate_button = tk.Button(root, text='=', width=25, height=23,
                                 font=("Arial", 12, 'bold'), command=calculate,
                                 bg='#00C853', fg='#512DA8', activebackground='#00C853', activeforeground='#512DA8')
    calculate_button.grid(row=6, column=3, rowspan=3, padx=1, pady=1)

    clear_button = tk.Button(root, text='Clear', width=25, height=7,
                             font=("Arial", 12, 'bold'), command=clear,
                             bg='#1DE9B6', fg='#9C27B0', activebackground='#1DE9B6', activeforeground='#9C27B0')
    clear_button.grid(row=5, column=3, padx=1, pady=1)

    # Creating the label for displaying roots
    result = tk.Label(root, text='', font=("Arial", 14), bg='#69F0AE', fg='white')
    result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Creating number buttons
    buttons = [
    {'text': '7', 'row': 5, 'column': 0, 'width': 25, 'height': 7, 'active-foreground': '#69F0AE', 'bg': '#69F0AE','fg': '#9C27B0'},
    {'text': '8', 'row': 5, 'column': 1, 'width': 25, 'height': 7, 'bg': '#00E676', 'fg': '#673AB7'},
    {'text': '9', 'row': 5, 'column': 2, 'width': 25, 'height': 7, 'bg': '#00C853', 'fg': '#512DA8'},
    {'text': '4', 'row': 6, 'column': 0, 'width': 25, 'height': 7, 'bg': '#69F0AE', 'fg': '#9C27B0'},
    {'text': '5', 'row': 6, 'column': 1, 'width': 25, 'height': 7, 'bg': '#00E676', 'fg': '#673AB7'},
    {'text': '6', 'row': 6, 'column': 2, 'width': 25, 'height': 7, 'bg': '#00C853', 'fg': '#512DA8'},
    {'text': '1', 'row': 7, 'column': 0, 'width': 25, 'height': 7, 'bg': '#69F0AE', 'fg': '#9C27B0'},
    {'text': '2', 'row': 7, 'column': 1, 'width': 25, 'height': 7, 'bg': '#00E676', 'fg': '#673AB7'},
    {'text': '3', 'row': 7, 'column': 2, 'width': 25, 'height': 7, 'bg': '#00C853', 'fg': '#512DA8'},
    {'text': '0', 'row': 8, 'column': 1, 'width': 25, 'height': 7, 'bg': '#69F0AE', 'fg': '#9C27B0', 'command': lambda: insert_button_value('0')},
    {'text': '.', 'row': 8, 'column': 2, 'width': 25, 'height': 7, 'bg': '#00E676', 'fg': '#673AB7'},
    {'text': '2dp', 'row': 8, 'column': 0, 'width': 25, 'height': 7, 'bg': '#1DE9B6', 'fg': '#512DA8', 'command': round_result},
    ]

    for button in buttons:
    	btn = tk.Button(root, text=button['text'], width=button['width'], height=button['height'],
                    activebackground=button['bg'], bg=button['bg'], fg=button['fg'],
                    font=("Arial", 12, 'bold'), activeforeground=button['fg'],
                    command=button.get('command', lambda btn=button['text']: insert_button_value(btn)))
    	btn.grid(row=button['row'], column=button['column'], padx=2, pady=2)

    entry_a.bind("<FocusIn>", lambda event: set_active_entry(entry_a))
    entry_b.bind("<FocusIn>", lambda event: set_active_entry(entry_b))
    entry_c.bind("<FocusIn>", lambda event: set_active_entry(entry_c))

    root.mainloop()


def open_calculator():
    calculator = Calculator()
    calculator.run()


def open_unit_converter():
    select_unit_type()
    # Create and start a new thread for unit converter
    unit_converter_thread = threading.Thread(target=unit_converter, args=("Length",))
    unit_converter_thread.start()


def open_calculate_area():
    calculate_area()


def open_number_converter():
    # Create and start a new thread for number converter
    number_converter_thread = threading.Thread(target=number_converter)
    number_converter_thread.start()


def open_calculate_quadratic():
    calculate_quadratic()
    
    
def main_menu():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("900x450")
    root.resizable(False, False)
    root.configure(bg="white")

    def exit_program():
        root.destroy()

    # Create an image label
    Img1 = PhotoImage(file=r'/home/ur053/hi.png')
    Label(root, image=Img1, bg='white').place(x=15, y=120)

    # Create a heading label
    Heading3 = Label(text='MENU', fg='white', bg='purple', font=('Times New Romans', 30, 'bold'), width=35,
                     height=2)
    Heading3.place(x=0, y=0)

    # Create buttons for different functionalities
    calculator_button = tk.Button(root, text="Calculator", width=25, height=3, font=("Arial", 12, 'bold'), fg='white',
                                  bg='purple', activeforeground='white', activebackground='purple',
                                  command=open_calculator)
    calculator_button.place(x=320, y=120)

    unit_converter_button = tk.Button(root, text="Unit Converter", width=25, height=3, font=("Arial", 12, 'bold'),
                                      fg='white', bg='purple', activeforeground='white',
                                      activebackground='purple', command=open_unit_converter)
    unit_converter_button.place(x=600, y=120)

    number_converter_button = tk.Button(root, text="Number Converter", width=25, height=3, font=("Arial", 12, 'bold'),
                                        fg='white', bg='purple', activeforeground='white',
                                        activebackground='purple', command=open_number_converter)
    number_converter_button.place(x=600, y=240)

    area_calculator_button = tk.Button(root, text="Area Calculator", width=25, height=3, font=("Arial", 12, 'bold'),
                                       fg='white', bg='purple', activeforeground='white',
                                       activebackground='purple', border=2, command=open_calculate_area)
    area_calculator_button.place(x=320, y=240)

    exit_button = tk.Button(root, text="Exit", width=25, height=3, bg='purple', fg='white',
                            font=("Arial", 12, 'bold'),
                            activebackground='purple', activeforeground='white', command=exit_program)
    exit_button.place(x=600, y=360)
    
    quadratic_button = tk.Button(root, text="Quadratic Equation Solver", width=25, height=3, font=("Arial", 12, 'bold'), fg='white', bg='purple', activeforeground='white', activebackground='purple', border=2, command=open_calculate_quadratic)
    quadratic_button.place(x=320, y=360)

    root.mainloop()


def open_window():
    root1 = tk.Tk()
    root1.title("Calculator App")
    root1.geometry("780x400")
    root1.resizable(False, False)
    root1.configure(bg="white")

    def open():
        root1.destroy()
        main_menu()

    # Create a heading label for the calculator app
    Heading1 = Label(text='Calculator', fg='purple', bg='white',
                     activebackground='white', font=('Times New Roman', 40, 'bold', 'italic'))
    Heading1.place(x=390, y=90)

    # Create a subheading label for the calculator app
    Heading2 = Label(text='App', fg='purple', bg='white',
                     activebackground='white', font=('Times New Roman', 40, 'bold', 'italic'))
    Heading2.place(x=440, y=150)

    # Add an image label
    Img = PhotoImage(file=r'/home/ur053/hi.png')
    Label(root1, image=Img, bg='white').place(x=20, y=40)

    # Create an 'OPEN' button to open the main menu
    OpenButton = Button(text='OPEN', fg='white', bg='purple', activebackground='purple', border=0,
                        activeforeground='white', font=('Times New Romans', 23, 'bold'), width=20, height=1,
                        command=open)
    OpenButton.place(x=300, y=250)

    root1.mainloop()


def main():
    open_window()


if __name__ == '__main__':
    main()
