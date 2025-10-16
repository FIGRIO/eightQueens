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

def beam_search(beta):
    Open = [[]] 
    
    for row in range(8):
        tat_ca_con = []
        for state in Open:
            for col in range(8):
                if an_toan(state, row, col):
                    child_state = state + [col]
                    heuristic_value = distance_heuristic(state, row, col)
                    tat_ca_con.append((heuristic_value, child_state))
        
        if not tat_ca_con:
            return []

        tat_ca_con.sort(key=lambda x: x[0])
        
        Open = [state for h, state in tat_ca_con[:beta]]

    solutions = [state for state in Open if len(state) == 8]
    return solutions

def board():
    root = tk.Tk()
    root.title("8 Quân Hậu - Beam Search (Khoảng cách)")
    root.geometry("1100x820+200+50")

    frame = tk.Frame(root)
    frame.pack()

    canvas = tk.Canvas(frame, width=800, height=800)
    canvas.pack(side="left")

    control = tk.Frame(frame)
    control.pack(side="right", fill="y", padx=20, pady=20)
    
    BEAM_WIDTH = 200
    nghiem = beam_search(BEAM_WIDTH)
    chiso = len(nghiem)
    i = 0

    def ve():
        canvas.delete("all")
        for r in range(8):
            for c in range(8):
                color = "white" if (r + c) % 2 == 0 else "black"
                canvas.create_rectangle(c*100, r*100, (c+1)*100, (r+1)*100, fill=color)
        
        if not nghiem:
            lbl.config(text=f"Không tìm thấy lời giải với Beam width = {BEAM_WIDTH}")
            return

        sol = nghiem[i]
        for r, c in enumerate(sol):
            canvas.create_rectangle(c*100, r*100, (c+1)*100, (r+1)*100, fill="pink")
        lbl.config(text=f"Nghiệm {i+1}/{chiso}\n(Beam width = {BEAM_WIDTH})")

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
    
    ve()
        
    root.mainloop()

if __name__ == "__main__":
    board()