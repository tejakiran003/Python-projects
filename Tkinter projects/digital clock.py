from tkinter import *
from time import strftime

root=Tk()
root.title('Digital Clock')
root.geometry('630x135')
root.minsize(465,130)
root.maxsize(465,130)
root.config(bg='black')

def time():
    cur_time = strftime('%I:%M:%S %p')
    clock_label.config(text=cur_time)
    root.after(1000, time)

clock_label = Label(root,text='Digital clock',font=('Mistral',80),bg='black',fg='#03fc3d',padx=5,pady=5)
clock_label.pack()
time()
root.mainloop()