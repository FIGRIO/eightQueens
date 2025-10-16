import tkinter as tk

def an_toan(state, row, col):
    for r, c in enumerate(state):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True

def and_or_search():
    solutions = []
    
    def solve(state):
        # Nút AND
        if len(state) == 8:
            solutions.append(list(state))
            return

        current_row = len(state)
        
        # Nút OR
        for col in range(8):
            if an_toan(state, current_row, col):
                new_state = state + [col]
                solve(new_state)
    
    solve([])
    return solutions

def board():
    root = tk.Tk()
    root.title("8 Quân Hậu - AND-OR Search")
    root.geometry("1100x820+200+50")

    frame = tk.Frame(root)
    frame.pack()

    canvas = tk.Canvas(frame, width=800, height=800)
    canvas.pack(side="left")

    control = tk.Frame(frame)
    control.pack(side="right", fill="y", padx=20, pady=20)

    nghiem = and_or_search()
    chiso = len(nghiem)
    i = 0

    def ve():
        canvas.delete("all")
        for r in range(8):
            for c in range(8):
                color = "white" if (r + c) % 2 == 0 else "black"
                canvas.create_rectangle(c*100, r*100, (c+1)*100, (r+1)*100, fill=color)
        
        if not nghiem:
            lbl.config(text="Không tìm thấy lời giải nào.")
            return

        sol = nghiem[i]
        for r, c in enumerate(sol):
            canvas.create_rectangle(c*100, r*100, (c+1)*100, (r+1)*100, fill="pink")
        lbl.config(text=f"Nghiệm {i+1}/{chiso}")

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