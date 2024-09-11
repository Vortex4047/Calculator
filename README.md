# Basic-Calculator
This Python code creates a fully functional graphical calculator using the Tkinter library. Let’s go through it in detail to understand how it works, including the different parts of the code and the functions they perform.

### 1. **Importing Tkinter**
```python
from tkinter import *
```
This imports all classes and functions from the Tkinter library, which is used to create the GUI (graphical user interface) of the calculator.

### 2. **Creating the Main Window**
```python
screen = Tk()
screen.title('Calculator')
screen.resizable(False, False)
screen.configure(bg='#17161b')
screen.geometry('570x600+100+200')
```
- `screen = Tk()` initializes the main window for the application.
- `screen.title('Calculator')` sets the title of the window.
- `screen.resizable(False, False)` prevents the window from being resized.
- `screen.configure(bg='#17161b')` sets the background color of the window.
- `screen.geometry('570x600+100+200')` defines the size of the window as 570 pixels wide and 600 pixels tall, and places the window at position `(100, 200)` on the screen.

### 3. **Variables for Storing the Input and Expression**
```python
expression = ""
equation = ""
```
These variables hold the mathematical expression entered by the user:
- `expression` stores the current button inputs.
- `equation` holds the full mathematical expression to be evaluated.

### 4. **Function to Display the Input (`show()`)**
```python
def show(value):
    global equation
    equation += value
    label_result.config(text=equation)
```
- This function takes the button value as input (e.g., numbers or operators).
- `global equation` allows the function to modify the `equation` variable.
- `equation += value` adds the clicked button’s value to the current equation.
- `label_result.config(text=equation)` updates the display label to show the current input.

### 5. **Function to Clear the Display (`clear()`)**
```python
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)
```
- Clears the `equation` by resetting it to an empty string.
- Updates the display by setting the label to an empty string.

### 6. **Function to Calculate the Result (`calculate()`)**
```python
def calculate():
    global equation
    try:
        result = str(eval(equation))
        label_result.config(text=result)
        equation = result
    except:
        label_result.config(text="Error")
        equation = ""
```
- `calculate()` evaluates the mathematical expression stored in `equation`.
- `eval(equation)` calculates the result of the expression. It converts the string `equation` into an actual math operation.
- The result is converted into a string and displayed on the label using `label_result.config(text=result)`.
- If an invalid expression is encountered, the `except` block displays an error message and resets the `equation`.

### 7. **Result Display (`label_result`)**
```python
label_result = Label(screen, width=25, height=2, text="", font=("arial", 30))
label_result.pack()
```
- This creates a label that will show the current input and result.
- `width=25` and `height=2` set the size of the label.
- The font is set to Arial with a size of 30.
- `label_result.pack()` positions the label at the top of the window.

### 8. **Button Creation**
Each button on the calculator is created using the `Button()` widget. Let’s look at one as an example:
```python
click_me = Button(screen, text='C', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#3697f5', command=clear)
click_me.place(x=10, y=100)
```
- **`Button()`** creates a button with the following attributes:
  - `screen`: The parent window where the button is placed.
  - `text='C'`: The text displayed on the button.
  - `width=5, height=1`: The size of the button.
  - `font=('arial', 30, 'bold')`: Font style and size.
  - `fg='#fff'`: Text color (white).
  - `bg='#3697f5'`: Background color (blue).
  - `command=clear`: The function that will be called when the button is clicked (in this case, `clear()`).
- `place(x=10, y=100)` positions the button on the screen.

### 9. **Lambda Functions for Passing Arguments**
For most buttons, `lambda` is used to pass arguments (like numbers or operators) to the `show()` function:
```python
click_me1 = Button(screen, text='/', width=5, height=1, font=('arial', 30, 'bold'), fg='#fff', bg='#2a2d36', command=lambda: show("/"))
click_me1.place(x=150, y=100)
```
Here, the `command=lambda: show("/")` ensures that when the division button is clicked, the `show()` function is called with the argument `/`.

### 10. **Placing Buttons**
All buttons are placed at specific `x` and `y` coordinates on the window using the `place()` method. Each button represents a digit, operator, or function (`C`, `=`, etc.) on the calculator.

For example:
- `click_me7.place(x=150, y=200)` places the '8' button at coordinates `(150, 200)`.

### 11. **Main Event Loop**
```python
screen.mainloop()
```
This starts the Tkinter event loop, which listens for user interaction (like button clicks) and keeps the application running.

---

### **Summary of Functionality:**
- The calculator GUI is created with Tkinter.
- The buttons for digits (0-9), operators (`+`, `-`, `*`, `/`), and special functions (`C` for clear, `=` for calculation) are placed on the window.
- When a button is clicked, the corresponding value is displayed in the label.
- When the `=` button is pressed, the expression is evaluated, and the result is displayed.
- Errors (like dividing by zero or invalid input) are caught and displayed as "Error."

This code provides a simple but functional calculator that can handle basic arithmetic operations.
