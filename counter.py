from tkinter import *
from tkinter import messagebox as mb
import time
import datetime
import math
def counter():
    i = int(text.get())
    i += 1
    text.delete(0,END)
    text.insert(0,i)
    
def reseter():
    text.delete(0,END)
    text.insert(0,'0')

def total_count():
    global total
    i = int(text.get())
    total += i
    text.delete(0,END)
    text.insert(0,'0')
    text_2.delete(0,END)
    text_2.insert(0,total)

def total_reset():
    global total
    total = 0
    text_2.delete(0,END)
    text_2.insert(0,total)

win = Tk()
win.title('counter')
win.minsize(width=250, height=300)
win.attributes("-topmost", True)
win.geometry("200x200")
mylabel = Label(win, text = 'counter',font=('MS　ゴシック',20))
mylabel.pack()

total = 0

text = Entry(win,font=('MS　ゴシック',20))
text.pack()
text.insert(0,'0')
text_2 = Entry(win,font=('MS　ゴシック',20))
text_2.pack()
text_2.insert(0,'0')

countButton = Button(win,text = 'count',command=counter,width=10,height=0,font=('MS　ゴシック',20))
countButton.pack(side='top')
resetButton = Button(win,text = 'reset',command=reseter,width=10,height=0,font=('MS　ゴシック',20))
resetButton.pack(side='top')
totalButton = Button(win,text = 'total',command=total_count,width=10,height=0,font=('MS　ゴシック',20))
totalButton.pack(side='top')
total_resetButton = Button(win,text = 'total reset',command=total_reset,width=10,height=0,font=('MS　ゴシック',20))
total_resetButton.pack(side='top')



win.mainloop()