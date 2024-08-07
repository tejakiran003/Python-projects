from tkinter import *

root = Tk()
root.title('Calculator')

# Display box
db = Entry(root, width=30, font=('Arial', 24), justify=RIGHT)
db.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Logic
def button_click(num):
    current = db.get()
    db.delete(0, END)
    db.insert(0, current + num)

def clear():
    db.delete(0, END)

def backspace():
    current = db.get()
    db.delete(0, END)
    db.insert(0, current[:-1])

def calc(operator):
    current = db.get()
    db.insert(END, operator)

def equal():
    try:
        result = eval(db.get()) #The eval() function evaluates the string expression currently in the display. For example, if the display shows "2+3*4", eval() will compute this expression and return 14.
        db.delete(0, END)
        db.insert(0, str(round(result, 3)))
    except Exception as e:  #If the eval() function encounters an error (like a malformed expression), it catches the exception and proceeds to the error-handling code.
        db.delete(0, END)
        db.insert(0, "Error")

# Row 1
Button(root, text='%', padx=36, pady=10, font=('Arial', 14), command=lambda: calc('%')).grid(row=1, column=0, padx=10, pady=10)
Button(root, text='/', padx=36, pady=10, font=('Arial', 14), command=lambda: calc('/')).grid(row=1, column=1, padx=10, pady=10)
Button(root, text='C', padx=36, pady=10, font=('Arial', 14), command=clear).grid(row=1, column=2, padx=10, pady=10)
Button(root, text='<-', padx=36, pady=10, font=('Arial', 14), command=backspace).grid(row=1, column=3, padx=10, pady=10)

# Row 2
Button(root, text='7', padx=36, pady=10, font=('Arial', 14), command=lambda: button_click('7')).grid(row=2, column=0, padx=10, pady=10)
Button(root, text='8', padx=36, pady=10, font=('Arial', 14), command=lambda: button_click('8')).grid(row=2, column=1, padx=10, pady=10)
Button(root, text='9', padx=36, pady=10, font=('Arial', 14), command=lambda: button_click('9')).grid(row=2, column=2, padx=10, pady=10)
Button(root, text='*', padx=36, pady=10, font=('Arial', 14), command=lambda: calc('*')).grid(row=2, column=3, padx=10, pady=10)

# Row 3
Button(root, text='4', padx=36, pady=10, font=('Arial', 14), command=lambda: button_click('4')).grid(row=3, column=0, padx=10, pady=10)
Button(root, text='5', padx=36, pady=10, font=('Arial', 14), command=lambda: button_click('5')).grid(row=3, column=1, padx=10, pady=10)
Button(root, text='6', padx=36, pady=10, font=('Arial', 14), command=lambda: button_click('6')).grid(row=3, column=2, padx=10, pady=10)
Button(root, text='-', padx=36, pady=10, font=('Arial', 14), command=lambda: calc('-')).grid(row=3, column=3, padx=10, pady=10)

# Row 4
Button(root, text='1', padx=36, pady=10, font=('Arial', 14), command=lambda: button_click('1')).grid(row=4, column=0, padx=10, pady=10)
Button(root, text='2', padx=36, pady=10, font=('Arial', 14), command=lambda: button_click('2')).grid(row=4, column=1, padx=10, pady=10)
Button(root, text='3', padx=36, pady=10, font=('Arial', 14), command=lambda: button_click('3')).grid(row=4, column=2, padx=10, pady=10)
Button(root, text='+', padx=36, pady=10, font=('Arial', 14), command=lambda: calc('+')).grid(row=4, column=3, padx=10, pady=10)

# Row 5
Button(root, text='x^2', padx=36, pady=10, font=('Arial', 14), command=lambda: calc('**2')).grid(row=5, column=0, padx=10, pady=10)
Button(root, text='0', padx=36, pady=10, font=('Arial', 14), command=lambda: button_click('0')).grid(row=5, column=1, padx=10, pady=10)
Button(root, text='.', padx=36, pady=10, font=('Arial', 14), command=lambda: button_click('.')).grid(row=5, column=2, padx=10, pady=10)
Button(root, text='=', padx=36, pady=10, font=('Arial', 14), command=equal).grid(row=5, column=3, padx=10, pady=10)

# Showing widgets
root.mainloop()
