#!/usr/bin/env python3
"""
Mobile Test Script for Futuristic Calculator
This script simulates mobile screen dimensions to test mobile optimizations
"""

import tkinter as tk
import os
import sys

# Add the current directory to path to import calculator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import FuturisticCalculator

class MobileSimulator:
    def __init__(self):
        # Create a test window to simulate mobile screen
        self.test_window = tk.Tk()
        self.test_window.title("Mobile Calculator Test")
        
        # Simulate mobile screen dimensions
        mobile_width = 400
        mobile_height = 700
        
        # Override screen dimensions for testing
        original_screenwidth = self.test_window.winfo_screenwidth
        original_screenheight = self.test_window.winfo_screenheight
        
        self.test_window.winfo_screenwidth = lambda: mobile_width
        self.test_window.winfo_screenheight = lambda: mobile_height
        
        # Create calculator with mobile dimensions
        self.calculator = FuturisticCalculator()
        
        # Restore original methods
        self.test_window.winfo_screenwidth = original_screenwidth
        self.test_window.winfo_screenheight = original_screenheight
        
        # Close test window
        self.test_window.destroy()
        
        print("Mobile Calculator Test Started!")
        print("Features:")
        print("- Touch-optimized buttons")
        print("- Larger fonts for mobile")
        print("- Simplified layout")
        print("- Swipe gestures (swipe left/right to switch modes)")
        print("- No emojis (Pydroid 3 compatible)")
        print("- Responsive design")
        
        # Run the calculator
        self.calculator.run()

if __name__ == "__main__":
    MobileSimulator()