import tkinter as tk

class LightGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Smart Light Control")

        self.status = True
        self.running = True

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.light_button = tk.Button(
            self.root,
            text="LIGHT ON",
            font=("Arial",20),
            width=20,
            height=3,
            bg="green",
            # command=self.toggle
        )
        self.light_button.pack(pady=10)

        self.stop_button = tk.Button(
            self.frame,
            text="STOP DETECTION",
            font=("Arial",16),
            width=20,
            height=2,
            bg="orange",
            command=self.stop_detection
        )
        self.stop_button.pack(pady=10)

        # self.root.protocol("WM_DELETE_WINDOW", self.stop_detection)

    def stop_detection(self):
        self.running = False
        print("Detection Stopped")

    def toggle(self):

        self.status = not self.status

        if self.status:
            self.light_button.config(text="LIGHT ON", bg="green")
        else:
            self.light_button.config(text="LIGHT OFF", bg="red")

    def light_on(self):

        self.status=True
        self.light_button.config(text="LIGHT ON", bg="green")

    def light_off(self):

        self.status=False
        self.light_button.config(text="LIGHT OFF", bg="red")

    def run(self):
        self.root.mainloop()