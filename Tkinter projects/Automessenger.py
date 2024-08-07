from tkinter import *
import pyautogui as pag
import time

def messenger():
    try:
        times = int(input1.get())
        waiting_time = int(input2.get())
        message = input3.get()
        
        print(f"Sending {times} times")
        print(f"Waiting {waiting_time} seconds")
        print(f"Message: {message}")
        
        # Give user time to focus the WhatsApp window
        time.sleep(3)
        
        for x in range(times):
            pag.typewrite(message)
            pag.press('enter') 
            time.sleep(waiting_time)
    except Exception as e:
        print(f"Error: {e}")

# Tkinter GUI setup
root = Tk()
root.title('Auto Messenger')
root.iconbitmap('Tkinter projects/messanger_ico.ico')

# Labels and input fields
label1 = Label(root, text='How many times:')
label1.grid(row=0, column=0, sticky=E)
label1_1 = Label(root, text="times (0 to infinite times)", font=('Arial', 12))
label1_1.grid(row=0, column=1, padx=60, sticky=W)

label2 = Label(root, text="Waiting time:")
label2.grid(row=1, column=0, sticky=E)
label2_1 = Label(root, text="seconds", font=('Arial', 12))
label2_1.grid(row=1, column=1, padx=35, sticky=W)

label3 = Label(root, text="Message:")
label3.grid(row=2, column=0, sticky=E)

input1 = Entry(root, width=5)
input1.grid(row=0, column=1, padx=10, pady=15, sticky=W)
input2 = Entry(root, width=3)
input2.grid(row=1, column=1, padx=10, pady=15, sticky=W)
input3 = Entry(root, width=30)
input3.grid(row=2, column=1, padx=10, pady=15, sticky=W)

button = Button(root, text="Start sending", command=messenger)
button.grid(row=3, column=1)

root.mainloop()

'''import pyautogui
import time
counter = 0
while counter<10:
    time.sleep(3)
    pyautogui.typewrite('test')
    pyautogui.press('enter')
    counter +=1'''
    