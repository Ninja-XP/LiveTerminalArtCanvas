# Developer Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Setup Instructions](#setup-instructions)
3. [Code Structure](#code-structure)
4. [Contributing](#contributing)
5. [Testing](#testing)
6. [Deployment](#deployment)

## Introduction

Welcome to the development guide for **Live Terminal Art Canvas**. This guide provides instructions for setting up your development environment, understanding the code structure, and contributing to the project.

## Setup Instructions

To begin developing, follow these steps to set up your local environment.

### Prerequisites
Ensure that you have the following installed:
- Python 3.6+
- Termux (for Android users)
- `curses` library (typically comes with Python in Termux)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LiveTerminalArtCanvas.git
   cd LiveTerminalArtCanvas
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:

   ```bash
   ./scripts/run.sh
   ```

### Code Structure

The project follows a modular structure, where functionality is divided into logical components.

```
LiveTerminalArtCanvas/
├── src/
│   ├── main.py            # Main entry point for the application
│   ├── core/
│   │   ├── input_handler.py  # Handles user input
│   │   ├── renderer.py       # Manages the display logic
│   │   ├── canvas.py         # Canvas management logic
│   └── utils/
│       ├── color.py          # Color management
│       └── animation.py      # Animation effects like rain
├── scripts/
│   ├── run.sh              # Shell script to start the application
└── README.md
```

### Key Components

`main.py`: The entry point to run the application.

`canvas.py`: Manages the drawing grid and coordinates.

`input_handler.py`: Processes user inputs and modifies the canvas.

`renderer.py`: Handles rendering the canvas to the terminal using curses.

### Contributing

We welcome contributions to the project! Please follow these guidelines when submitting code:

1. Fork the repository.


2. Create a feature branch: `git checkout -b feature-branch`.


3. Commit your changes: `git commit -m "Description of changes"``.


4. Push the changes to your forked repository: `git push origin feature-branch`.


5. Open a pull request to the main repository.



Please make sure that your code follows the PEP8 guidelines and includes adequate tests.



### Testing

To run the tests for this project:

1. Ensure the testing dependencies are installed:

   ```bash
   pip install -r requirements.txt
   ```


2. Run the tests:

   ```bash
   pytest
   ```


### Deployment

For deployment, ensure your environment matches the development setup, and run the application via the ./scripts/run.sh script.
