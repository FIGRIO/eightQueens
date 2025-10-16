import heapq
import tkinter as tk
import math

def an_toan(state, row, col):
    for r, c in enumerate(state):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True

def distance_heuristic(parent_state, new_row, new_col):
    if not parent_state:
        return 0

    parent_row = len(parent_state) - 1
    parent_col = parent_state[-1]

    distance = math.sqrt(math.pow((new_row - parent_row), 2) + math.pow((new_col - parent_col), 2))
    return distance

def greedy_bfs_distance_multiple():
    Open = []
    initial_state = []
    heapq.heappush(Open, (0, initial_state))

    closed = set()
    solutions = []

    while Open:
        h_value, state = heapq.heappop(Open)

        if tuple(state) in closed:
            continue
        closed.add(tuple(state))

        if len(state) == 8:
            solutions.append(state)
            continue

        row = len(state)
        for col in range(8):
            if an_toan(state, row, col):
                new_state = state + [col]
                new_h = distance_heuristic(state, row, col)
                print(new_h)
                heapq.heappush(Open, (new_h, new_state))

    return solutions

def board():
    root = tk.Tk()
    root.title("8 Quân Hậu - Greedy Khoảng cách (Nhiều nghiệm)")
    root.geometry("1100x820+200+50")

    frame = tk.Frame(root)
    frame.pack()

    canvas = tk.Canvas(frame, width=800, height=800)
    canvas.pack(side="left")

    control = tk.Frame(frame)
    control.pack(side="right", fill="y", padx=20, pady=20)

    nghiem = greedy_bfs_distance_multiple()
    chiso = len(nghiem)
    i = 0

    def ve():
        canvas.delete("all")
        for r in range(8):
            for c in range(8):
                color = "white" if (r + c) % 2 == 0 else "black"
                canvas.create_rectangle(c*100, r*100, (c+1)*100, (r+1)*100, fill=color)
        
        if not nghiem:
            return

        sol = nghiem[i]
        for r, c in enumerate(sol):
            canvas.create_rectangle(c*100, r*100, (c+1)*100, (r+1)*100, fill="pink")
        lbl.config(text=f"Nghiệm {i+1}/{len(nghiem)}")

    def next_sol():
        nonlocal i
        if not nghiem:
            return
        i = (i + 1) % chiso
        ve()

    btn = tk.Button(control, text="Kết quả tiếp theo", command=next_sol)
    btn.pack(pady=10)

    lbl = tk.Label(control, text="", font=("Arial", 12))
    lbl.pack()

    if nghiem:
        ve()
    else:
        lbl.config(text="Không tìm thấy lời giải nào.")
        
    root.mainloop()

if __name__ == "__main__":
    board()