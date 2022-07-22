import pyautogui
import time
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def spammed():
    label1 = tk.Label(root, text='spamming!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)



def my_bot():
    time.sleep(3)
    f = open("Thelyrics.txt", "r")
    words = []
    for line in f:
        line = line.replace('\n', "")
        words = line.split()
        for word in words:
            for char in word:
                pyautogui.press(char)
            pyautogui.press(' ')
        pyautogui.press('enter')
    f.close()


button1 = tk.Button(text='Click Me to spam the Lyrics', command=spammed and my_bot, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
