import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.image import imread
import numpy as np
import math
import re
from PIL import Image, ImageTk
import os

class FuturisticCalculator:
    def __init__(self):
        # Main window setup
        self.screen = tk.Tk()
        self.screen.title('Futuristic Calculator Pro')
        self.screen.configure(bg='#0a0a0f')
        self.screen.resizable(True, True)
        
        # Detect screen size and optimize for mobile/tablet
        screen_width = self.screen.winfo_screenwidth()
        screen_height = self.screen.winfo_screenheight()
        
        # Mobile/tablet optimization - better detection
        if screen_width <= 1024 or screen_height <= 768:
            self.is_mobile = True
            # Use most of the screen but leave some margin
            width = int(screen_width * 0.95)
            height = int(screen_height * 0.95)
            self.screen.geometry(f'{width}x{height}')
            # Center the window
            x = (screen_width - width) // 2
            y = (screen_height - height) // 2
            self.screen.geometry(f'{width}x{height}+{x}+{y}')
            
            self.button_font_size = 18
            self.display_font_size = 28
            self.title_font_size = 16
        else:
            self.is_mobile = False
            self.screen.geometry('1400x900')
            self.screen.minsize(1200, 800)
            self.button_font_size = 12
            self.display_font_size = 36
            self.title_font_size = 20
        
        # Global variables
        self.expression = ""
        self.history_log = []
        self.current_mode = "calculator"
        self.current_theme = "neon"  # neon, glass, cyberpunk, minimal
        self.sound_on = True
        self.fullscreen = False
        self.reference_image = None
        
        # Theme configurations
        self.themes = {
            "neon": {
                "bg": "#0a0a0f",
                "primary": "#00ff88",
                "secondary": "#4ecdc4", 
                "accent": "#ff6b6b",
                "button_bg": "#1a1a2e",
                "button_hover": "#16213e",
                "display_bg": "#0f0f23",
                "glass_effect": False
            },
            "glass": {
                "bg": "#1a1a2e",
                "primary": "#ffffff",
                "secondary": "#64b5f6",
                "accent": "#ff4081",
                "button_bg": "#2a2a3e",
                "button_hover": "#3a3a4e",
                "display_bg": "#252538",
                "glass_effect": True
            },
            "cyberpunk": {
                "bg": "#0d1117",
                "primary": "#f0f6fc",
                "secondary": "#58a6ff",
                "accent": "#f85149",
                "button_bg": "#21262d",
                "button_hover": "#30363d",
                "display_bg": "#161b22",
                "glass_effect": False
            },
            "minimal": {
                "bg": "#f5f5f5",
                "primary": "#333333",
                "secondary": "#2196f3",
                "accent": "#ff5722",
                "button_bg": "#ffffff",
                "button_hover": "#e0e0e0",
                "display_bg": "#fafafa",
                "glass_effect": False
            }
        }
        
        self.setup_ui()
        self.bind_events()
        self.apply_theme()
        
    def setup_ui(self):
        # Main container frames
        self.calculator_frame = tk.Frame(self.screen, bg=self.themes[self.current_theme]["bg"])
        self.graphing_frame = tk.Frame(self.screen, bg=self.themes[self.current_theme]["bg"])
        
        self.setup_calculator_ui()
        self.setup_graphing_ui()
        
        # Start with calculator mode
        self.calculator_frame.pack(fill='both', expand=True)
        
    def setup_calculator_ui(self):
        # Header with mobile-optimized design
        header_height = 60 if self.is_mobile else 80
        header_padx = 10 if self.is_mobile else 20
        header_pady = 5 if self.is_mobile else 10
        
        header_frame = tk.Frame(self.calculator_frame, bg=self.themes[self.current_theme]["bg"], height=header_height)
        header_frame.pack(fill='x', padx=header_padx, pady=header_pady)
        header_frame.pack_propagate(False)
        
        # Title with responsive design
        title_frame = tk.Frame(header_frame, bg=self.themes[self.current_theme]["bg"])
        title_frame.pack(side='left', fill='y')
        
        if self.is_mobile:
            title_label = tk.Label(title_frame, text="FUTURISTIC CALC", 
                                  font=('Arial', self.title_font_size, 'bold'), 
                                  bg=self.themes[self.current_theme]["bg"], 
                                  fg=self.themes[self.current_theme]["primary"])
            title_label.pack()
        else:
            title_label = tk.Label(title_frame, text="FUTURISTIC", 
                                  font=('Arial', self.title_font_size, 'bold'), 
                                  bg=self.themes[self.current_theme]["bg"], 
                                  fg=self.themes[self.current_theme]["primary"])
            title_label.pack()
            
            subtitle_label = tk.Label(title_frame, text="CALCULATOR PRO", 
                                     font=('Arial', 12), bg=self.themes[self.current_theme]["bg"], 
                                     fg=self.themes[self.current_theme]["secondary"])
            subtitle_label.pack()
        
        # Control buttons - mobile optimized
        controls_frame = tk.Frame(header_frame, bg=self.themes[self.current_theme]["bg"])
        controls_frame.pack(side='right', fill='y')
        
        if not self.is_mobile:
            # Theme selector (only on desktop)
            theme_frame = tk.Frame(controls_frame, bg=self.themes[self.current_theme]["bg"])
            theme_frame.pack(side='left', padx=10)
            
            tk.Label(theme_frame, text="Theme:", font=('Arial', 10), 
                    bg=self.themes[self.current_theme]["bg"], fg=self.themes[self.current_theme]["primary"]).pack()
            
            self.theme_var = tk.StringVar(value=self.current_theme)
            theme_combo = ttk.Combobox(theme_frame, textvariable=self.theme_var, 
                                      values=list(self.themes.keys()), state="readonly", width=10)
            theme_combo.pack()
            theme_combo.bind('<<ComboboxSelected>>', self.change_theme)
        else:
            # Mobile theme selector (simplified)
            self.theme_var = tk.StringVar(value=self.current_theme)
        
        # Mode switch button - larger for mobile
        button_text = "GRAPH" if self.is_mobile else "GRAPHING"
        self.create_glass_button(controls_frame, button_text, self.switch_to_graphing, 
                                side='right', padx=5 if self.is_mobile else 10)
        
        # Display area - mobile optimized
        display_padx = 10 if self.is_mobile else 20
        display_pady = 5 if self.is_mobile else 10
        
        display_container = tk.Frame(self.calculator_frame, bg=self.themes[self.current_theme]["bg"])
        display_container.pack(fill='x', padx=display_padx, pady=display_pady)
        
        # Main display - responsive font size
        display_height = 2 if self.is_mobile else 2
        display_padx_inner = 15 if self.is_mobile else 20
        
        # Use a more mobile-friendly font
        display_font = "Arial" if self.is_mobile else "JetBrains Mono"
        
        self.label_result = tk.Label(display_container, text="0", anchor='e', 
                                    font=(display_font, self.display_font_size, 'bold'), 
                                    height=display_height, 
                                    bg=self.themes[self.current_theme]["display_bg"], 
                                    fg=self.themes[self.current_theme]["primary"], 
                                    relief='flat', bd=0, padx=display_padx_inner,
                                    wraplength=400 if self.is_mobile else 0)
        self.label_result.pack(fill='x', pady=5)
        
        # History display - smaller on mobile
        if not self.is_mobile:
            history_frame = tk.Frame(display_container, bg=self.themes[self.current_theme]["bg"])
            history_frame.pack(fill='x', pady=5)
            
            tk.Label(history_frame, text="History:", font=('Arial', 10, 'bold'), 
                    bg=self.themes[self.current_theme]["bg"], fg=self.themes[self.current_theme]["secondary"]).pack(anchor='w')
            
            self.history_display = tk.Text(history_frame, height=2, bg=self.themes[self.current_theme]["display_bg"], 
                                          fg=self.themes[self.current_theme]["secondary"], 
                                          font=('JetBrains Mono', 9), bd=0, wrap='word')
            self.history_display.pack(fill='x')
        else:
            # Minimal history for mobile
            self.history_display = tk.Text(display_container, height=1, bg=self.themes[self.current_theme]["display_bg"], 
                                          fg=self.themes[self.current_theme]["secondary"], 
                                          font=('JetBrains Mono', 8), bd=0, wrap='word')
            self.history_display.pack(fill='x', pady=2)
        
        # Button area with professional layout
        self.setup_calculator_buttons()
        
    def setup_calculator_buttons(self):
        button_padx = 10 if self.is_mobile else 20
        button_pady = 5 if self.is_mobile else 10
        
        button_container = tk.Frame(self.calculator_frame, bg=self.themes[self.current_theme]["bg"])
        button_container.pack(fill='both', expand=True, padx=button_padx, pady=button_pady)
        
        # Scientific functions panel - responsive layout
        if self.is_mobile:
            # Compact scientific functions for mobile - scrollable
            sci_frame = tk.Frame(button_container, bg=self.themes[self.current_theme]["bg"])
            sci_frame.pack(fill='x', pady=3)
            
            sci_buttons = [
                ('sin', lambda: self.show('sin(')), ('cos', lambda: self.show('cos(')), 
                ('tan', lambda: self.show('tan(')), ('sqrt', lambda: self.show('sqrt(')),
                ('pi', lambda: self.show('π')), ('e', lambda: self.show('e')),
                ('^', lambda: self.show('^')), ('log', lambda: self.show('log(')),
            ]
            
            # 4 buttons per row on mobile
            for i, (text, cmd) in enumerate(sci_buttons):
                self.create_glass_button(sci_frame, text, cmd, row=i//4, column=i%4, 
                                       sticky='ew', padx=2, pady=2, button_type='scientific')
            
            for i in range(4):
                sci_frame.grid_columnconfigure(i, weight=1)
        else:
            # Full scientific functions for desktop
            sci_frame = tk.LabelFrame(button_container, text="Scientific Functions", 
                                     bg=self.themes[self.current_theme]["bg"], 
                                     fg=self.themes[self.current_theme]["primary"],
                                     font=('Arial', 10, 'bold'), bd=0)
            sci_frame.pack(fill='x', pady=5)
            
            sci_buttons = [
                ('sin', lambda: self.show('sin(')), ('cos', lambda: self.show('cos(')), 
                ('tan', lambda: self.show('tan(')), ('log', lambda: self.show('log(')),
                ('ln', lambda: self.show('ln(')), ('√', lambda: self.show('sqrt(')),
                ('π', lambda: self.show('π')), ('e', lambda: self.show('e')),
                ('^', lambda: self.show('^')), ('!', lambda: self.show('!')),
            ]
            
            for i, (text, cmd) in enumerate(sci_buttons):
                self.create_glass_button(sci_frame, text, cmd, row=i//5, column=i%5, 
                                       sticky='ew', padx=2, pady=2, button_type='scientific')
            
            for i in range(5):
                sci_frame.grid_columnconfigure(i, weight=1)
        
        # Main calculator grid - responsive layout
        main_frame = tk.Frame(button_container, bg=self.themes[self.current_theme]["bg"])
        main_frame.pack(fill='both', expand=True, pady=5)
        
        if self.is_mobile:
            # Mobile layout - single column with larger buttons
            numbers_frame = tk.Frame(main_frame, bg=self.themes[self.current_theme]["bg"])
            numbers_frame.pack(fill='both', expand=True)
            
            # Mobile number pad layout
            number_buttons = [
                ('C', self.clear, 0, 0, 'clear'), ('⌫', self.backspace, 0, 1, 'clear'),
                ('(', lambda: self.show('('), 0, 2, 'operator'), (')', lambda: self.show(')'), 0, 3, 'operator'),
                
                ('7', lambda: self.show('7'), 1, 0, 'number'), ('8', lambda: self.show('8'), 1, 1, 'number'),
                ('9', lambda: self.show('9'), 1, 2, 'number'), ('/', lambda: self.show('/'), 1, 3, 'operator'),
                
                ('4', lambda: self.show('4'), 2, 0, 'number'), ('5', lambda: self.show('5'), 2, 1, 'number'),
                ('6', lambda: self.show('6'), 2, 2, 'number'), ('×', lambda: self.show('*'), 2, 3, 'operator'),
                
                ('1', lambda: self.show('1'), 3, 0, 'number'), ('2', lambda: self.show('2'), 3, 1, 'number'),
                ('3', lambda: self.show('3'), 3, 2, 'number'), ('-', lambda: self.show('-'), 3, 3, 'operator'),
                
                ('0', lambda: self.show('0'), 4, 0, 'number'), ('.', lambda: self.show('.'), 4, 1, 'number'),
                ('%', lambda: self.show('%'), 4, 2, 'operator'), ('+', lambda: self.show('+'), 4, 3, 'operator'),
            ]
            
            for text, cmd, row, col, btn_type in number_buttons:
                self.create_glass_button(numbers_frame, text, cmd, row=row, column=col, 
                                       sticky='nsew', padx=2, pady=2, button_type=btn_type)
            
            # Equals button (spans full width)
            self.create_glass_button(numbers_frame, '=', self.calculate, row=5, column=0, 
                                    columnspan=4, sticky='ew', padx=2, pady=2, button_type='equals')
            
            # Utility buttons row - simplified for mobile
            utility_buttons = [
                ('HIST', self.show_history), ('THEME', self.cycle_theme), 
                ('CLR', self.clear_all), ('EXIT', self.exit_app),
            ]
            
            for i, (text, cmd) in enumerate(utility_buttons):
                self.create_glass_button(numbers_frame, text, cmd, row=6, column=i, 
                                       sticky='ew', padx=2, pady=2, button_type='utility')
            
            # Configure grid weights
            for i in range(7):
                numbers_frame.grid_rowconfigure(i, weight=1)
            for i in range(4):
                numbers_frame.grid_columnconfigure(i, weight=1)
                
        else:
            # Desktop layout - two columns
            # Left side - Numbers and basic operations
            numbers_frame = tk.LabelFrame(main_frame, text="Numbers & Operations", 
                                         bg=self.themes[self.current_theme]["bg"], 
                                         fg=self.themes[self.current_theme]["primary"],
                                         font=('Arial', 10, 'bold'), bd=0)
            numbers_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
            
            # Number pad layout
            number_buttons = [
                ('C', self.clear, 0, 0, 'clear'), ('⌫', self.backspace, 0, 1, 'clear'),
                ('(', lambda: self.show('('), 0, 2, 'operator'), (')', lambda: self.show(')'), 0, 3, 'operator'),
                
                ('7', lambda: self.show('7'), 1, 0, 'number'), ('8', lambda: self.show('8'), 1, 1, 'number'),
                ('9', lambda: self.show('9'), 1, 2, 'number'), ('/', lambda: self.show('/'), 1, 3, 'operator'),
                
                ('4', lambda: self.show('4'), 2, 0, 'number'), ('5', lambda: self.show('5'), 2, 1, 'number'),
                ('6', lambda: self.show('6'), 2, 2, 'number'), ('×', lambda: self.show('*'), 2, 3, 'operator'),
                
                ('1', lambda: self.show('1'), 3, 0, 'number'), ('2', lambda: self.show('2'), 3, 1, 'number'),
                ('3', lambda: self.show('3'), 3, 2, 'number'), ('-', lambda: self.show('-'), 3, 3, 'operator'),
                
                ('0', lambda: self.show('0'), 4, 0, 'number'), ('.', lambda: self.show('.'), 4, 1, 'number'),
                ('%', lambda: self.show('%'), 4, 2, 'operator'), ('+', lambda: self.show('+'), 4, 3, 'operator'),
            ]
            
            for text, cmd, row, col, btn_type in number_buttons:
                self.create_glass_button(numbers_frame, text, cmd, row=row, column=col, 
                                       sticky='nsew', padx=3, pady=3, button_type=btn_type)
            
            # Equals button (spans 2 columns)
            self.create_glass_button(numbers_frame, '=', self.calculate, row=5, column=0, 
                                    columnspan=4, sticky='ew', padx=3, pady=3, button_type='equals')
            
            # Configure grid weights
            for i in range(6):
                numbers_frame.grid_rowconfigure(i, weight=1)
            for i in range(4):
                numbers_frame.grid_columnconfigure(i, weight=1)
            
            # Right side - Utility functions
            utils_frame = tk.LabelFrame(main_frame, text="Utilities", 
                                       bg=self.themes[self.current_theme]["bg"], 
                                       fg=self.themes[self.current_theme]["primary"],
                                       font=('Arial', 10, 'bold'), bd=0)
            utils_frame.pack(side='right', fill='y')
            
            utility_buttons = [
                ('History', self.show_history),
                ('Sound', self.toggle_sound),
                ('Theme', self.cycle_theme),
                ('Fullscreen', self.toggle_fullscreen),
                ('Clear All', self.clear_all),
                ('Exit', self.exit_app),
            ]
            
            for i, (text, cmd) in enumerate(utility_buttons):
                self.create_glass_button(utils_frame, text, cmd, row=i, column=0, 
                                       sticky='ew', padx=5, pady=3, button_type='utility')
            
            utils_frame.grid_columnconfigure(0, weight=1)
        
    def setup_graphing_ui(self):
        # Header - mobile optimized
        header_height = 60 if self.is_mobile else 80
        header_padx = 10 if self.is_mobile else 20
        header_pady = 5 if self.is_mobile else 10
        
        graph_header = tk.Frame(self.graphing_frame, bg=self.themes[self.current_theme]["bg"], height=header_height)
        graph_header.pack(fill='x', padx=header_padx, pady=header_pady)
        graph_header.pack_propagate(False)
        
        title_text = "GRAPHER" if self.is_mobile else "FUNCTION GRAPHER"
        title_font_size = self.title_font_size if self.is_mobile else 18
        
        title_label = tk.Label(graph_header, text=title_text, 
                              font=('Arial', title_font_size, 'bold'), bg=self.themes[self.current_theme]["bg"], 
                              fg=self.themes[self.current_theme]["secondary"])
        title_label.pack(side='left', pady=15 if not self.is_mobile else 10)
        
        button_text = "CALC" if self.is_mobile else "CALCULATOR"
        self.create_glass_button(graph_header, button_text, self.switch_to_calculator, 
                                side='right', padx=5 if self.is_mobile else 10, pady=10 if self.is_mobile else 15)
        
        # Control panel - mobile optimized
        control_padx = 10 if self.is_mobile else 20
        control_pady = 5 if self.is_mobile else 10
        
        control_panel = tk.Frame(self.graphing_frame, bg=self.themes[self.current_theme]["bg"])
        control_panel.pack(fill='x', padx=control_padx, pady=control_pady)
        
        # Function input with mobile-friendly UI
        if self.is_mobile:
            input_frame = tk.Frame(control_panel, bg=self.themes[self.current_theme]["bg"])
            input_frame.pack(fill='x', pady=3)
        else:
            input_frame = tk.LabelFrame(control_panel, text="Function Input", 
                                       bg=self.themes[self.current_theme]["bg"], 
                                       fg=self.themes[self.current_theme]["primary"],
                                       font=('Arial', 10, 'bold'), bd=0)
            input_frame.pack(fill='x', pady=5)
        
        # Function entry - responsive
        func_input_frame = tk.Frame(input_frame, bg=self.themes[self.current_theme]["bg"])
        func_input_frame.pack(fill='x', padx=5 if self.is_mobile else 10, pady=3 if self.is_mobile else 5)
        
        label_font_size = 12 if self.is_mobile else 14
        entry_font_size = 12 if self.is_mobile else 14
        
        tk.Label(func_input_frame, text="f(x) =", font=('Arial', label_font_size, 'bold'), 
                bg=self.themes[self.current_theme]["bg"], fg=self.themes[self.current_theme]["primary"]).pack(side='left', padx=3)
        
        self.function_entry = tk.Entry(func_input_frame, font=('JetBrains Mono', entry_font_size), 
                                      bg=self.themes[self.current_theme]["display_bg"], 
                                      fg=self.themes[self.current_theme]["primary"], 
                                      insertbackground=self.themes[self.current_theme]["primary"], 
                                      bd=0, relief='flat')
        self.function_entry.pack(side='left', fill='x', expand=True, padx=3)
        self.function_entry.insert(0, "x^2")
        
        # Range and plot controls - mobile responsive
        controls_frame = tk.Frame(input_frame, bg=self.themes[self.current_theme]["bg"])
        controls_frame.pack(fill='x', padx=5 if self.is_mobile else 10, pady=3 if self.is_mobile else 5)
        
        if self.is_mobile:
            # Mobile layout - stacked controls
            range_frame = tk.Frame(controls_frame, bg=self.themes[self.current_theme]["bg"])
            range_frame.pack(fill='x', pady=2)
            
            tk.Label(range_frame, text="Range:", font=('Arial', 10, 'bold'), 
                    bg=self.themes[self.current_theme]["bg"], fg=self.themes[self.current_theme]["primary"]).pack(side='left', padx=2)
            
            self.x_min_entry = tk.Entry(range_frame, font=('JetBrains Mono', 10), 
                                       bg=self.themes[self.current_theme]["display_bg"], 
                                       fg=self.themes[self.current_theme]["primary"], 
                                       insertbackground=self.themes[self.current_theme]["primary"], 
                                       bd=0, width=6)
            self.x_min_entry.pack(side='left', padx=2)
            self.x_min_entry.insert(0, "-10")
            
            tk.Label(range_frame, text="to", font=('Arial', 10), 
                    bg=self.themes[self.current_theme]["bg"], fg=self.themes[self.current_theme]["secondary"]).pack(side='left', padx=2)
            
            self.x_max_entry = tk.Entry(range_frame, font=('JetBrains Mono', 10), 
                                       bg=self.themes[self.current_theme]["display_bg"], 
                                       fg=self.themes[self.current_theme]["primary"], 
                                       insertbackground=self.themes[self.current_theme]["primary"], 
                                       bd=0, width=6)
            self.x_max_entry.pack(side='left', padx=2)
            self.x_max_entry.insert(0, "10")
            
            # Button row for mobile
            button_frame = tk.Frame(controls_frame, bg=self.themes[self.current_theme]["bg"])
            button_frame.pack(fill='x', pady=2)
            
            self.create_glass_button(button_frame, "PLOT", self.plot_function, 
                                    side='left', padx=2, button_type='equals')
            
            self.create_glass_button(button_frame, "IMG", self.load_reference_image, 
                                    side='left', padx=2, button_type='utility')
            
            self.create_glass_button(button_frame, "CLR", self.clear_reference_image, 
                                    side='left', padx=2, button_type='clear')
        else:
            # Desktop layout - horizontal controls
            tk.Label(controls_frame, text="Range:", font=('Arial', 12, 'bold'), 
                    bg=self.themes[self.current_theme]["bg"], fg=self.themes[self.current_theme]["primary"]).pack(side='left', padx=5)
            
            tk.Label(controls_frame, text="x min:", font=('Arial', 10), 
                    bg=self.themes[self.current_theme]["bg"], fg=self.themes[self.current_theme]["secondary"]).pack(side='left', padx=2)
            
            self.x_min_entry = tk.Entry(controls_frame, font=('JetBrains Mono', 10), 
                                       bg=self.themes[self.current_theme]["display_bg"], 
                                       fg=self.themes[self.current_theme]["primary"], 
                                       insertbackground=self.themes[self.current_theme]["primary"], 
                                       bd=0, width=8)
            self.x_min_entry.pack(side='left', padx=2)
            self.x_min_entry.insert(0, "-10")
            
            tk.Label(controls_frame, text="x max:", font=('Arial', 10), 
                    bg=self.themes[self.current_theme]["bg"], fg=self.themes[self.current_theme]["secondary"]).pack(side='left', padx=2)
            
            self.x_max_entry = tk.Entry(controls_frame, font=('JetBrains Mono', 10), 
                                       bg=self.themes[self.current_theme]["display_bg"], 
                                       fg=self.themes[self.current_theme]["primary"], 
                                       insertbackground=self.themes[self.current_theme]["primary"], 
                                       bd=0, width=8)
            self.x_max_entry.pack(side='left', padx=2)
            self.x_max_entry.insert(0, "10")
            
            # Plot button
            self.create_glass_button(controls_frame, "PLOT", self.plot_function, 
                                    side='left', padx=10, button_type='equals')
            
            # Reference image button
            self.create_glass_button(controls_frame, "Load Image", self.load_reference_image, 
                                    side='left', padx=5, button_type='utility')
            
            # Clear image button
            self.create_glass_button(controls_frame, "Clear Image", self.clear_reference_image, 
                                    side='left', padx=5, button_type='clear')
        
        # Function presets - mobile responsive
        if self.is_mobile:
            presets_frame = tk.Frame(control_panel, bg=self.themes[self.current_theme]["bg"])
            presets_frame.pack(fill='x', pady=3)
            
            # Compact presets for mobile
            preset_buttons = [
                ('x²', 'x^2'), ('x³', 'x^3'), ('sin', 'sin(x)'), ('cos', 'cos(x)'),
                ('tan', 'tan(x)'), ('ln', 'ln(x)'), ('√x', 'sqrt(x)'), ('1/x', '1/x'),
            ]
            
            # 4 buttons per row on mobile
            for i, (display, func) in enumerate(preset_buttons):
                self.create_glass_button(presets_frame, display, 
                                       lambda f=func: self.set_function(f),
                                       row=i//4, column=i%4, sticky='ew', padx=1, pady=1, 
                                       button_type='scientific')
            
            for i in range(4):
                presets_frame.grid_columnconfigure(i, weight=1)
        else:
            presets_frame = tk.LabelFrame(control_panel, text="Function Presets", 
                                         bg=self.themes[self.current_theme]["bg"], 
                                         fg=self.themes[self.current_theme]["primary"],
                                         font=('Arial', 10, 'bold'), bd=0)
            presets_frame.pack(fill='x', pady=5)
            
            preset_buttons = [
                ('x²', 'x^2'), ('x³', 'x^3'), ('sin(x)', 'sin(x)'), ('cos(x)', 'cos(x)'),
                ('tan(x)', 'tan(x)'), ('ln(x)', 'ln(x)'), ('√x', 'sqrt(x)'), ('1/x', '1/x'),
                ('e^x', 'e^x'), ('|x|', 'abs(x)'), ('x·sin(x)', 'x*sin(x)'), ('sin(x)/x', 'sin(x)/x')
            ]
            
            for i, (display, func) in enumerate(preset_buttons):
                self.create_glass_button(presets_frame, display, 
                                       lambda f=func: self.set_function(f),
                                       row=i//6, column=i%6, sticky='ew', padx=2, pady=2, 
                                       button_type='scientific')
            
            for i in range(6):
                presets_frame.grid_columnconfigure(i, weight=1)
        
        # Matplotlib setup with enhanced styling
        self.setup_matplotlib()
        
    def setup_matplotlib(self):
        plt.style.use('dark_background')
        
        # Mobile-responsive figure size
        if self.is_mobile:
            figsize = (8, 5)
            canvas_padx = 5
            canvas_pady = 5
            font_size = 10
        else:
            figsize = (12, 8)
            canvas_padx = 20
            canvas_pady = 10
            font_size = 12
        
        self.fig, self.ax = plt.subplots(figsize=figsize, facecolor=self.themes[self.current_theme]["bg"])
        self.fig.patch.set_facecolor(self.themes[self.current_theme]["bg"])
        self.ax.set_facecolor(self.themes[self.current_theme]["display_bg"])
        
        # Enhanced grid and styling
        self.ax.grid(True, alpha=0.3, color=self.themes[self.current_theme]["secondary"], linestyle='--')
        self.ax.set_xlabel('x', color=self.themes[self.current_theme]["primary"], fontsize=font_size, fontweight='bold')
        self.ax.set_ylabel('y', color=self.themes[self.current_theme]["primary"], fontsize=font_size, fontweight='bold')
        self.ax.tick_params(colors=self.themes[self.current_theme]["primary"], labelsize=font_size-2)
        
        self.canvas = FigureCanvasTkAgg(self.fig, self.graphing_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True, padx=canvas_padx, pady=canvas_pady)
        
    def create_glass_button(self, parent, text, command, row=None, column=None, columnspan=1, 
                           sticky='', padx=5, pady=5, side=None, button_type='normal'):
        """Create a glassmorphism-style button with mobile-optimized sizing"""
        
        # Color scheme based on button type
        color_schemes = {
            'normal': (self.themes[self.current_theme]["button_bg"], self.themes[self.current_theme]["primary"]),
            'number': (self.themes[self.current_theme]["button_bg"], self.themes[self.current_theme]["primary"]),
            'operator': (self.themes[self.current_theme]["secondary"], 'white'),
            'equals': (self.themes[self.current_theme]["accent"], 'white'),
            'clear': ('#ff6b6b', 'white'),
            'scientific': ('#9b59b6', 'white'),
            'utility': (self.themes[self.current_theme]["secondary"], 'white')
        }
        
        bg_color, fg_color = color_schemes.get(button_type, color_schemes['normal'])
        
        # Mobile-optimized button sizing
        if self.is_mobile:
            button_padx = 8
            button_pady = 20 if button_type in ['number', 'operator', 'equals'] else 15
        else:
            button_padx = 10
            button_pady = 8
        
        btn = tk.Button(parent, text=text, command=command, 
                       font=('Arial', self.button_font_size, 'bold'), bd=0, relief='flat',
                       bg=bg_color, fg=fg_color, 
                       activebackground=self.themes[self.current_theme]["button_hover"],
                       activeforeground=fg_color, cursor='hand2',
                       padx=button_padx, pady=button_pady)
        
        # Enhanced hover effects with animation
        def on_enter(e):
            btn.config(bg=self.themes[self.current_theme]["button_hover"], 
                      relief='raised', bd=2)
            if self.sound_on:
                self.screen.bell()
        
        def on_leave(e):
            btn.config(bg=bg_color, relief='flat', bd=0)
        
        def on_click(e):
            btn.config(relief='sunken', bd=2)
            self.screen.after(100, lambda: btn.config(relief='flat', bd=0))
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.bind("<Button-1>", on_click)
        
        # Positioning
        if row is not None and column is not None:
            btn.grid(row=row, column=column, columnspan=columnspan, 
                    sticky=sticky, padx=padx, pady=pady)
        elif side:
            btn.pack(side=side, padx=padx, pady=pady)
        else:
            btn.pack(padx=padx, pady=pady)
        
        return btn
    
    # -------------------- CALCULATOR FUNCTIONS --------------------
    def show(self, value):
        if self.expression == "0" or self.expression == "Error":
            self.expression = ""
        self.expression += value
        self.label_result.config(text=self.expression)
        self.animate_display()
    
    def clear(self):
        self.expression = "0"
        self.label_result.config(text=self.expression)
        self.animate_clear()
    
    def clear_all(self):
        self.expression = "0"
        self.history_log.clear()
        self.label_result.config(text=self.expression)
        self.update_history_display()
        self.animate_clear()
    
    def backspace(self):
        if len(self.expression) > 1:
            self.expression = self.expression[:-1]
        else:
            self.expression = "0"
        self.label_result.config(text=self.expression)
    
    def calculate(self):
        try:
            # Enhanced calculation with more functions
            safe_expression = self.expression.replace('^', '**')
            safe_expression = safe_expression.replace('×', '*')
            safe_expression = safe_expression.replace('÷', '/')
            
            # Mathematical functions
            safe_expression = re.sub(r'sin\(', 'math.sin(', safe_expression)
            safe_expression = re.sub(r'cos\(', 'math.cos(', safe_expression)
            safe_expression = re.sub(r'tan\(', 'math.tan(', safe_expression)
            safe_expression = re.sub(r'log\(', 'math.log10(', safe_expression)
            safe_expression = re.sub(r'ln\(', 'math.log(', safe_expression)
            safe_expression = re.sub(r'sqrt\(', 'math.sqrt(', safe_expression)
            safe_expression = re.sub(r'abs\(', 'abs(', safe_expression)
            
            # Constants
            safe_expression = safe_expression.replace('π', str(math.pi))
            safe_expression = safe_expression.replace('e', str(math.e))
            
            # Factorial
            safe_expression = re.sub(r'(\d+)!', r'math.factorial(\1)', safe_expression)
            
            result = str(eval(safe_expression))
            
            # Format result for better display
            if '.' in result:
                result = f"{float(result):.10g}"
            
            self.history_log.append(f"{self.expression} = {result}")
            self.label_result.config(text=result)
            self.expression = result
            self.update_history_display()
            self.animate_result()
            
        except Exception as e:
            self.label_result.config(text="Error")
            self.expression = "0"
            self.animate_error()
    
    # -------------------- GRAPHING FUNCTIONS --------------------
    def plot_function(self):
        try:
            func_text = self.function_entry.get()
            x_min = float(self.x_min_entry.get())
            x_max = float(self.x_max_entry.get())
            
            # Create x values with higher resolution
            x = np.linspace(x_min, x_max, 2000)
            
            # Parse and evaluate function with better handling
            func_text = self.parse_function(func_text)
            
            # Evaluate function
            y = eval(func_text, {"x": x, "np": np, "math": math, "sin": np.sin, 
                                "cos": np.cos, "tan": np.tan, "log": np.log10, 
                                "ln": np.log, "sqrt": np.sqrt, "abs": np.abs,
                                "pi": np.pi, "e": np.e})
            
            # Clear and plot with enhanced styling
            self.ax.clear()
            
            # Plot reference image if loaded
            if self.reference_image is not None:
                self.ax.imshow(self.reference_image, extent=[x_min, x_max, -10, 10], 
                              alpha=0.3, aspect='auto')
            
            # Plot function with gradient effect
            self.ax.plot(x, y, color=self.themes[self.current_theme]["accent"], 
                        linewidth=3, alpha=0.9, label=f'f(x) = {self.function_entry.get()}')
            
            # Enhanced styling
            self.ax.grid(True, alpha=0.3, color=self.themes[self.current_theme]["secondary"], 
                        linestyle='--', linewidth=0.5)
            self.ax.set_facecolor(self.themes[self.current_theme]["display_bg"])
            self.ax.set_xlabel('x', color=self.themes[self.current_theme]["primary"], 
                              fontsize=12, fontweight='bold')
            self.ax.set_ylabel('y', color=self.themes[self.current_theme]["primary"], 
                              fontsize=12, fontweight='bold')
            self.ax.tick_params(colors=self.themes[self.current_theme]["primary"])
            self.ax.legend(facecolor=self.themes[self.current_theme]["button_bg"], 
                          edgecolor=self.themes[self.current_theme]["secondary"])
            
            # Add zero lines
            self.ax.axhline(y=0, color=self.themes[self.current_theme]["primary"], 
                           linewidth=1, alpha=0.5)
            self.ax.axvline(x=0, color=self.themes[self.current_theme]["primary"], 
                           linewidth=1, alpha=0.5)
            
            self.canvas.draw()
            
        except Exception as e:
            self.show_notification(f"Error plotting: {str(e)}")
    
    def parse_function(self, func_text):
        """Enhanced function parsing with better x handling"""
        # Handle implicit multiplication with x
        func_text = re.sub(r'(\d)x', r'\1*x', func_text)
        func_text = re.sub(r'x(\d)', r'x*\1', func_text)
        func_text = re.sub(r'\)x', r')*x', func_text)
        func_text = re.sub(r'x\(', r'x*(', func_text)
        
        # Replace mathematical notation
        func_text = func_text.replace('^', '**')
        func_text = func_text.replace('π', 'pi')
        
        return func_text
    
    def set_function(self, func):
        self.function_entry.delete(0, 'end')
        self.function_entry.insert(0, func)
    
    def load_reference_image(self):
        """Load a reference image for graphing overlay"""
        try:
            file_path = filedialog.askopenfilename(
                title="Select Reference Image",
                filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff")]
            )
            
            if file_path:
                # Load and process image
                img = imread(file_path)
                self.reference_image = img
                self.show_notification("Reference image loaded successfully!")
                
        except Exception as e:
            self.show_notification(f"Error loading image: {str(e)}")
    
    def clear_reference_image(self):
        """Clear the reference image"""
        self.reference_image = None
        self.show_notification("Reference image cleared!")
        # Replot to remove image
        self.plot_function()
    
    # -------------------- UI FUNCTIONS --------------------
    def switch_to_graphing(self):
        self.current_mode = "graphing"
        self.calculator_frame.pack_forget()
        self.graphing_frame.pack(fill='both', expand=True)
    
    def switch_to_calculator(self):
        self.current_mode = "calculator"
        self.graphing_frame.pack_forget()
        self.calculator_frame.pack(fill='both', expand=True)
    
    def change_theme(self, event=None):
        self.current_theme = self.theme_var.get()
        self.apply_theme()
    
    def cycle_theme(self):
        themes = list(self.themes.keys())
        current_index = themes.index(self.current_theme)
        next_index = (current_index + 1) % len(themes)
        self.current_theme = themes[next_index]
        self.theme_var.set(self.current_theme)
        self.apply_theme()
    
    def apply_theme(self):
        """Apply the selected theme to all UI elements"""
        theme = self.themes[self.current_theme]
        
        # Update main window
        self.screen.configure(bg=theme["bg"])
        
        # Update frames
        for frame in [self.calculator_frame, self.graphing_frame]:
            frame.configure(bg=theme["bg"])
        
        # Update display
        if hasattr(self, 'label_result'):
            self.label_result.configure(bg=theme["display_bg"], fg=theme["primary"])
        
        # Update matplotlib if in graphing mode
        if hasattr(self, 'fig'):
            self.fig.patch.set_facecolor(theme["bg"])
            self.ax.set_facecolor(theme["display_bg"])
            self.canvas.draw()
    
    def toggle_sound(self):
        self.sound_on = not self.sound_on
        self.show_notification(f"Sound {'ON' if self.sound_on else 'OFF'}")
    
    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.screen.attributes('-fullscreen', self.fullscreen)
    
    def show_history(self):
        """Show calculation history in a modern popup"""
        history_window = tk.Toplevel(self.screen)
        history_window.title("Calculation History")
        history_window.configure(bg=self.themes[self.current_theme]["bg"])
        history_window.geometry('500x400')
        history_window.resizable(True, True)
        
        # Header
        header = tk.Frame(history_window, bg=self.themes[self.current_theme]["bg"])
        header.pack(fill='x', padx=20, pady=10)
        
        tk.Label(header, text="Calculation History", 
                font=('Arial', 16, 'bold'), bg=self.themes[self.current_theme]["bg"], 
                fg=self.themes[self.current_theme]["primary"]).pack(side='left')
        
        # Clear history button
        self.create_glass_button(header, "Clear", 
                                lambda: [self.history_log.clear(), self.update_history_display(), history_window.destroy()],
                                side='right', button_type='clear')
        
        # History display with scrollbar
        text_frame = tk.Frame(history_window, bg=self.themes[self.current_theme]["bg"])
        text_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')
        
        history_text = tk.Text(text_frame, bg=self.themes[self.current_theme]["display_bg"], 
                              fg=self.themes[self.current_theme]["primary"], 
                              font=('JetBrains Mono', 12), yscrollcommand=scrollbar.set,
                              wrap='word', bd=0)
        history_text.pack(side='left', fill='both', expand=True)
        
        scrollbar.config(command=history_text.yview)
        
        # Populate history
        for item in self.history_log:
            history_text.insert('end', item + '\n')
        
        history_text.config(state='disabled')
    
    def update_history_display(self):
        """Update the mini history display"""
        if hasattr(self, 'history_display'):
            self.history_display.config(state='normal')
            self.history_display.delete(1.0, 'end')
            for item in self.history_log[-3:]:  # Show last 3 items
                self.history_display.insert('end', item + '\n')
            self.history_display.config(state='disabled')
    
    def show_notification(self, message):
        """Show a modern notification popup"""
        notification = tk.Toplevel(self.screen)
        notification.title("Notification")
        notification.configure(bg=self.themes[self.current_theme]["bg"])
        notification.geometry('350x120')
        notification.resizable(False, False)
        
        # Center the notification
        notification.transient(self.screen)
        notification.grab_set()
        
        # Content
        content_frame = tk.Frame(notification, bg=self.themes[self.current_theme]["bg"])
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(content_frame, text="INFO", font=('Arial', 14, 'bold'), 
                bg=self.themes[self.current_theme]["bg"], 
                fg=self.themes[self.current_theme]["secondary"]).pack()
        
        tk.Label(content_frame, text=message, bg=self.themes[self.current_theme]["bg"], 
                fg=self.themes[self.current_theme]["primary"], 
                font=('Arial', 12), wraplength=300).pack(pady=10)
        
        # Auto-close after 2 seconds
        self.screen.after(2000, notification.destroy)
    
    # -------------------- ANIMATION FUNCTIONS --------------------
    def animate_display(self):
        """Animate display updates"""
        original_color = self.label_result.cget('fg')
        self.label_result.config(fg=self.themes[self.current_theme]["secondary"])
        self.screen.after(100, lambda: self.label_result.config(fg=original_color))
    
    def animate_clear(self):
        """Animate clear operation"""
        self.label_result.config(fg=self.themes[self.current_theme]["accent"])
        self.screen.after(200, lambda: self.label_result.config(fg=self.themes[self.current_theme]["primary"]))
    
    def animate_result(self):
        """Animate calculation result"""
        self.label_result.config(fg=self.themes[self.current_theme]["secondary"])
        self.screen.after(500, lambda: self.label_result.config(fg=self.themes[self.current_theme]["primary"]))
    
    def animate_error(self):
        """Animate error state"""
        for i in range(3):
            self.screen.after(i*200, lambda: self.label_result.config(fg='#ff6b6b'))
            self.screen.after(i*200+100, lambda: self.label_result.config(fg=self.themes[self.current_theme]["primary"]))
    
    def exit_app(self):
        """Clean exit with mobile-friendly confirmation"""
        if self.is_mobile:
            # Simple exit for mobile (no confirmation dialog)
            self.screen.destroy()
        else:
            # Confirmation dialog for desktop
            if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
                self.screen.destroy()
    
    # -------------------- EVENT HANDLING --------------------
    def bind_events(self):
        """Bind keyboard and touch events"""
        self.screen.bind("<Key>", self.key_press)
        self.screen.focus_set()
        
        # Mobile-specific touch events
        if self.is_mobile:
            # Disable keyboard focus to prevent virtual keyboard
            self.screen.focus_set()
            
            # Add swipe gestures (simplified)
            self.screen.bind("<Button-1>", self.on_touch_start)
            self.screen.bind("<B1-Motion>", self.on_touch_move)
            self.screen.bind("<ButtonRelease-1>", self.on_touch_end)
            
            self.touch_start_x = 0
            self.touch_start_y = 0
        
        # Window events
        self.screen.protocol("WM_DELETE_WINDOW", self.exit_app)
    
    def on_touch_start(self, event):
        """Handle touch start"""
        self.touch_start_x = event.x
        self.touch_start_y = event.y
    
    def on_touch_move(self, event):
        """Handle touch move"""
        pass
    
    def on_touch_end(self, event):
        """Handle touch end - detect swipes"""
        if not self.is_mobile:
            return
            
        dx = event.x - self.touch_start_x
        dy = event.y - self.touch_start_y
        
        # Detect horizontal swipe to switch modes
        if abs(dx) > 100 and abs(dy) < 50:
            if dx > 0:  # Swipe right
                if self.current_mode == "calculator":
                    self.switch_to_graphing()
            else:  # Swipe left
                if self.current_mode == "graphing":
                    self.switch_to_calculator()
    
    def zoom_graph(self, factor):
        """Zoom the graph by a factor"""
        if hasattr(self, 'ax'):
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            
            x_center = (xlim[0] + xlim[1]) / 2
            y_center = (ylim[0] + ylim[1]) / 2
            
            x_range = (xlim[1] - xlim[0]) / factor
            y_range = (ylim[1] - ylim[0]) / factor
            
            self.ax.set_xlim(x_center - x_range/2, x_center + x_range/2)
            self.ax.set_ylim(y_center - y_range/2, y_center + y_range/2)
            
            self.canvas.draw()
    
    def key_press(self, event):
        """Handle keyboard input"""
        key = event.keysym
        
        if self.current_mode == "calculator":
            if key in ('Return', 'equal'):
                self.calculate()
            elif key in ('BackSpace',):
                self.backspace()
            elif key in ('Escape',):
                self.clear()
            elif key.lower() == 'c' and event.state & 0x4:  # Ctrl+C
                self.clear_all()
            elif key in ('plus', 'KP_Add'):
                self.show('+')
            elif key in ('minus', 'KP_Subtract'):
                self.show('-')
            elif key in ('asterisk', 'KP_Multiply'):
                self.show('*')
            elif key in ('slash', 'KP_Divide'):
                self.show('/')
            elif key == 'percent':
                self.show('%')
            elif key == 'period':
                self.show('.')
            elif key.isdigit():
                self.show(key)
            elif key in ('parenleft', 'parenright'):
                self.show('(' if key == 'parenleft' else ')')
    
    def run(self):
        """Start the application"""
        self.screen.mainloop()

# -------------------- MAIN EXECUTION --------------------
if __name__ == "__main__":
    app = FuturisticCalculator()
    app.run()