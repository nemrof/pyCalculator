import PySimpleGUI as sg

# TODO: generate UI
# TODO: make more complex functions
# TODO: make history of calculations


# + function
def addition(*argv):
    result = 0
    try:
        for arg in argv:
            result += arg
        return result
    except ValueError:
        print("Enter a number")


# - function
def subtraction(*argv):
    result = 0
    try:
        for arg in argv:
            result -= arg
        return result
    except ValueError:
        print("Enter a number")


# / function
def division(*argv):
    result = 0
    try:
        for arg in argv:
            result /= arg
        return result
    except argv == 0:
        print("Can't divide by 0")
    except ValueError:
        print("Enter a number")


# / function
def multiply(*argv):
    result = 0
    try:
        for arg in argv:
            result *= arg
        return result
    except ValueError:
        print("Enter a number")


# Choose operation:
#print("Type \'1\' to +, \'2\' to -, \'3\' to /, \'4\' to *.")
#option = int(input("Tell me what do you want to do? \n"))

#if option == 1:
#    print("option = 1 - +")
#    while True:
#        result = addition(int(input('Enter values:')))
#        print(f'Sum of given numbers is: {result}.')
#        break


# ------- UI -------
# layout initial settings
# dictionary keys for buttons layout
bn = {'size': (7, 2), 'font': ('Computer Modern', 24), 'button_color': ("black", "#ccf2ff"), 'border_width': '0'}
bf = {'size': (7, 2), 'font': ('Computer Modern', 24), 'button_color': ("black", "#d6f5f5"), 'border_width': '0'}
bs = {'size': (15, 2), 'font': ('Computer Modern', 24), 'button_color': ("black", "#d6f5f5"), 'border_width': '0'}


layout = [
[sg.Text('PyCalculator', size=(50, 1), justification='right', background_color='#ccffff', text_color='black')],
    [sg.Button(button_text="+", **bf), sg.Button(button_text="-", **bf), sg.Button(button_text="/", **bf), sg.Button(button_text="*", **bf)],
    [sg.Button(button_text='7', **bn), sg.Button(button_text='8', **bn), sg.Button(button_text='9', **bn), sg.Button(button_text='C', **bn)],
    [sg.Button(button_text='4', **bn), sg.Button(button_text='5', **bn), sg.Button(button_text='6', **bn), sg.Button(button_text='CE', **bn)],
    [sg.Button(button_text='1', **bn), sg.Button(button_text='2', **bn), sg.Button(button_text='3', **bn), sg.Button(button_text='%', **bn)],
    [sg.Button(button_text='0', **bn), sg.Button(button_text='.', **bn), sg.Button(button_text='=', **bs)],
]

# Create the window
window = sg.Window("Calculator", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
