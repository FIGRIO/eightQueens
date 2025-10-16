import tkinter as tk
import random
import math

def tinh_chi_phi(state):
    so_cap_tan_cong = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j) or state[i] == state[j]:
                so_cap_tan_cong += 1
    return so_cap_tan_cong

def simulated_annealing():
    nhiet_do = 1000.0
    alpha = 0.995

    trang_thai_hien_tai = [random.randint(0, 7) for _ in range(8)]

    while nhiet_do > 1e-5:
        chi_phi_hien_tai = tinh_chi_phi(trang_thai_hien_tai)

        if chi_phi_hien_tai == 0:
            return [trang_thai_hien_tai]

        col = random.randint(0, 7)
        new_row = random.randint(0, 7)
        trang_thai_lan_can = list(trang_thai_hien_tai)
        trang_thai_lan_can[col] = new_row

        chi_phi_moi = tinh_chi_phi(trang_thai_lan_can)

        delta_E = chi_phi_moi - chi_phi_hien_tai

        if delta_E < 0 or random.random() < math.exp(-delta_E / nhiet_do):
            trang_thai_hien_tai = trang_thai_lan_can

        nhiet_do *= alpha

    return []

def board():
    root = tk.Tk()
    root.title("8 Quân Hậu - Simulated Annealing")
    root.geometry("1100x820+200+50")

    frame = tk.Frame(root)
    frame.pack()

    canvas = tk.Canvas(frame, width=800, height=800)
    canvas.pack(side="left")

    control = tk.Frame(frame)
    control.pack(side="right", fill="y", padx=20, pady=20)

    nghiem = simulated_annealing()
    chiso = len(nghiem)
    i = 0

    def ve():
        canvas.delete("all")
        for r in range(8):
            for c in range(8):
                color = "white" if (r + c) % 2 == 0 else "black"
                canvas.create_rectangle(c*100, r*100, (c+1)*100, (r+1)*100, fill=color)

        if not nghiem:
            lbl.config(text="Không tìm thấy lời giải.\nHãy thử lại.")
            return

        sol = nghiem[0]
        for c, r in enumerate(sol):
            canvas.create_rectangle(c*100, r*100, (c+1)*100, (r+1)*100, fill="pink")
        lbl.config(text=f"Nghiệm {i+1}/{chiso}")

    def next_sol():
        nonlocal i
        nonlocal nghiem

        nghiem = simulated_annealing()
        chiso = len(nghiem)
        i = 0
        ve()

    btn = tk.Button(control, text="Thử lại", command=next_sol)
    btn.pack(pady=10)

    lbl = tk.Label(control, text="", font=("Arial", 12))
    lbl.pack()

    ve()

    root.mainloop()

if __name__ == "__main__":
    board()