from tkinter import *
from tkinter import messagebox as mb
import time
import datetime
import math
def save_text():
    save_text = en.get()
    d = datetime.datetime.now()
    today = '{}.{}.{}:{}'.format(d.month,d.day,d.hour,d.minute)
    with open('memo.txt','a') as f:
        f.write('{} {}\n'.format(today,save_text))
    en.delete(0,END)
    mb.showinfo('info','保存しました')
root = Tk()
root.title('memo')
root.attributes("-topmost", True)
root.geometry("300x100")


    
lb = Label(text='memo')
lb.pack()
en = Entry()
en.pack()

bt_s = Button(text='text_save',command=save_text)
bt_s.pack()
root.mainloop()