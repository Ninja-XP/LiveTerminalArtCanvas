# Live Terminal Art Canvas
[![Python](https://img.shields.io/static/v1?label=Python&message=3.x&color=blue&style=for-the-badge&logo=python)](https://www.python.org/) [![Version](https://img.shields.io/static/v1?label=Version&message=1.0&color=blue&style=for-the-badge&logo=appveyor)](https://github.com/Ninja-XP/LiveTerminalArtCanvas.git) [![Build](https://img.shields.io/static/v1?label=Build&message=Passing&color=success&style=for-the-badge&logo=github)](https://github.com/Ninja-XP/LiveTerminalArtCanvas/actions) [![Stars](https://img.shields.io/github/stars/craftingeagle/FFCompanion?color=yellow&style=for-the-badge&logo=github)](https://github.com/Ninja-XP/LiveTerminalArtCanvas/stargazers)
Welcome to **Live Terminal Art Canvas** — a fun and interactive terminal-based drawing application that lets you create art using your keyboard! With support for colors, animations, and saving/loading canvas states, this project brings creativity to your terminal.

![Canvas Screenshot]
![Screenshot_2024_1121_113010](https://github.com/user-attachments/assets/7aff2374-2fcf-44f8-96d3-2263b79e6d02)


## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Screenshots](#screenshots)
6. [Changelog](#changelog)
7. [Contributing](#contributing)
8. [Contact](#contact)

## Introduction

**Live Terminal Art Canvas** allows you to draw on a terminal canvas, interact with it using the keyboard, and see your creations come to life with animations. This project aims to provide a unique artistic experience in the terminal with the following features:
- Color support for drawing.
- Save and load your canvas state.
- Create animations like rain effects.
- Simple and responsive controls.

## Features

- **Drawing**: Move the cursor and draw symbols at any position on the canvas.
- **Color Support**: Change the drawing color with customizable options.
- **Animations**: Add dynamic rain effects to the canvas.
- **Save and Load**: Save your canvas artwork and reload it later to continue.
- **Cross-platform**: Works on Linux, MacOS, and Android (via Termux).

## Installation

### Termux (for Android)

1. Install Termux from [Google Play](https://play.google.com/store/apps/details?id=com.termux) or [F-Droid](https://f-droid.org/packages/com.termux/).

2. Update Termux packages:
   ```bash
   pkg update && pkg upgrade
   ```

3. Install Python and required dependencies:

   ```bash
   pkg install python3
   pip install -r requirements.txt
   ```


4. Clone the repository:

   ```bash
   git clone https://github.com/Ninja-Xp/LiveTerminalArtCanvas.git
   cd LiveTerminalArtCanvas
   ```


5. Run the application:

   ```bash
   ./scripts/run.sh
   ```

### Linux/MacOS

1. Clone the repository:

   ```bash
   git clone https://github.com/Ninja-Xp/LiveTerminalArtCanvas.git
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

Once the application is running, you can interact with the canvas using the following keyboard shortcuts:

- *`Arrow Keys`*: Move the cursor.

- *`Spacebar`*: Draw at the current cursor position.

- *`1, 2, 3, 4`*: Switch between colors (Red, Green, Blue, Yellow).

- *`C`*: Clear the canvas.

- *`S`*: Save the current canvas to a file.

- *`L`*: Load a previously saved canvas.

- *`R`*: Trigger the rain animation.

- *`Q`*: Quit the application.


## Screenshots

Here are some screenshots of the Live Terminal Art Canvas in action:

![Screenshot_2024_1121_112557](https://github.com/user-attachments/assets/52bfbb38-c40d-4455-aa62-d2a07b544cff)


- Use the arrow keys to move the cursor and press spacebar to draw.

![Screenshot_2024_1121_112909](https://github.com/user-attachments/assets/99bc3bac-835b-4ada-be6e-ba881a93f1c9)


- Change colors and draw your masterpiece!

## Changelog

For a detailed list of changes, features, and fixes, check the Changelog.

## Contributing

We welcome contributions to the project! If you'd like to help out, please follow these steps:

1. Fork the repository.


2. Create a feature branch (git checkout -b feature-branch).


3. Commit your changes (git commit -m "Add new feature").


4. Push to your forked repository (git push origin feature-branch).


5. Open a pull request to merge your changes.



For larger contributions, please open an issue first to discuss your changes.

## Contact

For any inquiries or support requests, feel free to reach out:

Gmail: reachninjaxp@gmail.com

GitHub: https://github.com/Ninja-Xp

Project Repository: https://github.com/Ninja-Xp/LiveTerminalArtCanvas
