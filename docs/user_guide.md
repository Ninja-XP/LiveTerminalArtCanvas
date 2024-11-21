## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Keyboard Shortcuts](#keyboard-shortcuts)
5. [Troubleshooting](#troubleshooting)

## Introduction

Welcome to the **Live Terminal Art Canvas** user guide! This application allows you to draw art on a terminal canvas, customize it with colors, and even create animations. It’s designed to provide an interactive and engaging way to create art directly in your terminal.

## Installation

### Termux (for Android)
1. Install Termux from the Play Store or F-Droid.
2. Update Termux packages:
   ```bash
   pkg update
   ```

3. Install Python 3 and dependencies:

   ```bash
   pkg install python3
   pip install -r requirements.txt
   ```


4. Clone the repository:

   ```bash
   git clone https://github.com/Ninja-XP/LiveTerminalArtCanvas.git
   cd LiveTerminalArtCanvas
   ```


5. Run the application:

   ```bash
   ./scripts/run.sh
   ```



## Linux/MacOS

1. Clone the repository:

   ```bash
   git clone https://github.com/Ninja-XP/LiveTerminalArtCanvas.git
   cd LiveTerminalArtCanvas
   ```


2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```


3. Run the application:

   ```bash
   ./scripts/run.sh
   ```


## Usage

Upon launching the application, you will see a blank canvas in the terminal. You can move the cursor and start drawing.

## Keyboard Shortcuts

*`Arrow Keys`*: Move the cursor around the canvas.

*`Spacebar`*: Draw at the current cursor position.

*`1, 2, 3, 4`*: Switch to different colors (Red, Green, Blue, Yellow).

*`C`*: Clear the canvas and reset the state.

*`S`*: Save the current canvas to a file.

*`L`*: Load a previously saved canvas.

*`R`*: Activate the rain animation effect.

*`Q`*: Quit the application.


## Troubleshooting

###  No Colors Displaying

If colors aren't showing correctly, ensure that your terminal supports colors. If you're using Termux, make sure curses is working correctly by testing simple color programs.

###  Cursor Not Moving

Ensure that your input handling (Arrow Keys) is correctly configured. If there are issues with the input, check the keyboard configurations for Termux or your terminal.

If issues persist, feel free to open an issue on the repository’s GitHub page.
