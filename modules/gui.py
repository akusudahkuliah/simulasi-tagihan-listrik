import tkinter as tk
from tkinter import ttk

from modules.config import *
from modules.billing import hitung_tagihan
from modules.database import load_data, simpan_data


def start_app():

    app = tk.Tk()

    app.title(APP_TITLE)
    app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    tk.Label(app,text="SIMULASI TAGIHAN LISTRIK",font=("Segoe UI",18,"bold")).grid(row=0,column=0,columnspan=2,pady=20)

    tk.Label(app,text="Nama").grid(row=1,column=0,padx=10,pady=5)

    nama_entry=tk.Entry(app,width=35)
    nama_entry.grid(row=1,column=1)

    tk.Label(app,text="Golongan").grid(row=2,column=0,padx=10,pady=5)

    golongan=ttk.Combobox(app,values=list(TARIF.keys()),state="readonly",width=32)
    golongan.current(1)
    golongan.grid(row=2,column=1)

    tk.Label(app,text="Pemakaian (kWh)").grid(row=3,column=0,padx=10,pady=5)

    kwh_entry=tk.Entry(app,width=35)
    kwh_entry.grid(row=3,column=1)

    hasil=tk.Label(app,text="Belum ada perhitungan",justify="left",font=("Consolas",11))
    hasil.grid(row=5,column=0,columnspan=2,pady=15)

    tk.Label(app,text="Riwayat Perhitungan",font=("Segoe UI",10,"bold")).grid(row=6,column=0,columnspan=2)

    riwayat=tk.Listbox(app,width=80,height=8)
    riwayat.grid(row=7,column=0,columnspan=2,pady=10)

    data=load_data()

    for item in data:
        riwayat.insert(
            tk.END,
            f"{item['nama']} | {item['golongan']} | {item['kwh']} kWh | Rp {item['total']:,.2f}"
        )

    def hitung():

        try:

            nama=nama_entry.get()

            kwh=float(kwh_entry.get())

            tarif=TARIF[golongan.get()]

            subtotal,ppn,total=hitung_tagihan(kwh,tarif)

            hasil.config(
                text=f"Subtotal : Rp {subtotal:,.2f}\nPPN : Rp {ppn:,.2f}\nTotal : Rp {total:,.2f}"
            )

            data.append({
                "nama":nama,
                "golongan":golongan.get(),
                "kwh":kwh,
                "total":total
            })

            simpan_data(data)

            riwayat.insert(
                tk.END,
                f"{nama} | {golongan.get()} | {kwh} kWh | Rp {total:,.2f}"
            )

        except:

            hasil.config(text="Input tidak valid!")

    def reset():

        nama_entry.delete(0,tk.END)
        kwh_entry.delete(0,tk.END)
        golongan.current(1)

    tk.Button(app,text="Hitung",width=15,command=hitung).grid(row=4,column=0,pady=10)

    tk.Button(app,text="Reset",width=15,command=reset).grid(row=4,column=1,pady=10)

    app.mainloop()