import tkinter as tk

def tekan_tombol(nilai):
    teks_sekarang = layar_var.get()
    layar_var.set(teks_sekarang + str(nilai))

def hitung_hasil():
    try:
        hasil = str(eval(layar_var.get()))
        layar_var.set(hasil)
    except:
        layar_var.set("Error")

def hapus_layar():
    layar_var.set("")


# Buat jendela utama
window = tk.Tk()
window.title("Kalkulator")
window.geometry("400x500")
window.resizable(False, False)

# Buat layar input
layar_var = tk.StringVar()
layar = tk.Entry(window, textvariable=layar_var, font=("Arial", 20), justify="right", bd=10)
layar.pack(fill="both", ipadx=8, ipady=10, pady=10)

# Frame untuk tombol
frame_tombol = tk.Frame(window)
frame_tombol.pack()

# Susunan tombol kalkulator
tombol_list = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+'),
    ('%', '.')
]

# Buat tombol satu persatu
for baris, row in enumerate(tombol_list):
    for kolom, teks in enumerate(row):
        if teks == "=":
            tombol = tk.Button(frame_tombol, text=teks, width=5, height=2, command=hitung_hasil, font=('Arial', 18))
        elif teks == "C":
            tombol = tk.Button(frame_tombol, text=teks, width=5, height=2, command=hapus_layar, font=('Arial', 18))
        else:
            tombol = tk.Button(frame_tombol, text=teks, width=5, height=2, command=lambda t=teks: tekan_tombol(t), font=('Arial', 18))
        tombol.grid(row=baris, column=kolom, padx=5, pady=5)

window.mainloop()