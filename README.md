# 🧮 Calculator

A simple, lightweight, and extensible calculator application built with Python.
Supports both desktop and mobile testing environments, with packaging support via PyInstaller.

## 🚀 Features

* Basic arithmetic operations (addition, subtraction, multiplication, division).
* Clean and modular Python code.
* Cross-platform compatibility.
* Ready for packaging into executables (`.exe`, `.app`, etc.) using **PyInstaller**.
* Includes **test script** for mobile-friendly verification.

## 📂 Project Structure

```
.
├── calculator.py        # Main calculator program
├── mobile_test.py       # Test script for mobile devices
├── calculator.spec      # PyInstaller build configuration
├── requirements.txt     # Dependencies
└── tempCodeRunnerFile.py# Temporary run file (ignore)
```

## ⚙️ Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/calculator.git
   cd calculator
   ```

2. Create a virtual environment (recommended):

   ```
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

## ▶️ Usage

Run the calculator:

```
python calculator.py
```

Run mobile test script:

```
python mobile_test.py
```


## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m "Add feature"`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request
