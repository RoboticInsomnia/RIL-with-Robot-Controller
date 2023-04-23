
import tkinter as tk

class RobotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Robotic Insomnia V.1")
        master.config(bg="black")

        # Create labels
        self.direction_label = tk.Label(master, text="Direction:", font=("Arial", 20, "bold"), fg="white", bg="black")
        self.speed_label = tk.Label(master, text="Speed:", font=("Arial", 20, "bold"), fg="white", bg="black")
        self.status_label = tk.Label(master, text="Status: Disconnected", font=("Arial", 20, "bold"), fg="white", bg="black")

        # Create entry fields
        self.direction_entry = tk.Entry(master, font=("Arial", 20), bd=0)
        self.speed_entry = tk.Entry(master, font=("Arial", 20), bd=0)

        # Create buttons
        self.connect_button = tk.Button(master, text="Connect", font=("Arial", 20), fg="white", bg="#333", command=self.connect)
        self.disconnect_button = tk.Button(master, text="Disconnect", font=("Arial", 20), fg="white", bg="#333", command=self.disconnect)
        self.forward_button = tk.Button(master, text="Forward", font=("Arial", 20), fg="white", bg="#333", command=self.forward)
        self.backward_button = tk.Button(master, text="Backward", font=("Arial", 20), fg="white", bg="#333", command=self.backward)
        self.left_button = tk.Button(master, text="Left", font=("Arial", 20), fg="white", bg="#333", command=self.left)
        self.right_button = tk.Button(master, text="Right", font=("Arial", 20), fg="white", bg="#333", command=self.right)
        self.stop_button = tk.Button(master, text="Stop", font=("Arial", 20), fg="white", bg="#333", command=self.stop)

        # Set layout
        self.direction_label.grid(row=0, column=0, padx=10, pady=10)
        self.direction_entry.grid(row=0, column=1, padx=10, pady=10)
        self.speed_label.grid(row=1, column=0, padx=10, pady=10)
        self.speed_entry.grid(row=1, column=1, padx=10, pady=10)
        self.connect_button.grid(row=2, column=0, pady=10)
        self.disconnect_button.grid(row=2, column=1, pady=10)
        self.status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.forward_button.grid(row=4, column=0, padx=10, pady=10)
        self.backward_button.grid(row=4, column=1, padx=10, pady=10)
        self.left_button.grid(row=5, column=0, padx=10, pady=10)
        self.right_button.grid(row=5, column=1, padx=10, pady=10)
        self.stop_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def connect(self):
        self.status_label.config(text="Status: Connected")

    def disconnect(self):
        self.status_label.config(text="Status: Disconnected")

    def forward(self):
        direction = self.direction_entry.get()
        speed = self.speed_entry.get()
        print(f"Moving {direction} at speed {speed}")

    def backward(self):
        direction = self.direction_entry.get()
        speed = self.speed_entry.get()
        print(f"Moving {direction} backwards at speed {speed}")

    def left(self):
        print("Turning left")

    def right(self):
        print("Turning right")

    def stop(self):
        print("Stopping")


if __name__ == '__main__':
    root = tk.Tk()
    gui = RobotGUI(root)
    root.mainloop()