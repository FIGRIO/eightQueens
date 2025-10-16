import heapq
import tkinter as tk
import math

def an_toan(state, row, col):
    for r, c in enumerate(state):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True

def gn(state, row, col):
    if not state:
        return 0
    
    prev_row = len(state) - 1
    prev_col = state[-1]
    
    distance = math.sqrt(math.pow((row - prev_row), 2) + math.pow((col - prev_col), 2))
    return distance

def heuristic(state):
    return 8 - len(state)

def A_star():
    Open = []
    # (f_cost, g_cost, state)
    heapq.heappush(Open, (0 + 8, 0, []))
    solutions = []
    closed = set()

    while Open:
        f_cost, g_cost, state = heapq.heappop(Open)

        if tuple(state) in closed:
            continue
        closed.add(tuple(state))
        
        if len(state) == 8:
            solutions.append((g_cost, state))
            continue
            
        current_row = len(state)
        for col in range(8):
            if an_toan(state, current_row, col):
                
                step_cost = gn(state, current_row, col)
                new_g = g_cost + step_cost
                new_h = heuristic(state + [col])
                new_f = new_g + new_h
                
                new_state = state + [col]
                heapq.heappush(Open, (new_f, new_g, new_state))
                
    return solutions

def board():
    root = tk.Tk()
    root.title("8 Quân Hậu - A* Search")
    root.geometry("1100x820+200+50")

    frame = tk.Frame(root)
    frame.pack()

    canvas = tk.Canvas(frame, width=800, height=800)
    canvas.pack(side="left")

    control = tk.Frame(frame)
    control.pack(side="right", fill="y", padx=20, pady=20)

    nghiem_data = A_star()
    if nghiem_data:
        nghiem_data.sort(key=lambda x: x[0])
        nghiem = [sol[1] for sol in nghiem_data]
    else:
        nghiem = []

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