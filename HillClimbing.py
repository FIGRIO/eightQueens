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

def hill_climbing():
    trang_thai_hien_tai = [random.randint(0, 7) for _ in range(8)]
    
    while True:
        chi_phi_hien_tai = tinh_chi_phi(trang_thai_hien_tai)

        if chi_phi_hien_tai == 0:
            return [trang_thai_hien_tai]

        chi_phi_tot_nhat = chi_phi_hien_tai
        trang_thai_tot_nhat_tiep_theo = list(trang_thai_hien_tai)

        for col in range(8):
            vi_tri_goc = trang_thai_hien_tai[col]
            for row in range(8):
                if trang_thai_hien_tai[col] == row:
                    continue
                
                trang_thai_lan_can = list(trang_thai_hien_tai)
                trang_thai_lan_can[col] = row
                chi_phi_moi = tinh_chi_phi(trang_thai_lan_can)
                
                if chi_phi_moi < chi_phi_tot_nhat:
                    chi_phi_tot_nhat = chi_phi_moi
                    trang_thai_tot_nhat_tiep_theo = trang_thai_lan_can
        
        if chi_phi_tot_nhat >= chi_phi_hien_tai:
            return [] 
            
        trang_thai_hien_tai = trang_thai_tot_nhat_tiep_theo

def board():
    root = tk.Tk()
    root.title("8 Quân Hậu - Hill Climbing ")
    root.geometry("1100x820+200+50")

    frame = tk.Frame(root)
    frame.pack()

    canvas = tk.Canvas(frame, width=800, height=800)
    canvas.pack(side="left")

    control = tk.Frame(frame)
    control.pack(side="right", fill="y", padx=20, pady=20)

    nghiem = hill_climbing()
    chiso = len(nghiem)
    i = 0

    def ve():
        canvas.delete("all")
        for r in range(8):
            for c in range(8):
                color = "white" if (r + c) % 2 == 0 else "black"
                canvas.create_rectangle(c*100, r*100, (c+1)*100, (r+1)*100, fill=color)

        if not nghiem:
            lbl.config(text="Không tìm thấy lời giải (bị kẹt).\nHãy thử lại.")
            return

        sol = nghiem[0]
        for c, r in enumerate(sol):
            canvas.create_rectangle(c*100, r*100, (c+1)*100, (r+1)*100, fill="pink")
        lbl.config(text=f"Nghiệm {i+1}/{chiso}")

    def next_sol():
        nonlocal i
        nonlocal nghiem

        nghiem = hill_climbing()
        chiso = len(nghiem)
        i = 0
        ve()

    btn = tk.Button(control, text="Thử lại với trạng thái khác", command=next_sol)
    btn.pack(pady=10)

    lbl = tk.Label(control, text="", font=("Arial", 12))
    lbl.pack()
    
    ve()
        
    root.mainloop()

if __name__ == "__main__":
    board()