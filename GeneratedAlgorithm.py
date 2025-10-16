import tkinter as tk
import random

def tinh_chi_phi(state):
    so_cap_tan_cong = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j) or state[i] == state[j]:
                so_cap_tan_cong += 1
    return so_cap_tan_cong

def genetic_algorithm(kich_thuoc_quan_the, so_the_he_toi_da):
    quan_the = [[random.randint(0, 7) for _ in range(8)] for _ in range(kich_thuoc_quan_the)]

    for the_he in range(so_the_he_toi_da):
        quan_the_moi = []

        quan_the_da_danh_gia = sorted([(tinh_chi_phi(ca_the), ca_the) for ca_the in quan_the])

        for chi_phi, ca_the in quan_the_da_danh_gia:
            if chi_phi == 0:
                return [ca_the]

        cha_me = [ca_the for chi_phi, ca_the in quan_the_da_danh_gia[:int(kich_thuoc_quan_the / 2)]]

        while len(quan_the_moi) < kich_thuoc_quan_the:
            cha = random.choice(cha_me)
            me = random.choice(cha_me)
            diem_lai_ghep = random.randint(1, 6)

            con = cha[:diem_lai_ghep] + me[diem_lai_ghep:]

            if random.random() < 0.1:
                vi_tri_dot_bien = random.randint(0, 7)
                gia_tri_moi = random.randint(0, 7)
                con[vi_tri_dot_bien] = gia_tri_moi

            quan_the_moi.append(con)

        quan_the = quan_the_moi

    return []

def board():
    root = tk.Tk()
    root.title("8 Quân Hậu - Genetic Algorithm")
    root.geometry("1100x820+200+50")

    frame = tk.Frame(root)
    frame.pack()

    canvas = tk.Canvas(frame, width=800, height=800)
    canvas.pack(side="left")

    control = tk.Frame(frame)
    control.pack(side="right", fill="y", padx=20, pady=20)

    nghiem = genetic_algorithm(100, 1000)
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
        
        nghiem = genetic_algorithm(100, 1000)
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