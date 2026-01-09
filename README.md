# 🖱️ Clicker-Leveler

A simple and addictive clicker game built with Python's Tkinter GUI library. Click the button to increase your score and watch your "status" change as you progress. A perfect starter project for Python GUI learners.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## ✨ Features

*   **Click Counter:** Tracks every button press in real-time.
*   **Dynamic Leveling:** Your "level" title changes based on your click count.
*   **Lightweight & Fast:** A single-file application with no dependencies.
*   **Beginner-Friendly:** Clean, well-commented code perfect for learning Tkinter basics.

## 🚀 How to Run

1.  Ensure you have Python 3 installed on your system.
2.  Clone this repository:
    ```bash
    git clone https://github.com/your-username/clicker-leveler.git
    ```
3.  Navigate to the project folder:
    ```bash
    cd clicker-leveler
    ```
4.  Run the Python script:
    ```bash
    python clicker_game.py
    ```

## 📸 Screenshot

![Clicker-Leveler Screenshot](screenshot.png) *(You can add a screenshot later)*

## 🛠️ How It Works

The core logic is simple:
*   A global variable tracks the click count.
*   Each click triggers the `increment()` function.
*   The function updates the counter label and checks the count against thresholds to change the user's "level" label.
