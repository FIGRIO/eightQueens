#giao diện 8 quân hậu tkinker
import tkinter as tk
def board():
    root = tk.Tk()
    root.title("8 Quân Hậu")
    root.geometry(f"{800}x{800}+{450}+{50}")
    canvas = tk.Canvas(root, width=800, height=800)
    canvas.pack()
    for i in range(8):
        for j in range(8):
            color = "white" if (i + j) % 2 == 0 else "black"
            canvas.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill=color)
    queens = [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)]
    for (i, j) in queens:
        canvas.create_rectangle(j * 100 , i * 100 , (j + 1) * 100 , (i + 1) * 100, fill="pink")
    root.mainloop()
if __name__ == "__main__":
    board()