from tkinter import *
from tkinter import messagebox as mb
import time
import datetime
import math
def start_timer():
    global day_1 
    day_1 = datetime.datetime.now()
    print('{}:{}'.format(day_1.hour,day_1.minute))
def end_timer():
    day_2 = datetime.datetime.now()
    d = day_2 - day_1
    print('{}:{}'.format(day_2.hour,day_2.minute))
    mb.showinfo('time','作業時間:{}'.format(str(d)))
def timer():
    win = Tk()
    win.title('timer')
    win.minsize(width=250, height=150)
    win.attributes("-topmost", True)

    win.option_add('*Dialog.msg.font', 'Helvetica 12') 

    mylabel = Label(win, text = 'timer',font=('MS　ゴシック',20))
    mylabel.pack()

    startButton = Button(win,text = 'start',width=10,height=0,font=('MS　ゴシック',20),command=start_timer)
    startButton.pack()
    endButton = Button(win,text = 'end',width=10,height=0,font=('MS　ゴシック',20),command=end_timer)
    endButton.pack()

    win.mainloop()
timer()