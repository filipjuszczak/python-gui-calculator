"""
A very simple GUI calculator using Tkinker.

The calculator features:
    - addition
    - subtraction
    - multiplication
    - division
    - square root of a number
    - number to the power of 2
    - 1 over number -> 1/3 = 0.(3)
    - percentages
    - memory
    - history
"""

# Required import.
from tkinter import *
import math

# Global variables.
number = None
symbol = None
memory = None


def positive_negative():
    """
    Converts positive numbers into negative and vice-versa.
    :return: None
    """

    # If the first character of output is not a "-", put it there.
    if result.get()[0] != '-':
        result.insert(0, '-')
    # Otherwise delete it.
    else:
        current = result.get()[1:]
        result.delete(0, END)
        result.insert(0, current)


def comma():
    """
    Puts a comma, so the number becomes a float.
    :return: None
    """

    # If there is not a single "." in the number, put it there.
    if '.' not in result.get():
        current = result.get()
        result.delete(0, END)
        result.insert(0, current + '.')


def add():
    """
    Adds two numbers.
    :return: None
    """

    global number
    global symbol

    first_number = result.get()
    number = float(first_number)
    symbol = '+'
    result.delete(0, END)


def subtract():
    """
    Subtracts two numbers.
    :return: None
    """

    global number
    global symbol

    first_number = result.get()
    number = float(first_number)
    symbol = '-'
    result.delete(0, END)


def multiply():
    """
    Multiplies two numbers.
    :return: None
    """

    global number
    global symbol

    first_number = result.get()
    number = float(first_number)
    symbol = '*'
    result.delete(0, END)


def divide():
    """
    Divides the first number by the second.
    :return: None
    """

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
    global result
    global history_output

    # If the second number was not input, print just the first one.
    if result.get() == '':
        result.insert(0, int(number))

    # If the operation is addition.
    elif symbol == '+':
        read_number = float(result.get())
        answer = number + read_number
        result.delete(0, END)

        # *
        if answer - int(answer) != 0:
            result.insert(0, str(answer))
        else:
            result.insert(0, str(int(answer)))

        history_text = history_output['text']
        history_text += '{0} + {1} = {2}\n'.format(number, read_number, answer)
        history_output = Label(root, width=25, height=25, borderwidth=5,
                               relief='groove',
                               text=history_text)
        history_output.grid(row=1, column=5, padx=(0, 8), rowspan=7)

        # **
        number = answer

    # If the operation is subtraction.
    elif symbol == '-':
        read_number = float(result.get())
        answer = number - read_number
        result.delete(0, END)

        # *
        if answer - int(answer) != 0:
            result.insert(0, str(answer))
        else:
            result.insert(0, str(int(answer)))

        history_text = history_output['text']
        history_text += '{0} - {1} = {2}\n'.format(number, read_number, answer)
        history_output = Label(root, width=25, height=25, borderwidth=5,
                               relief='groove',
                               text=history_text)
        history_output.grid(row=1, column=5, padx=(0, 8), rowspan=7)

        # **
        number = answer

    # If the operation is multiplication.
    elif symbol == '*':
        read_number = float(result.get())
        answer = number * read_number
        result.delete(0, END)

        # *
        if answer - int(answer) != 0:
            result.insert(0, str(answer))
        else:
            result.insert(0, str(int(answer)))

        history_text = history_output['text']
        history_text += '{0} * {1} = {2}\n'.format(number, read_number, answer)
        history_output = Label(root, width=25, height=25, borderwidth=5,
                               relief='groove',
                               text=history_text)
        history_output.grid(row=1, column=5, padx=(0, 8), rowspan=7)

        # **
        number = answer

    # If the operation is division.
    elif symbol == '/':
        read_number = float(result.get())
        answer = number / read_number
        result.delete(0, END)

        # *
        if answer - int(answer) != 0:
            result.insert(0, str(answer))
        else:
            result.insert(0, str(int(answer)))

        history_text = history_output['text']
        history_text += '{0} / {1} = {2}\n'.format(number, read_number, answer)
        history_output = Label(root, width=25, height=25, borderwidth=5,
                               relief='groove',
                               text=history_text)
        history_output.grid(row=1, column=5, padx=(0, 8), rowspan=7)

        # **
        number = answer


def memory_clear():
    """
    Clears the memory.
    :return: None
    """

    global memory

    memory = None


def memory_recall():
    """
    Clears the input and puts in a number which is currently in the memory.
    :return: None
    """

    global memory
    global result

    if memory is not None:
        result.delete(0, END)
        result.insert(0, memory)


def memory_add():
    """
    Sets the memory variable to whatever is in the input field at the moment
    or adds the number in the current input field to the existing memory.
    :return: None
    """

    global memory

    if memory is None:
        memory = float(result.get())
    else:
        memory += float(result.get())


def memory_subtract():
    """
    Subtracts the number in the current input field from the existing memory.
    :return: None
    """

    global memory

    if memory is not None:
        memory -= float(result.get())


def percent():
    """
    Reads the current number from input field and converts it to a percent.
    :return: None
    """

    global result

    current = result.get()
    to_work = float(current) / 100
    result.delete(0, END)
    result.insert(0, to_work)


def ce():
    """
    Clears the input field and history.
    :return: None
    """

    global result
    global history_output
    global number

    number = None

    result.delete(0, END)
    history_output.destroy()
    history_output = Label(root, width=25, height=25, borderwidth=5,
                           relief='groove',
                           text='')
    history_output.grid(row=1, column=5, padx=(0, 8), rowspan=7)


def c():
    """
    Clears the input field and history.
    :return: None
    """

    global result
    global history_output
    global number

    number = None

    result.delete(0, END)
    history_output.destroy()
    history_output = Label(root, width=25, height=25, borderwidth=5,
                           relief='groove',
                           text='')
    history_output.grid(row=1, column=5, padx=(0, 8), rowspan=7)


def delete():
    """
    Deletes the last input character.
    :return: None
    """

    global result

    current = result.get()

    if len(current) == 1:
        to_print = ''

    elif current[-2] == '.':
        to_print = current[:-2]
    else:
        to_print = current[:-1]

    result.delete(0, END)
    result.insert(0, to_print)


def one_over():
    """
    Reads the current number from input field and calculates 1 / x, where x
    is the read number.
    :return: None
    """

    global result
    current = result.get()
    to_print = 1 / float(current)
    result.delete(0, END)
    result.insert(0, to_print)


def x_squared():
    """
    Reads the current number from input field and calculates x to the power
    of 2, where x is the read number.
    :return: None
    """

    global result
    current = result.get()
    to_print = math.pow(current, 2)
    result.delete(0, END)
    result.insert(0, to_print)


def sqrt_x():
    """
    Reads the current number from input field and calculates a square root
    of x, where x is the read number.
    :return:
    """

    global result
    current = result.get()
    to_print = math.sqrt(float(current))
    result.delete(0, END)
    result.insert(0, to_print)


# The main window.
root = Tk()
# Setting main window's title.
root.title('Calculator')

# The output field that will display numbers.
result = Entry(root, width=50, borderwidth=5, justify='right')
result.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# History label.
history = Label(root, width=25, borderwidth=5, relief='groove', text='History')
history.grid(row=0, column=5, padx=(0, 10))

# The output field that will display calculator history.
history_output = Label(root, width=25, height=25, borderwidth=5,
                       relief='groove',
                       text='')
history_output.grid(row=1, column=5, padx=(0, 8), rowspan=7)

# Creating all buttons.
button_memory_clear = Button(root, text='MC', padx=33, pady=5,
                             command=memory_clear)
button_memory_recall = Button(root, text='MR', padx=34, pady=5,
                              command=memory_recall)
button_memory_add = Button(root, text='M+', padx=34, pady=5,
                           command=memory_add)
button_memory_subtract = Button(root, text='M-', padx=34, pady=5,
                                command=memory_subtract)
button_percent = Button(root, text='%', padx=38, pady=20, command=percent)
button_ce = Button(root, text='CE', padx=36, pady=20, command=ce)
button_c = Button(root, text='C', padx=39, pady=20, command=c)
button_delete = Button(root, text='<<', padx=36, pady=20, command=delete)
button_one_over_x = Button(root, text='1/x', padx=35, pady=20,
                           command=one_over)
button_x_squared = Button(root, text='x^2', padx=32, pady=20,
                          command=x_squared)
button_sqrt_x = Button(root, text='√x', padx=36, pady=20, command=sqrt_x)
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
button_equals = Button(root, text='=', padx=40, pady=20, command=equals)
button_addition = Button(root, text='+', padx=40, pady=20, command=add)
button_subtraction = Button(root, text='-', padx=41, pady=20, command=subtract)
button_plus_minus = Button(root, text='+/-', padx=35, pady=20,
                           command=positive_negative)
button_comma = Button(root, text=',', padx=42, pady=20, command=comma)
button_multiply = Button(root, text='X', padx=40, pady=20, command=multiply)
button_divide = Button(root, text='/', padx=42, pady=20, command=divide)

# Placing buttons in the right positions.
result.grid(row=0, column=0, columnspan=4)
button_memory_clear.grid(row=1, column=0)
button_memory_recall.grid(row=1, column=1)
button_memory_add.grid(row=1, column=2)
button_memory_subtract.grid(row=1, column=3)
button_percent.grid(row=2, column=0)
button_ce.grid(row=2, column=1)
button_c.grid(row=2, column=2)
button_delete.grid(row=2, column=3)
button_one_over_x.grid(row=3, column=0)
button_x_squared.grid(row=3, column=1)
button_sqrt_x.grid(row=3, column=2)
button_divide.grid(row=3, column=3)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
button_plus_minus.grid(row=7, column=0)
button_0.grid(row=7, column=1)
button_comma.grid(row=7, column=2)
button_multiply.grid(row=4, column=3)
button_subtraction.grid(row=5, column=3)
button_addition.grid(row=6, column=3)
button_equals.grid(row=7, column=3)

# Starting the program
root.mainloop()
