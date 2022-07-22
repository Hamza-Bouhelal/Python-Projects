from tkinter import *
import math
from pynput.keyboard import Listener
import threading

class calculator:
    def __init__(self):
        self.ws = None
        self.tocalculate = "0"
        self.ans = ""

    def addval(self, val):
        if " " not in self.tocalculate:
            if self.tocalculate == "0" and val != ".":
                self.tocalculate = val
            else:
                if val == ".":
                    if '.' not in self.tocalculate:
                        self.tocalculate = self.tocalculate + val
                else:
                    self.tocalculate = self.tocalculate + val
        else:
            if val == '0':
                if self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1] != '0':
                    self.tocalculate = self.tocalculate + val
            elif val == '.':
                if '.' not in self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1]:
                    if self.tocalculate[len(self.tocalculate) - 1] == " ":
                        self.tocalculate = self.tocalculate + "0" + val
                    else:
                        self.tocalculate = self.tocalculate + val
            else:
                self.tocalculate = self.tocalculate + val

    def addop(self, val):
        if val == 'x':
            val = '*'
        if self.tocalculate[len(self.tocalculate) - 1] != " ":
            self.tocalculate += " " + val + " "

    def untype(self):
        if len(self.tocalculate)>1:
            if self.tocalculate[len(self.tocalculate)-1] == " ":
                self.tocalculate = self.tocalculate[0:len(self.tocalculate)-3]
            else:
                if self.tocalculate[len(self.tocalculate)-2] == ".":
                    self.tocalculate = self.tocalculate[0:len(self.tocalculate) - 2]
                else:
                    self.tocalculate = self.tocalculate[0:len(self.tocalculate) - 1]
        else:
            self.tocalculate = "0"

    def c(self):
        self.tocalculate = "0"

    def reverse(self):
        if " " not in self.tocalculate:
            if int(1 / float(self.tocalculate)) == (1 / float(self.tocalculate)):
                self.tocalculate = str(int(1 / float(self.tocalculate)))
            else:
                self.tocalculate = str(round(1 / float(self.tocalculate), 3))
        else:
            if self.tocalculate[len(self.tocalculate) - 1] != " ":
                stri = ""
                for ele in self.tocalculate.split(" "):
                    if ele != self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1]:
                        stri += ele + " "
                if int(1 / float(self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1])) == 1 / float(
                        self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1]):
                    stri += str(int(1 / float(self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1])))
                else:
                    stri += str(round(1 / float(self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1]), 3))
                self.tocalculate = stri

    def raisepower(self):
        if " " not in self.tocalculate:
            if float(self.tocalculate) * float(self.tocalculate) != int(
                    float(self.tocalculate) * float(self.tocalculate)):
                self.tocalculate = str(round(float(self.tocalculate) * float(self.tocalculate), 3))
            else:
                self.tocalculate = str(int(float(self.tocalculate) * float(self.tocalculate)))
        else:
            if self.tocalculate[len(self.tocalculate) - 1] != " ":
                stri = ""
                for ele in self.tocalculate.split(" "):
                    if ele != self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1]:
                        stri += ele + " "

                if int(float(self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1]) * float(
                        self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1])) == float(
                        self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1]) * float(
                        self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1]):
                    stri += str(int(float(self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1]) * float(
                        self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1])))
                else:
                    stri += str(round(float(self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1]) * float(
                        self.tocalculate.split(" ")[len(self.tocalculate.split(" ")) - 1]), 3))
                self.tocalculate = stri

    def negate(self):
        if self.tocalculate[len(self.tocalculate) - 1] != " ":
            if " " in self.tocalculate:
                temp = ""
                for ele in self.tocalculate.split(" "):
                    if ele != self.tocalculate.split(" ")[len(self.tocalculate.split(" "))-1]:
                        temp += ele + " "
                if self.tocalculate.split(" ")[len(self.tocalculate.split(" "))-1].replace('-', ' ') == self.tocalculate.split(" ")[len(self.tocalculate.split(" "))-1]:
                    temp += "-" + self.tocalculate.split(" ")[len(self.tocalculate.split(" "))-1]
                    print("he")
                else:
                    temp += self.tocalculate.split(" ")[len(self.tocalculate.split(" "))-1].replace("-", "")
                    print("he")
                self.tocalculate = temp
            else:
                if self.tocalculate != "0":
                    if self.tocalculate.replace("-", "") == self.tocalculate:
                        self.tocalculate = '-' + self.tocalculate
                    else:
                        self.tocalculate = self.tocalculate.replace('-', "")

    def dosqrt(self):
        if " " not in self.tocalculate:
            if int(math.sqrt(float(self.tocalculate))) == math.sqrt(float(self.tocalculate)):
                self.tocalculate = str(int(math.sqrt(float(self.tocalculate))))
            else:
                self.tocalculate = str(round(math.sqrt(float(self.tocalculate)), 3))
        else:
            if self.tocalculate[len(self.tocalculate)-1] != " ":
                temp = ""
                for ele in self.tocalculate.split(" "):
                    if ele != self.tocalculate.split(" ")[len(self.tocalculate.split(" "))-1]:
                        temp += ele + " "
                    else:
                        last = float(ele)
                if math.sqrt(last) == int(math.sqrt(last)):
                    temp += str(int(math.sqrt(last)))
                else:
                    temp += str(round(math.sqrt(last), 3))
                self.tocalculate = temp

    def returnlast(self):
        if self.ans != "":
            if " " not in self.tocalculate:
                if self.tocalculate == "0":
                    self.tocalculate = str(self.ans)
                else:
                    if self.tocalculate.replace('.', '') == self.tocalculate:
                        self.tocalculate += self.ans
            else:
                if (self.tocalculate.split(" ")[len(self.tocalculate.split(" "))-1].replace(".", '') == self.tocalculate.split(" ")[len(self.tocalculate.split(" "))-1].replace(".", '')) or self.tocalculate[len(self.tocalculate)-1]==" ":
                    if self.tocalculate[len(self.tocalculate)-1] != " ":
                        if self.tocalculate.split(" ")[len(self.tocalculate.split(" "))-1] == '0':
                            self.tocalculate = self.tocalculate[0:len(self.tocalculate)-1] + self.ans
                        else:
                            self.tocalculate += self.ans
                    else:
                        self.tocalculate += self.ans

    def evaluate(self):
        if self.tocalculate.replace("/ 0", '') != self.tocalculate:
            self.tocalculate = "0"
        if self.tocalculate[len(self.tocalculate)-1] == " ":
            self.tocalculate = self.tocalculate[0:len(self.tocalculate)-3]
        self.tocalculate = str(eval(self.tocalculate))
        if self.tocalculate.replace('.', '') != self.tocalculate:
            if float(self.tocalculate) == int(float(self.tocalculate)):
                self.tocalculate = self.tocalculate.split(".")[0] + '.' + self.tocalculate.split(".")[1][0:3]
        self.ans = self.tocalculate

    def on_press(self, key):
        if self.ws.focus_displayof():
            if 'char' in list(key.__dict__.keys()):
                print(key.char)
                if key.char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']:
                    self.addval(key.char)
                elif key.char == '*' or key.char == '+' or key.char == '-' or key.char == '/' or key.char == '%':
                    self.addop(key.char)
                elif key.char == '=':
                    self.evaluate()
            elif 'name' in list(key.__dict__.keys()):
                print(key.name)
                if key.name == 'enter':
                    self.evaluate()
        self.lab1.config(text=self.tocalculate)
    def listen(self):
        with Listener(
                on_press=self.on_press,
                ) as listener:
            listener.join()

    def showcal(self):
        newtread = threading.Thread(target=self.listen, daemon=True)
        newtread.start()
        self.ws = Tk()
        self.ws.title("Calculator")
        self.ws.geometry('320x270')
        self.ws.resizable(0, 0)
        f = ('Times', 14)
        f2 = ('Bombshell Pro', 22)
        f3 = ('Bombshell Pro', 3)
        Label(
            self.ws,
            text=" ",
            font=f3).grid(row=0, column=0)
        lab = Label(
            self.ws,
            text=self.tocalculate,
            font=f2)
        lab.grid(row=1, column=0)
        self.lab1 = lab
        Label(
            self.ws,
            text=" ",
            font=f3)
        lab.grid(row=2, column=0)
        Label(
            self.ws,
            text=" ",
            font=f3)
        lab.grid(row=2, column=0)
        left_frame = Frame(
            self.ws,
            bd=0,
            bg='#CCCCCC',
        )
        Button(
            left_frame,
            width=7,
            text='SQRT',
            font=f,
            relief=SOLID,
            command=lambda: [self.dosqrt(), lab.config(text=self.tocalculate)],
            cursor='hand2',
        ).grid(row=2, column=0, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='%',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=lambda: [self.addop('%'), lab.config(text=self.tocalculate)],
        ).grid(row=2, column=1, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='C',
            relief=SOLID,
            font=f,
            cursor='hand2',
            command=lambda: [self.c(), lab.config(text=self.tocalculate)],
        ).grid(row=2, column=2, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='DEL',
            font=f,
            cursor='hand2',
            command=lambda: [self.untype(), lab.config(text=self.tocalculate)],
            relief=SOLID,
        ).grid(row=2, column=3, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='1/x',
            font=f,
            cursor='hand2',
            command=lambda: [self.reverse(), lab.config(text=self.tocalculate)],
            relief=SOLID,
        ).grid(row=3, column=0, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='x²',
            font=f,
            cursor='hand2',
            command=lambda: [self.raisepower(), lab.config(text=self.tocalculate)],
            relief=SOLID,
        ).grid(row=3, column=1, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='+/-',
            font=f,
            cursor='hand2',
            relief=SOLID,
            command=lambda: [self.negate(), lab.config(text=self.tocalculate)],
        ).grid(row=3, column=2, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='/',
            font=f,
            cursor='hand2',
            relief=SOLID,
            command=lambda: [self.addop('/'), lab.config(text=self.tocalculate)],
        ).grid(row=3, column=3, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='7',
            font=f,
            command=lambda: [self.addval('7'), lab.config(text=self.tocalculate)],
            cursor='hand2',
        ).grid(row=4, column=0, pady=0, padx=0)
        Button(
            left_frame,
            command=lambda: [self.addval('8'), lab.config(text=self.tocalculate)],
            width=7,
            text='8',
            font=f,
            cursor='hand2',
        ).grid(row=4, column=1, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='9',
            font=f,
            command=lambda: [self.addval('9'), lab.config(text=self.tocalculate)],
            cursor='hand2',
        ).grid(row=4, column=2, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='x',
            relief=SOLID,
            font=f,
            cursor='hand2',
            command=lambda: [self.addop('x'), lab.config(text=self.tocalculate)],
        ).grid(row=4, column=3, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='4',
            font=f,
            command=lambda: [self.addval('4'), lab.config(text=self.tocalculate)],
            cursor='hand2',
        ).grid(row=5, column=0, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='5',
            command=lambda: [self.addval('5'), lab.config(text=self.tocalculate)],
            font=f,
            cursor='hand2',
        ).grid(row=5, column=1, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='6',
            font=f,
            command=lambda: [self.addval('6'), lab.config(text=self.tocalculate)],
            cursor='hand2',
        ).grid(row=5, column=2, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='-',
            font=f,
            relief=SOLID,
            command=lambda: [self.addop('-'), lab.config(text=self.tocalculate)],
            cursor='hand2',
        ).grid(row=5, column=3, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='1',
            font=f,
            cursor='hand2',
            command=lambda: [self.addval('1'), lab.config(text=self.tocalculate)],
        ).grid(row=6, column=0, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='2',
            command=lambda: [self.addval('2'), lab.config(text=self.tocalculate)],
            font=f,

            cursor='hand2',
        ).grid(row=6, column=1, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='3',
            font=f,
            command=lambda: [self.addval('3'), lab.config(text=self.tocalculate)],
            cursor='hand2',
        ).grid(row=6, column=2, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='+',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=lambda: [self.addop('+'), lab.config(text=self.tocalculate)],
        ).grid(row=6, column=3, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='ANS',
            font=f,
            cursor='hand2',
            command=lambda: [self.returnlast(), lab.config(text=self.tocalculate)],
        ).grid(row=7, column=0, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='0',
            font=f,
            command=lambda: [self.addval('0'), lab.config(text=self.tocalculate)],
            cursor='hand2',
        ).grid(row=7, column=1, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text=',',
            font=f,
            cursor='hand2',
            command=lambda: [self.addval('.'), lab.config(text=self.tocalculate)],
        ).grid(row=7, column=2, pady=0, padx=0)
        Button(
            left_frame,
            width=7,
            text='=',
            relief=SOLID,
            font=f,
            command=lambda: [self.evaluate(), lab.config(text=self.tocalculate)],
            cursor='hand2',
        ).grid(row=7, column=3, pady=0, padx=0)
        left_frame.grid(row=3, column=0, pady=0, padx=0)
        self.ws.mainloop()


p = calculator()
p.showcal()
