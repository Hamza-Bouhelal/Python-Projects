from random import randint
from random import randrange
import math
import pandas as pd
import tkinter as tk

def what_smaller_progress(lst):
    j, k, s = -1, -1, 2
    for i in range(len(lst)):
        if s > float(lst[i][2]):
            s = float(lst[i][2])
            j = i
    s = 2
    if len(lst) > 1:
        for i in range(len(lst)):
            if s > float(lst[i][2]) and s != float(lst[j][2]):
                s = float(lst[i][2])
                k = i
        return j, k
    return j

def planner():
    n = int(input(" "))
    lst = []
    for _ in range(n):
        lst.append([])
    for i in range(n):
        mod = input("enter the module name: ")
        lst[i].append(mod)
        date = int(input("enter the date of the exam: "))
        lst[i].append(date)
        progress = float(input("enter your progress in this module: "))
        lst[i].append(progress)
    starting_day = input("Enter the day you're going to start working: ")
    days_until_exam = 9999
    for i in range(len(lst)):
        if lst[i][1] < days_until_exam:
            days_until_exam = lst[i][1]
    days_until_exam -= 8
    lst1 = []
    slot = 0
    reset = 0
    if starting_day == "monday" or starting_day == "thursday":
        i = 0
    if starting_day == "tuesday":
        i = 1
    if starting_day == "wednesday":
        i = 2
    if starting_day == "friday":
        i = 1
        reset = 1
    if starting_day == "saturday":
        i = 2
        reset = 1
    if starting_day == "sunday":
        i = 5
    for _ in range(days_until_exam):
        i += 1
        lst1.append([])
        if i == 1:
            slot += 1
        if i == 2 or i == 3:
            slot += 2
            if i == 3:
                i=0
                reset += 1
        if reset == 2:
            slot += 1
            reset = 0
        if i == 6:
            slot += 1
            i = 0
    temp = 0
    for ele in lst:
        temp += (1-ele[2])
    step_per_slot = temp/slot
    reset = 0
    final_list = []
    weeks = math.floor((days_until_exam/7)+1)
    for _ in range(weeks+1):
        final_list.append([])
    idx, what_day = 0, 0
    if starting_day == "monday":
        i = 0
    if starting_day == "thursday":
        i = 0
        what_day = 1
        final_list[0].append("")
    if starting_day == "tuesday":
        i = 1
        what_day = 2
        final_list[0].append("")
        final_list[0].append("")
    if starting_day == "wednesday":
        i = 2
        what_day = 3
        final_list[0].append("")
        final_list[0].append("")
        final_list[0].append("")
    if starting_day == "friday":
        i = 1
        reset = 1
        what_day = 4
        final_list[0].append("")
        final_list[0].append("")
        final_list[0].append("")
        final_list[0].append("")

    if starting_day == "saturday":
        i = 2
        reset = 1
        what_day = 5
        final_list[0].append("")
        final_list[0].append("")
        final_list[0].append("")
        final_list[0].append("")
        final_list[0].append("")
    if starting_day == "sunday":
        slot += 1
        i = 5
        what_day = 6
        final_list[0].append("")
        final_list[0].append("")
        final_list[0].append("")
        final_list[0].append("")
        final_list[0].append("")
        final_list[0].append("")


    for _ in range(days_until_exam):
        l, m = what_smaller_progress(lst)
        randi = randint(0, 1)
        i += 1
        if i == 1:
            if reset == 0:#monday
                if randi == 1:
                    final_list[idx].append(lst[l][0])
                    lst[l][2] += step_per_slot
                    what_day += 1
                else:
                    final_list[idx].append(lst[m][0])
                    lst[m][2] += step_per_slot
                    what_day += 1
            else: #Thursday
                if randi == 1:
                    final_list[idx].append(lst[l][0])
                    lst[l][2] += step_per_slot
                    what_day += 1
                else:
                    final_list[idx].append(lst[m][0])
                    lst[m][2] += step_per_slot
                    what_day += 1
        if i == 2:
            if reset == 0: # Tuesday
                if l!=m:
                    final_list[idx].append(lst[l][0] + " " + lst[m][0])
                    lst[l][2] += step_per_slot
                    lst[m][2] += step_per_slot
                else:
                    randi2 = randrange(len(lst))
                    final_list[idx].append(lst[l][0] + " " + lst[randi2][0])
                    lst[l][2] += step_per_slot
                    lst[randi2][2] += step_per_slot
                what_day += 1
            else: # friday
                if l != m:
                    final_list[idx].append(lst[l][0] + " " + lst[m][0])
                    lst[l][2] += step_per_slot
                    lst[m][2] += step_per_slot
                else:
                    randi2 = randrange(len(lst))
                    final_list[idx].append(lst[l][0] + " " + lst[randi2][0])
                    lst[l][2] += step_per_slot
                    lst[randi2][2] += step_per_slot
                what_day += 1
        if i == 3:
            if reset == 0: # wednesday
                if l != m:
                    final_list[idx].append(lst[l][0] + " " + lst[m][0])
                    lst[l][2] += step_per_slot
                    lst[m][2] += step_per_slot
                else:
                    randi2 = randrange(len(lst))
                    final_list[idx].append(lst[l][0] + " " + lst[randi2][0])
                    lst[l][2] += step_per_slot
                    lst[randi2][2] += step_per_slot
                what_day += 1
            else:  # saturday
                if l != m:
                    final_list[idx].append(lst[l][0] + " " + lst[m][0])
                    lst[l][2] += step_per_slot
                    lst[m][2] += step_per_slot
                else:
                    randi2 = randrange(len(lst))
                    final_list[idx].append(lst[l][0] + " " + lst[randi2][0])
                    lst[l][2] += step_per_slot
                    lst[randi2][2] += step_per_slot
                what_day += 1
            i = 0
            reset += 1
        if reset ==2: #sunday
            if randi == 1:
                final_list[idx].append(lst[l][0])
                lst[l][2] += step_per_slot
                what_day += 1
            else:
                final_list[idx].append(lst[m][0])
                lst[m][2] += step_per_slot
                what_day += 1
            reset = 0
        if i == 5: #starting from sunday
            if randi == 1:
                final_list[idx].append(lst[l][0])
                lst[l][2] += step_per_slot
            else:
                final_list[idx].append(lst[m][0])
                lst[m][2] += step_per_slot
            what_day += 1
            i = 0
        if what_day == 7:
            what_day = 0
            idx +=1
    if final_list[len(final_list)-1][0] != "":
        while len(final_list[len(final_list)-1])<len(final_list[0]):
            final_list[len(final_list)-1].append("")
    cols = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    df = pd.DataFrame(final_list, columns=cols)
    df.to_excel("Exam_planning.xlsx")






class Window1:
    def __init__(self, window):
        pass

        lbl = tk.Label(window, text="Exam study schedule", font=("Arial Bold", 20))
        lbl.place(x=125, y=0)
        lbl2 = tk.Label(window, text="Enter the number of modules you have:", font=("Arial Bold", 14))
        lbl2.place(x=10, y=60)
        n = tk.Entry(window, width=8)
        n.place(x=100, y=60)
        n.pack()
        btn = tk.Button(window, text="Click Me", command=lambda : button_click(window))
        btn.pack()
        btn.place(x=400, y=60)

def button_click(window):
    pass
    app = Window2(window)



class Window2:
    def __init__(self, window):
        input_token = 0
        module_name = tk.Label(window, text="The module's name")
        module_name.place(x=1, y=0)
        inp_mod_name = tk.Entry(window, width=50)
        inp_mod_name.place(x=1, y=0)
        Nmbre_of_days = tk.Label(window, text="The Number of days: ")
        Nmbre_of_days.place(x=1, y=0)
        inp_nbr_day = tk.Entry(window, width=50)
        inp_nbr_day.place(x=1, y=0)
        Nmbre_of_days = tk.Label(window, text="The Number of days: ")
        Nmbre_of_days.place(x=1, y=0)
        inp_nbr_day = tk.Entry(window, width=50)
        inp_nbr_day.place(x=1, y=0)

    def button_method(self):
        #run this when button click to close window
        self.window.destroy()

def main(): #run mianloop
    window = tk.Tk()
    window.geometry('500x300')
    window.title("Exam schedule")
    global app
    app = Window1(window)
    window.mainloop()

if __name__ == '__main__':
    main()


