# Dobot Control Interface

This project provides a versatile interface for controlling a Dobot robotic arm, offering both a Command Line Interface (CLI) and a Graphical User Interface (GUI). It utilizes the `pydobot` library to communicate with the Dobot, allowing for operations such as moving to specific coordinates, returning to the home position, manipulating the tool attached to the Dobot, and querying the current position of the robotic arm.

## Folder Structure

```
DobotControl/
│
├── src/
│   └── dobot_control.py  # Main script for Dobot control
│
└── README.md
```

## Setup

1. **Install Dependencies**: Ensure Python 3 is installed on your system. Install the required Python package `pydobot` by running:

   ```
   pip install pydobot
   ```

2. **Connect Dobot**: Connect your Dobot robotic arm to your computer via USB.

3. **Adjust Port**: In `src/dobot_control.py`, adjust the `port` parameter in the `DobotController` initialization to match the port your Dobot is connected to.

## Usage

- **CLI Mode**: Run the script without arguments to use the CLI. Available commands include moving the Dobot, turning the tool on/off, and querying the current position.

  ```
  python src/dobot_control.py
  ```

- **GUI Mode**: Run the script with the `--gui` argument to launch the graphical user interface.

  ```
  python src/dobot_control.py --gui
  ```

## Features

- **Home**: Return the Dobot to its starting position.
- **Turn On/Off Tool**: Activate or deactivate the Dobot's tool.
- **Move**: Command the Dobot to move along the X, Y, or Z axis by a specified distance.
- **Current Position**: Display the current position of the Dobot.