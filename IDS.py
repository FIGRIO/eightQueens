import queue
import tkinter as tk

def an_toan(state, row, col):
    for r, c in enumerate(state):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True

def DBS(state, depth):
    if len(state) == 8:
        return [state]
    if depth > 0:
        solutions = []
        for col in range(8):
            if an_toan(state,len(state), col):
                result = DBS(state + [col], depth - 1)
                if result != None:
                    solutions += result
        return solutions
    return None

def IDS():
    solutions = []
    for depth in range(9):
        result = DBS([], depth)
        if result != None:
            solutions += result
    return solutions

def board():
    root = tk.Tk()
    root.title("8 Quân Hậu")
    root.geometry("1100x820+200+50")

    frame = tk.Frame(root)
    frame.pack()

    canvas = tk.Canvas(frame, width=800, height=800)
    canvas.pack(side="left")

    control = tk.Frame(frame)
    control.pack(side="right", fill="y", padx=20, pady=20)

    nghiem = IDS()
    chiso = len(nghiem)
    i = 0

    def ve():
        canvas.delete("all")
        for r in range(8):
            for c in range(8):
                color = "white" if (r + c) % 2 == 0 else "black"
                canvas.create_rectangle(
                    c*100, r*100, (c+1)*100, (r+1)*100, fill=color
                )

        sol = nghiem[i]
        for r, c in enumerate(sol):
            canvas.create_rectangle(
                c*100, r*100, (c+1)*100, (r+1)*100, fill="pink"
            )
        lbl.config(text=f"Nghiệm {i+1}/{len(nghiem)}")

    def next_sol():
        nonlocal i
        i += 1
        if i >= chiso:
            i = 0
        ve()

    btn = tk.Button(control, text="Kết quả tiếp theo", command=next_sol)
    btn.pack(pady=10)

    lbl = tk.Label(control, text="", font=("Arial", 12))
    lbl.pack()

    ve()
    root.mainloop()

if __name__ == "__main__":
    board()
