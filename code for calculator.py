from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title('Calculator')
screen.configure(bg='#17161b')
screen.resizable(True, True)

expression = ""
history_log = []
dark_mode = True
sound_on = True
fullscreen = False

# -------------------- FUNCTIONS --------------------
def show(value):
    global expression
    expression += value
    label_result.config(text=expression)
    if sound_on: screen.bell()

def clear():
    global expression
    expression = ""
    label_result.config(text="")

def clear_all():
    global expression, history_log
    expression = ""
    history_log.clear()
    label_result.config(text="")

def backspace():
    global expression
    expression = expression[:-1]
    label_result.config(text=expression)
    if sound_on: screen.bell()

def calculate():
    global expression, history_log
    try:
        result = str(eval(expression))
        history_log.append(expression + " = " + result)
        label_result.config(text=result)
        expression = result
    except:
        label_result.config(text="Error")
        expression = ""

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def toggle_sound():
    global sound_on
    sound_on = not sound_on
    messagebox.showinfo("Sound", f"Sound turned {'ON' if sound_on else 'OFF'}")

def show_history():
    if history_log:
        messagebox.showinfo("History", "\n".join(history_log[-5:]))
    else:
        messagebox.showinfo("History", "No history yet.")

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    screen.attributes('-fullscreen', fullscreen)

def exit_app():
    screen.destroy()

def key_press(event):
    key = event.keysym

    if key in ('Return', 'equal'):
        calculate()
    elif key in ('BackSpace',):
        backspace()
    elif key in ('Escape',):
        exit_app()
    elif key.lower() == 'c':
        clear()
    elif key in ('plus', 'KP_Add'):
        show('+')
    elif key in ('minus', 'KP_Subtract'):
        show('-')
    elif key in ('asterisk', 'KP_Multiply'):
        show('*')
    elif key in ('slash', 'KP_Divide'):
        show('/')
    elif key == 'percent':
        show('%')
    elif key == 'period':
        show('.')
    elif key.isdigit():
        show(key)
    elif key in ('parenleft', 'parenright'):
        show('(' if key == 'parenleft' else ')')

def apply_theme():
    bg = '#17161b' if dark_mode else '#f0f0f0'
    fg = '#ffffff' if dark_mode else '#000000'
    special_bg = '#3697f5' if dark_mode else '#007fff'
    equal_bg = '#fe9037' if dark_mode else '#ff9933'
    entry_bg = '#222222' if dark_mode else '#ffffff'

    screen.configure(bg=bg)
    label_result.config(bg=entry_bg, fg=fg)

    for btn, symbol in zip(buttons, button_symbols):
        btext = symbol[0]
        if btext == 'C':
            btn.config(bg=special_bg, fg='white')
        elif btext == '=':
            btn.config(bg=equal_bg, fg='white')
        else:
            btn.config(bg='#2a2d36' if dark_mode else '#d0d0d0', fg=fg)

# -------------------- UI SETUP --------------------
label_result = Label(screen, text="", anchor='e', font=("Arial", 40), height=2, bg="#222222", fg="white")
label_result.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

button_symbols = [
    ('C', 1, 0, clear, 1), ('⌫', 1, 1, backspace, 1), ('%', 1, 2, lambda: show('%'), 1), ('/', 1, 3, lambda: show('/'), 1),
    ('7', 2, 0, lambda: show('7'), 1), ('8', 2, 1, lambda: show('8'), 1), ('9', 2, 2, lambda: show('9'), 1), ('*', 2, 3, lambda: show('*'), 1),
    ('4', 3, 0, lambda: show('4'), 1), ('5', 3, 1, lambda: show('5'), 1), ('6', 3, 2, lambda: show('6'), 1), ('-', 3, 3, lambda: show('-'), 1),
    ('1', 4, 0, lambda: show('1'), 1), ('2', 4, 1, lambda: show('2'), 1), ('3', 4, 2, lambda: show('3'), 1), ('+', 4, 3, lambda: show('+'), 1),
    ('0', 5, 0, lambda: show('0'), 2), ('.', 5, 2, lambda: show('.'), 1), ('=', 5, 3, calculate, 1),
    ('Theme', 6, 0, toggle_theme, 2), ('Exit', 6, 2, exit_app, 2),
    ('History', 7, 0, show_history, 1), ('Sound', 7, 1, toggle_sound, 1), ('Clear All', 7, 2, clear_all, 1), ('Fullscreen', 7, 3, toggle_fullscreen, 1),
]

buttons = []
for (text, row, col, cmd, colspan) in button_symbols:
    btn = Button(screen, text=text, command=cmd, font=('Arial', 22), bd=0)
    btn.grid(row=row, column=col, columnspan=colspan, sticky='nsew', padx=4, pady=4)
    buttons.append(btn)

for i in range(8):
    screen.grid_rowconfigure(i, weight=1)
for i in range(4):
    screen.grid_columnconfigure(i, weight=1)

# -------------------- BIND KEYS --------------------
screen.bind("<Key>", key_press)

apply_theme()
screen.mainloop()
# -------------------- END OF FILE --------------------
# This is the end of the calculator.py file. It contains a simple GUI calculator with basic arithmetic operations, history, sound toggle, theme toggle, and fullscreen mode. The calculator supports keyboard input and has a responsive design.
# The code is structured to allow easy modifications and enhancements in the future.
