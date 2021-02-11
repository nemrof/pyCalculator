import PySimpleGUI as sg

# TODO: generate UI
# TODO: make more complex functions
# TODO: make history of calculations

# ------- UI -------
# layout initial settings
file_list_column = [
    [
        sg.Text("Output"),
        #sg.Text("Output")
    ],
    [
        sg.Button(button_text='7'),
        sg.Button(button_text='8'),
        sg.Button(button_text='9')
    ],
    [
        sg.Button(button_text='4'),
        sg.Button(button_text='5'),
        sg.Button(button_text='6')
    ],
    [
        sg.Button(button_text='1'),
        sg.Button(button_text='2'),
        sg.Button(button_text='3')
    ],
]
# For now will only show the name of the file that was chosen
numberFunctions = [
    [sg.Button(button_text="+")],
    [sg.Button(button_text="-")],
    [sg.Button(button_text="/")],
    [sg.Button(button_text="*")],
    #[sg.Text(size=(40, 1), key="-TOUT-")],
    #[sg.Image(key="-IMAGE-")],
]
# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.Column(numberFunctions),
    ]
]


#layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

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
print("Type \'1\' to +, \'2\' to -, \'3\' to /, \'4\' to *.")
option = int(input("Tell me what do you want to do? \n"))

if option == 1:
    print("option = 1 - +")
    while True:
        result = addition(int(input('Enter values:')))
        print(f'Sum of given numbers is: {result}.')
        break
