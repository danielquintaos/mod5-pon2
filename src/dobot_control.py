import sys
import platform
import tkinter as tk
from tkinter import simpledialog, messagebox
from pydobot import Dobot


class DobotController:
    def __init__(self, port='COM7'):  # Adjust the port to match your system
        self.device = Dobot(port=port)

    def move_to_position(self, x, y, z, r):
        self.device.move_to(x, y, z, r, wait=True)

    def home(self):
        self.device.go_home()

    def turn_on_tool(self):
        self.device.suck(True)

    def turn_off_tool(self):
        self.device.suck(False)

    def move_axis(self, axis, distance):
        x, y, z, r = self.device.pose()
        if axis == 'x':
            self.move_to_position(x + distance, y, z, r)
        elif axis == 'y':
            self.move_to_position(x, y + distance, z, r)
        elif axis == 'z':
            self.move_to_position(x, y, z + distance, r)

    def get_current_position(self):
        position = self.device.pose()
        return f"X={position[0]}, Y={position[1]}, Z={position[2]}, R={position[3]}"

    def close(self):
        self.device.close()


class DobotGUI:
    def __init__(self, master, controller):
        self.controller = controller
        self.master = master
        master.title("Dobot Control Panel")

        tk.Button(master, text="Home", command=self.controller.home).pack()
        tk.Button(master, text="Turn On Tool", command=self.controller.turn_on_tool).pack()
        tk.Button(master, text="Turn Off Tool", command=self.controller.turn_off_tool).pack()

        self.move_button = tk.Button(master, text="Move", command=self.move)
        self.move_button.pack()

        self.position_button = tk.Button(master, text="Current Position", command=self.current_position)
        self.position_button.pack()

    def move(self):
        axis = simpledialog.askstring("Input", "Enter axis (x, y, z):")
        distance = simpledialog.askfloat("Input", "Enter distance:")
        if axis and distance is not None:
            self.controller.move_axis(axis, distance)

    def current_position(self):
        position = self.controller.get_current_position()
        messagebox.showinfo("Current Position", position)

    def close(self):
        self.controller.close()
        self.master.quit()


def run_cli(controller):
    while True:
        command = input("Enter command: ")
        if command == "home":
            controller.home()
        elif command == "ligar ferramenta":
            controller.turn_on_tool()
        elif command == "desligar ferramenta":
            controller.turn_off_tool()
        elif command.startswith("mover"):
            _, axis, distance = command.split()
            controller.move_axis(axis, float(distance))
        elif command == "atual":
            print(controller.get_current_position())
        else:
            print("Unknown command. Please try again.")


def main():
    if platform.system() == 'Windows':
        port = 'COM7'  # Example for Windows, adjust as necessary
    else:
        port = '/dev/ttyUSB0'
    controller = DobotController(port='/dev/ttyUSB0')  # Adjust the port to match your system
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        root = tk.Tk()
        gui = DobotGUI(root, controller)
        root.protocol("WM_DELETE_WINDOW", gui.close)
        root.mainloop()
    else:
        try:
            run_cli(controller)
        except KeyboardInterrupt:
            print("\nExiting...")
        finally:
            controller.close()


if __name__ == "__main__":
    main()