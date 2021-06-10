"""
A very simple GUI calculator using Tkinker.

The calculator can add, subtract, multiply and divide ints and floats.
It supports negative numbers and converting ints to floats and vice-versa.
"""

# Required import.
from tkinter import *

# Global variables.
number = None
symbol = None


def clear():
    # Clears the output.
    result.delete(0, END)


def positive_negative():
    # Converts positive numbers into negative and vice-versa.
    # If the first character of output is not a "-", put it there.
    if result.get()[0] != '-':
        result.insert(0, '-')
    # Otherwise delete it.
    else:
        current = result.get()[1:]
        result.delete(0, END)
        result.insert(0, current)


def comma():
    # Puts a comma, so the number becomes a float.
    # If there is not a single "." in the number, put it there.
    if '.' not in result.get():
        current = result.get()
        result.delete(0, END)
        result.insert(0, current + '.')


def add():
    # Adds two numbers.
    global number
    global symbol
    first_number = result.get()
    number = float(first_number)
    symbol = '+'
    result.delete(0, END)


def subtract():
    # Subtracts two numbers.
    global number
    global symbol
    first_number = result.get()
    number = float(first_number)
    symbol = '-'
    result.delete(0, END)


def multiply():
    # Multiplies two numbers.
    global number
    global symbol
    first_number = result.get()
    number = float(first_number)
    symbol = '*'
    result.delete(0, END)


def divide():
    # Divides two numbers.
    global number
    global symbol
    first_number = result.get()
    number = float(first_number)
    symbol = '/'
    result.delete(0, END)


def equals():
    """
    Checks the current symbol and performs actions corresponding to the symbol.

    * -> a simple check if the number is an int or a float.
    ** -> the global variable "number" becomes the result of the operation,
    so user can perform operations with the last result.
    """
    global number
    global symbol

    # If the operation is addition
    if symbol == '+':
        answer = number + float(result.get())
        result.delete(0, END)

        # *
        if answer - int(answer) != 0:
            result.insert(0, str(answer))
        else:
            result.insert(0, str(int(answer)))

        # **
        number = answer

    # If the operation is subtraction
    elif symbol == '-':
        answer = number - float(result.get())
        result.delete(0, END)

        # *
        if answer - int(answer) != 0:
            result.insert(0, str(answer))
        else:
            result.insert(0, str(int(answer)))

        # **
        number = answer

    # If the operation is multiplication
    elif symbol == '*':
        answer = number * float(result.get())
        result.delete(0, END)

        # *
        if answer - int(answer) != 0:
            result.insert(0, str(answer))
        else:
            result.insert(0, str(int(answer)))

        # **
        number = answer

    # If the operation is division
    elif symbol == '/':
        answer = number / float(result.get())
        result.delete(0, END)

        # *
        if answer - int(answer) != 0:
            result.insert(0, str(answer))
        else:
            result.insert(0, str(int(answer)))

        # **
        number = answer


# The main window.
root = Tk()
# Setting main window's title.
root.title('Simple calculator')

# The output field that will display the numbers.
result = Entry(root, width=50, borderwidth=5)
result.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Creating all buttons.
button_0 = Button(root, text='0', padx=40, pady=20,
                  command=lambda: result.insert(END, '0'))
button_1 = Button(root, text='1', padx=40, pady=20,
                  command=lambda: result.insert(END, '1'))
button_2 = Button(root, text='2', padx=40, pady=20,
                  command=lambda: result.insert(END, '2'))
button_3 = Button(root, text='3', padx=40, pady=20,
                  command=lambda: result.insert(END, '3'))
button_4 = Button(root, text='4', padx=40, pady=20,
                  command=lambda: result.insert(END, '4'))
button_5 = Button(root, text='5', padx=40, pady=20,
                  command=lambda: result.insert(END, '5'))
button_6 = Button(root, text='6', padx=40, pady=20,
                  command=lambda: result.insert(END, '6'))
button_7 = Button(root, text='7', padx=40, pady=20,
                  command=lambda: result.insert(END, '7'))
button_8 = Button(root, text='8', padx=40, pady=20,
                  command=lambda: result.insert(END, '8'))
button_9 = Button(root, text='9', padx=40, pady=20,
                  command=lambda: result.insert(END, '9'))
button_equals = Button(root, text='=', padx=87, pady=20, command=equals)
button_addition = Button(root, text='+', padx=39, pady=20, command=add)
button_subtraction = Button(root, text='-', padx=40, pady=20, command=subtract)
button_clear = Button(root, text='Clear', padx=75, pady=20, command=clear)
button_plus_minus = Button(root, text='+/-', padx=35, pady=20,
                           command=positive_negative)
button_comma = Button(root, text=',', padx=42, pady=20, command=comma)
button_multiply = Button(root, text='*', padx=40, pady=20, command=multiply)
button_divide = Button(root, text='/', padx=40, pady=20, command=divide)

# Placing buttons in the right positions.
button_0.grid(row=4, column=1)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_equals.grid(row=4, column=3, columnspan=2)
button_addition.grid(row=3, column=3)
button_subtraction.grid(row=2, column=3)
button_clear.grid(row=1, column=3, columnspan=2)
button_plus_minus.grid(row=4, column=0)
button_comma.grid(row=4, column=2)
button_multiply.grid(row=2, column=4)
button_divide.grid(row=3, column=4)

# Starting the program
root.mainloop()
