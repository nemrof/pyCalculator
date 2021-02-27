from tkinter import *
import math
import re


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title('Simple Calculator')
        master.iconbitmap('calculator-icon.ico')

        # define color schemes
        light_blue = '#edf2fb'
        med_blue = '#d6f4ff'
        dark_blue = '#61a5c2'
        cus_blue = '#99e4ff'
        an_blue = '#d3d5d9'

        # Text widget -- output
        self.screen = Text(master, background=light_blue, font=('Helvetica', 32), height=1, state='disabled',
                           foreground='black', bd=0, pady=50, padx=5, selectbackground=dark_blue,
                           inactiveselectbackground='white')

        # set up initial geometry
        for x in range(1, 6):
            self.master.columnconfigure(x, weight=1)
            self.master.rowconfigure(x, weight=1)

        # text widget setup
        self.screen.grid(row=0, column=0, columnspan=5, sticky=W+E+N+S)
        self.screen.configure(state='normal')
        self.equation = ''
        # default size
        self.master.geometry('500x600')
        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"\u00F7", bg=an_blue)
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00D7", bg=an_blue)
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('-', bg=an_blue)
        b13 = self.createButton('.')
        b14 = self.createButton(0)
        b15 = self.createButton(None)
        b16 = self.createButton('+', bg=an_blue)
        b17 = self.createButton('DEL', None, bg=med_blue)
        b18 = self.createButton('CE', None, bg=med_blue)
        b19 = self.createButton('=', None, bg=cus_blue)
        b20 = self.createButton(u"\u221A", bg=an_blue)   # sqr root
        b21 = self.createButton(u"\u221B", bg=an_blue)   # cube root
        b22 = self.createButton('x\u00B2', bg=an_blue)   # pwr 2
        b23 = self.createButton('x\u00B3', bg=an_blue)   # pwr 3
        b15.config(state='disabled') # blank space
        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23]

        count = 0
        for row in range(1, 5):
            for col in range(4):
                buttons[count].grid(row=row+1, column=col, sticky=W+E+N+S)
                count += 1
        buttons[16].grid(row=1, column=4, rowspan=1, sticky=W+E+N+S)
        buttons[17].grid(row=2, column=4, rowspan=2, sticky=W+E+N+S)
        buttons[18].grid(row=4, column=4, rowspan=2, sticky=W+E+N+S)
        buttons[19].grid(row=1, column=0, rowspan=1, sticky=W+E+N+S)
        buttons[20].grid(row=1, column=1, rowspan=1, sticky=W+E+N+S)
        buttons[21].grid(row=1, column=2, rowspan=1, sticky=W+E+N+S)
        buttons[22].grid(row=1, column=3, rowspan=1, sticky=W+E+N+S)


    def createButton(self, val, write=True, width=5, bg='#F0eff4'):
        return Button(self.master, text=val, command=lambda: self.click(val,write), width=width, bg=bg, bd=0,
                      fg='black', font=('Helvetica', 24))
        # wciskając inny kolor ->  , activebackground='#61a5c2')

    # buttons functionality
    def click(self, text, write):
        if write == None:
            if text == '=' and self.equation:
                # Take unicode sign and change it to math expression
                self.equation = re.sub(u'\u00F7', '/', self.equation)     # /
                self.equation = re.sub(u'\u00D7', '*', self.equation)     # *
                self.equation = re.sub('\u00B2', '**2', self.equation)   # power of 2
                self.equation = re.sub('\u00B3', '**3', self.equation)   # power of 3
                # Sqr root  ---  check if before sqr root is a number
                if re.findall('(\d+)\u221A(\d+)', self.equation):
                    sqr = re.findall('\u221A(\d+)', self.equation)
                    self.equation = re.sub('\u221A\d+', f'*math.sqrt({sqr[0]})', self.equation)
                elif re.findall('\u221A(\d+)', self.equation):
                    sqr = re.findall('\u221A(\d+)', self.equation)
                    self.equation = re.sub('\u221A\d+', f'math.sqrt({sqr[0]})', self.equation)
                # cubic root  --- check if before is a number
                if re.findall('(\d+)\u221B(\d+)', self.equation):
                    cbr = re.findall('\u221B(\d+)', self.equation)
                    self.equation = re.sub('\u221B\d+', f'*({cbr[0]}**(1/3))', self.equation)
                elif re.findall('\u221B(\d+)', self.equation):
                    cbr = re.findall('\u221B(\d+)', self.equation)
                    self.equation = re.sub('\u221B\d+', f'{cbr[0]}**(1/3)', self.equation)
                print(self.equation)

                # eval the input from txt widget
                try:
                    answer = str(eval(self.equation))
                except ZeroDivisionError:
                    answer = 'Error'
                self.clear_screen()
                self.insert_screen(answer, newline=True)
            elif text == 'CE':
                self.clear_screen()
            elif text == 'DEL':
                self.del_screen()
        else:
            # insert text to output widget
            self.insert_screen(text)


    # clear screen button
    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete(1.0, END)
        self.screen.configure(state='disabled')


    # del button
    def del_screen(self):
        self.equation = self.equation[:-1]
        self.screen.configure(state='normal')
        text = self.screen.get('1.0', END)[:-2]
        self.screen.tag_config('val', justify=RIGHT)
        self.screen.delete(1.0,END)
        self.screen.insert(END, text, 'val')
        self.screen.configure(state='disabled')

    # insert screen
    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.tag_config('val', justify=RIGHT)
        # change the output x^2, x^3 to ^2 ^3
        if re.findall('x\u00B2', str(value)):
            value = re.sub('x\u00B2', '\u00B2', str(value))
            self.screen.insert(END, str(value), 'val')
        elif re.findall('x\u00B3', str(value)):
            value = re.sub('x\u00B3', '\u00B3', str(value))
            self.screen.insert(END, str(value), 'val')
        else:
            self.screen.insert(END, str(value), 'val')
        # equation records every value
        self.equation += str(value)
        self.screen.configure(state='disabled')


root = Tk()
my_gui = Calculator(root)
root.mainloop()
