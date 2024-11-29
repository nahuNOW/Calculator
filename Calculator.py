# import time as t

# print("Welcome to the calculator!")
# t.sleep(1)

# # Prompt user for the function
# whatFuncTD = input("Press 1 to add, 2 to subtract, 3 to multiply, and 4 to divide: ")
# t.sleep(1)

# # Defining the functions
# def add():
#     num1 = float(input("What is the first number? "))
#     t.sleep(1)
#     num2 = float(input("What is the second number? "))
#     t.sleep(1)
#     total = num1 + num2
#     print(f"Your total is {total}")

# def subtract():
#     num1 = float(input("What is the first number? "))
#     t.sleep(1)
#     num2 = float(input("What is the second number? "))
#     t.sleep(1)
#     total = num1 - num2
#     print(f"Your total is {total}")

# def multiply():
#     num1 = float(input("What is the first number? "))
#     t.sleep(1)
#     num2 = float(input("What is the second number? "))
#     t.sleep(1)
#     total = num1 * num2
#     print(f"Your product is {total}")

# def divide():
#     num1 = float(input("What is the first number? "))
#     t.sleep(1)
#     num2 = float(input("What is the second number? "))
#     t.sleep(1)
#     if num2 == 0:
#         print("You can't divide by zero")
#     else:
#         total = num1 / num2
#         print(f"Your quotient is {total}")

# # Match the input and run the corresponding function
# if whatFuncTD == "1":
#     add()
# elif whatFuncTD == "2":
#     subtract()
# elif whatFuncTD == "3":
#     multiply()
# elif whatFuncTD == "4":
#     divide()
# else:
#     print("Invalid selection. Try again!")



import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display numbers
display = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 18), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Global variables
current_input = ""
first_number = None
operation = None

# Button click function
def button_click(value):
    global current_input
    current_input += str(value)
    display.delete(0, tk.END)
    display.insert(0, current_input)

# Clear function
def clear():
    global current_input, first_number, operation
    current_input = ""
    first_number = None
    operation = None
    display.delete(0, tk.END)

# Operation functions
def set_operation(op):
    global first_number, current_input, operation
    if current_input:
        first_number = float(current_input)
        operation = op
        current_input = ""
        display.delete(0, tk.END)

def calculate():
    global first_number, current_input, operation
    if first_number is not None and current_input:
        second_number = float(current_input)
        result = 0
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number != 0:
                result = first_number / second_number
            else:
                display.delete(0, tk.END)
                display.insert(0, "Error")
                return
        display.delete(0, tk.END)
        display.insert(0, result)
        current_input = str(result)
        first_number = None
        operation = None

# Buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text.isdigit() or text == "0":
        action = lambda x=text: button_click(x)
    elif text == "C":
        action = clear
    elif text == "=":
        action = calculate
    else:
        action = lambda x=text: set_operation(x)

    button = tk.Button(root, text=text, width=5, height=2, command=action, font=("Arial", 18))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the app
root.mainloop()
