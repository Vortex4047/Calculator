from tkinter import *

screen = Tk()
screen.title('Calculator')
screen.resizable(False, False)
screen.configure(bg='#17161b')
screen.geometry('570x600+100+200')
expression = ""
equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    try:
        result = str(eval(equation))  # Calculate the result of the expression
        label_result.config(text=result)  # Display result in the label
        equation = result  # Store the result for further calculations
    except:
        label_result.config(text="Error")  # Display error if expression is invalid
        equation = ""  # Reset equation on error

label_result = Label(screen, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

# Clear button
click_me = Button(screen, text='C', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#3697f5', command=clear)
click_me.place(x=10, y=100)

# Other buttons
click_me1 = Button(screen, text='/', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("/"))
click_me1.place(x=150, y=100)
click_me2 = Button(screen, text='%', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("%"))
click_me2.place(x=290, y=100)
click_me5 = Button(screen, text='*', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("*"))
click_me5.place(x=430, y=100)

click_me6 = Button(screen, text='7', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("7"))
click_me6.place(x=10, y=200)
click_me7 = Button(screen, text='8', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("8"))
click_me7.place(x=150, y=200)
click_me8 = Button(screen, text='9', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("9"))
click_me8.place(x=290, y=200)
click_me9 = Button(screen, text='-', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("-"))
click_me9.place(x=430, y=200)

click_me10 = Button(screen, text='4', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("4"))
click_me10.place(x=10, y=300)
click_me11 = Button(screen, text='5', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("5"))
click_me11.place(x=150, y=300)
click_me12 = Button(screen, text='6', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("6"))
click_me12.place(x=290, y=300)
click_me13 = Button(screen, text='+', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("+"))
click_me13.place(x=430, y=300)

click_me14 = Button(screen, text='1', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show("1"))
click_me14.place(x=10, y=400)
click_me15 = Button(screen, text='2', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show("2"))
click_me15.place(x=150, y=400)
click_me16 = Button(screen, text='3', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show("3"))
click_me16.place(x=290, y=400)
click_me17 = Button(screen, text='0', width=11, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show("0"))
click_me17.place(x=10, y=500)

click_me18 = Button(screen, text='.', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show("."))
click_me18.place(x=290, y=500)
click_me19 = Button(screen, text='=', width=5, height=3, font=('arial', 40, 'bold'), bd=1, fg='#fff', bg='#Fe9037', command=calculate)
click_me19.place(x=430, y=400)

screen.mainloop()
