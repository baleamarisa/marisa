import tkinter as tk
from tkinter import ttk
import random
import time


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.geometry("1000x600")

        # Variables
        self.selected_algorithm = tk.StringVar(value="Bubble Sort")
        self.num_elements = tk.IntVar(value=50)
        self.speed = tk.DoubleVar(value=0.5)
        self.is_paused = False
        self.stop_sorting = False

        # Data array
        self.data = []

        # Setup UI
        self.setup_ui()
        self.generate_data()

    def setup_ui(self):
        """Setup the graphical user interface."""
        # Control panel
        control_frame = tk.Frame(self.root, padx=10, pady=10)
        control_frame.pack(fill=tk.X)

        # Algorithm selector
        tk.Label(control_frame, text="Algorithm:").pack(side=tk.LEFT, padx=5)
        algorithm_menu = ttk.Combobox(control_frame, textvariable=self.selected_algorithm,
                                      values=["Bubble Sort", "Insertion Sort", "Selection Sort", "Bogo Sort"],
                                      state="readonly")
        algorithm_menu.pack(side=tk.LEFT, padx=5)

        # Number of elements slider
        tk.Label(control_frame, text="Number of Elements:").pack(side=tk.LEFT, padx=5)
        tk.Scale(control_frame, from_=5, to=100, orient=tk.HORIZONTAL, variable=self.num_elements).pack(side=tk.LEFT)

        # Speed slider
        tk.Label(control_frame, text="Speed:").pack(side=tk.LEFT, padx=5)
        tk.Scale(control_frame, from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, variable=self.speed).pack(
            side=tk.LEFT)

        # Buttons
        tk.Button(control_frame, text="Randomize", command=self.generate_data).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Start", command=self.start_sorting).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Pause/Resume", command=self.toggle_pause).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Reset", command=self.generate_data).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Exit", command=self.root.quit).pack(side=tk.LEFT, padx=5)

        # Canvas for visualization
        self.canvas = tk.Canvas(self.root, bg="white", height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def generate_data(self):
        """Generate random data for sorting."""
        self.data = [random.randint(10, 400) for _ in range(self.num_elements.get())]
        self.draw_data()

    def draw_data(self, color_array=None):
        """Draw the data as bars on the canvas."""
        self.canvas.delete("all")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        bar_width = canvas_width / len(self.data)

        for i, value in enumerate(self.data):
            x0 = i * bar_width
            y0 = canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = canvas_height
            color = color_array[i] if color_array else "blue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

        self.root.update_idletasks()

    def start_sorting(self):

        self.stop_sorting = False
        algorithm = self.selected_algorithm.get()
        if algorithm == "Bubble Sort":
            self.bubble_sort()
        elif algorithm == "Insertion Sort":
            self.insertion_sort()
        elif algorithm == "Selection Sort":
            self.selection_sort()
        elif algorithm == "Bogo Sort":
            self.bogo_sort()

    def toggle_pause(self):

        self.is_paused = not self.is_paused

    def bubble_sort(self):

        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - i - 1):
                if self.stop_sorting:
                    return
                while self.is_paused:
                    time.sleep(0.1)
                self.draw_data(["red" if x == j or x == j + 1 else "blue" for x in range(len(self.data))])
                time.sleep(self.speed.get())
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        self.draw_data(["green" for _ in self.data])

    def insertion_sort(self):

        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                if self.stop_sorting:
                    return
                while self.is_paused:
                    time.sleep(0.1)
                self.data[j + 1] = self.data[j]
                j -= 1
                self.draw_data(["red" if x == j or x == i else "blue" for x in range(len(self.data))])
                time.sleep(self.speed.get())
            self.data[j + 1] = key
        self.draw_data(["green" for _ in self.data])

    def selection_sort(self):

        for i in range(len(self.data)):
            min_idx = i
            for j in range(i + 1, len(self.data)):
                if self.stop_sorting:
                    return
                while self.is_paused:
                    time.sleep(0.1)
                self.draw_data(["red" if x == j or x == min_idx else "blue" for x in range(len(self.data))])
                time.sleep(self.speed.get())
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
        self.draw_data(["green" for _ in self.data])

    def bogo_sort(self):
        """Perform Bogo Sort on the data (not efficient)."""
        while not self.is_sorted():
            if self.stop_sorting:
                return
            while self.is_paused:
                time.sleep(0.1)
            random.shuffle(self.data)
            self.draw_data(["red" for _ in self.data])
            time.sleep(self.speed.get())
        self.draw_data(["green" for _ in self.data])

    def is_sorted(self):

        return all(self.data[i] <= self.data[i + 1] for i in range(len(self.data) - 1))


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
