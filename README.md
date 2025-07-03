# 🧮 Advanced Python GUI Calculator

A powerful and stylish calculator app built using **Python** and **Tkinter**.  
Packed with features like history, dark/light theme toggle, fullscreen support, sound feedback, and keyboard input handling — all in a clean, responsive UI.

---

## ⚙ Features

- ✅ **Basic Operations** — Add, subtract, multiply, divide, modulo, and decimals.
- 🕶️ **Dark/Light Mode** — Seamlessly switch between dark and light themes.
- 🔊 **Sound Feedback** — Optional beep sound on key press.
- 🧾 **History Viewer** — View the last 5 calculations with one click.
- 🔁 **Keyboard Input** — Full support for Enter, Backspace, Escape, numbers, and operators.
- 🔍 **Fullscreen Mode** — Toggle fullscreen for a distraction-free experience.
- 🧹 **Clear Options** — Clear input or reset entire session history.
- 💻 **Responsive Layout** — Auto-resizes with window resizing.

## 🖼️ Screenshots
![image](https://github.com/user-attachments/assets/2049463e-ba56-4cb2-97d6-30f19b664515)

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.x
- `tkinter` (comes pre-installed with Python)

### ▶️ Run the App
```
python calculator.py
```

### 🪄 Build Executable (Windows/cmd)

```
pyinstaller --onefile --noconsole calculator.py
```

This will generate a standalone `.exe` in the `dist/` folder, without opening a console window.

---

## 🎯 Keyboard Shortcuts

| Key                                 | Action              |
| ----------------------------------- | ------------------- |
| `Enter` / `=`                       | Evaluate Expression |
| `C`                                 | Clear Input         |
| `Backspace`                         | Delete Last Digit   |
| `Escape`                            | Exit App            |
| `0-9`, `+`, `-`, `*`, `/`, `%`, `.` | Standard Input      |
| `(`, `)`                            | Parentheses         |

## 🧠 Tech Stack

* **Language**: Python
* **GUI Library**: Tkinter

## 📁 File Structure

```
calculator.py      # Main application file
README.md          # Project documentation
/dist              # Output folder after building executable
/build             # PyInstaller build cache (can be ignored)
.spec file         # PyInstaller config (auto-generated)
```

## 🙌 Credits

Created by Vortex/Kritik
Feel free to use, modify, or suggest improvements!
