

# 🚀 Futuristic Calculator Pro

A cutting-edge, feature-rich **Python desktop calculator** built with **Tkinter** and **Matplotlib**.  
Experience the future of calculation with advanced scientific functions, interactive graphing, multiple themes, mobile optimization, and professional UI design.

🔗 **Repository:** [https://github.com/Vortex4047/Calculator.git](https://github.com/Vortex4047/Calculator.git)

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()
[![GUI](https://img.shields.io/badge/GUI-Tkinter-orange.svg)]()

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Vortex4047/Calculator.git
cd Calculator

# Install dependencies
pip install -r requirements.txt

# Run the calculator
python calculator.py
```

## ✨ Features

### 🧮 **Advanced Calculator**
- ✅ **Basic Operations** — Add, subtract, multiply, divide, modulo, percentages, and decimals
- 🔬 **Scientific Functions** — sin, cos, tan, log, ln, sqrt, factorial, power operations
- 📊 **Mathematical Constants** — π (pi), e (Euler's number)
- 🧮 **Complex Expressions** — Parentheses support, order of operations
- 🔢 **Smart Input** — Implicit multiplication, function parsing

### 📈 **Interactive Graphing**
- 📊 **Function Plotting** — Plot mathematical functions with high resolution
- 🖼️ **Reference Images** — Load and overlay reference images for comparison
- 🎯 **Function Presets** — Quick access to common functions (x², sin(x), etc.)
- 🔍 **Zoom & Pan** — Interactive graph manipulation
- 📐 **Customizable Range** — Set custom x-axis ranges for plotting

### 🎨 **Multiple Themes**
- 🌟 **Neon Theme** — Futuristic neon colors with glowing effects
- 🔮 **Glass Theme** — Modern glassmorphism design
- 🤖 **Cyberpunk Theme** — Dark cyberpunk aesthetic
- 🎯 **Minimal Theme** — Clean, minimalist design
- 🎨 **Dynamic Switching** — Change themes on-the-fly

### 📱 **Mobile Optimization**
- 📲 **Touch-Friendly** — Large buttons optimized for touch screens
- 📐 **Responsive Design** — Adapts to different screen sizes automatically
- 👆 **Swipe Gestures** — Swipe left/right to switch between calculator and graphing modes
- 🔤 **Mobile Fonts** — Optimized typography for mobile devices
- 📱 **Compact Layout** — Efficient use of screen space on mobile

### 🎯 **User Experience**
- 🧾 **Calculation History** — View and manage calculation history
- 🔊 **Sound Feedback** — Optional audio feedback for interactions
- ⌨️ **Keyboard Support** — Full keyboard input support
- 🔍 **Fullscreen Mode** — Distraction-free fullscreen experience
- ✨ **Smooth Animations** — Polished UI animations and transitions
- 🎨 **Glassmorphism Effects** — Modern glass-like button effects


## �️ Screesnshots
![Futuristic Calculator Pro](https://github.com/Vortex4047/Calculator/raw/main/screenshot.png)

*Advanced Python calculator with scientific functions, graphing capabilities, and multiple themes*

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.7+
- Required packages (install via pip):
  ```bash
  pip install -r requirements.txt
  ```
  
**Dependencies:**
- `tkinter` (usually comes pre-installed with Python)
- `matplotlib>=3.5.0` (for graphing functionality)
- `numpy>=1.21.0` (for mathematical operations)
- `Pillow>=8.0.0` (for image handling)

### ▶️ Run the App

**Standard Mode:**
```bash
python calculator.py
```

**Mobile Test Mode:**
```bash
python mobile_test.py
```

### 📱 Mobile/Tablet Usage
The calculator automatically detects screen size and optimizes the interface:
- **Mobile Detection:** Screens ≤ 1024x768 automatically use mobile layout
- **Touch Optimization:** Larger buttons and touch-friendly spacing
- **Gesture Support:** Swipe left/right to switch between calculator and graphing modes

### 🪄 Build Executable

**Windows:**
```bash
pyinstaller --onefile --noconsole calculator.py
```

**With Icon (optional):**
```bash
pyinstaller --onefile --noconsole --icon=calculator.ico calculator.py
```

This generates a standalone executable in the `dist/` folder.

## 🎮 Usage Guide

### 🧮 Calculator Mode
1. **Basic Calculations:** Use number buttons and operators for standard math
2. **Scientific Functions:** Access sin, cos, tan, log, sqrt, and more
3. **Constants:** Use π and e buttons for mathematical constants
4. **History:** Click "History" to view past calculations
5. **Themes:** Cycle through themes using the theme button

### 📊 Graphing Mode
1. **Function Input:** Enter mathematical functions using x as variable
   - Examples: `x^2`, `sin(x)`, `x*cos(x)`, `sqrt(x)`
2. **Range Setting:** Set x-axis range using min/max inputs
3. **Plotting:** Click "PLOT" to generate the graph
4. **Presets:** Use preset buttons for common functions
5. **Reference Images:** Load images to overlay on graphs for comparison

### 📱 Mobile Features
- **Auto-Detection:** App automatically optimizes for mobile screens
- **Swipe Navigation:** Swipe left/right to switch between modes
- **Touch Optimization:** Larger buttons and improved spacing
- **Simplified UI:** Streamlined interface for smaller screens

## ⌨️ Keyboard Shortcuts

### Calculator Mode
| Key                                 | Action                    |
| ----------------------------------- | ------------------------- |
| `Enter` / `=`                       | Evaluate Expression       |
| `C`                                 | Clear Current Input       |
| `Ctrl+C`                            | Clear All (History Reset) |
| `Backspace`                         | Delete Last Character     |
| `Escape`                            | Clear Input               |
| `0-9`                               | Number Input              |
| `+`, `-`, `*`, `/`, `%`             | Basic Operations          |
| `.`                                 | Decimal Point             |
| `(`, `)`                            | Parentheses               |

### Graphing Mode
| Key                                 | Action                    |
| ----------------------------------- | ------------------------- |
| `Enter`                             | Plot Function             |
| `Escape`                            | Clear Graph               |

### Global Shortcuts
| Key                                 | Action                    |
| ----------------------------------- | ------------------------- |
| `F11`                               | Toggle Fullscreen         |
| `Tab`                               | Switch Between Modes      |

## 🧠 Tech Stack

* **Language:** Python 3.7+
* **GUI Framework:** Tkinter (built-in)
* **Plotting:** Matplotlib
* **Mathematics:** NumPy
* **Image Processing:** Pillow (PIL)
* **Architecture:** Object-oriented design with responsive UI

## 📁 Project Structure

```
📦 futuristic-calculator/
├── 📄 calculator.py          # Main application with full features
├── 📄 mobile_test.py         # Mobile testing script
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # Project documentation
├── 📁 dist/                 # Built executables (after build)
├── 📁 build/                # Build cache (auto-generated)
└── 📄 *.spec               # PyInstaller config (auto-generated)
```

## 🎯 Function Examples

### Calculator Functions
```python
# Basic operations
2 + 3 * 4        # Result: 14
(5 + 3) / 2      # Result: 4

# Scientific functions
sin(π/2)         # Result: 1
sqrt(16)         # Result: 4
log(100)         # Result: 2
5!               # Result: 120
```

### Graphing Functions
```python
# Polynomial functions
x^2              # Parabola
x^3 - 2*x        # Cubic function

# Trigonometric functions
sin(x)           # Sine wave
cos(x) + sin(x)  # Combined trig functions

# Advanced functions
e^x              # Exponential
ln(x)            # Natural logarithm
x*sin(x)         # Modulated sine wave
```

## 🎨 Themes Preview

### 🌟 Neon Theme (Default)
- Futuristic neon green and blue colors
- Glowing button effects
- Dark background for reduced eye strain

### 🔮 Glass Theme
- Modern glassmorphism design
- Translucent elements
- Soft blue accents

### 🤖 Cyberpunk Theme
- Dark cyberpunk aesthetic
- Red and blue highlights
- High-contrast design

### 🎯 Minimal Theme
- Clean, minimalist design
- Light background
- Professional appearance

## 🐛 Troubleshooting

### Common Issues

**Import Errors:**
```bash
# Install missing dependencies
pip install matplotlib numpy pillow
```

**Display Issues on High-DPI Screens:**
```python
# The app automatically handles DPI scaling
# If issues persist, try running with:
python -m tkinter  # Test tkinter installation
```

**Mobile Detection Not Working:**
- The app detects screen resolution automatically
- For manual mobile testing, use `mobile_test.py`

## 🔄 Updates & Changelog

### Version 2.0 Features
- ✅ Interactive graphing with Matplotlib
- ✅ Multiple theme system
- ✅ Mobile optimization and touch support
- ✅ Reference image overlay for graphs
- ✅ Enhanced scientific calculator
- ✅ Improved error handling
- ✅ Swipe gesture support

### Planned Features
- 🔄 3D graphing capabilities
- 🔄 Equation solver
- 🔄 Unit converter
- 🔄 Custom theme creator
- 🔄 Export graphs as images

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup
```bash
git clone https://github.com/Vortex4047/Calculator.git
cd Calculator
pip install -r requirements.txt
python calculator.py
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙌 Credits

**Created by:** Vortex/Kritik  
**Inspired by:** Modern calculator apps and futuristic UI design  
**Special Thanks:** Python community, Tkinter developers, Matplotlib team

---

⭐ **Star this repository if you found it helpful!**  
🐛 **Report bugs or request features in the Issues section**  
🔄 **Fork and contribute to make it even better!**
