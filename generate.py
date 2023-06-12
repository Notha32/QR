import qrcode
from qrcode import ERROR_CORRECT_L
from tkinter import *
from tkinter import filedialog
import tkinter as tk

window = tk.Tk()
window.title("QR 1.0")
window.geometry("500x300")
window.resizable(height=False, width=False)

var = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()

var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()

var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()

photo = None


def generateqrcode():
    global img
    if var.get() or var2.get() or var3.get() or var4.get() or var5.get() or var6.get():
        a = lien.get()
        b = name.get()
        if var.get() == 1:
            color = "blue"
        if var2.get() == 1:
            color = "yellow"
        if var3.get() == 1:
            color = "black"
        if var4.get() == 1:
            color = "purple"
        if var5.get():
            color = "red"
        if var6.get():
            color = "green"

    if var7.get() or var8.get() or var9.get() or var10.get() or var11.get() or var12.get():
        a = lien.get()
        b = name.get()
        if var7.get() == 1:
            version1 = "5"
        if var8.get() == 1:
            version1 = "10"
        if var9.get() == 1:
            version1 = "15"
        if var10.get() == 1:
            version1 = "20"
        if var11.get():
            version1 = "25"
        if var12.get():
            version1 = "30"

    if var13.get() or var14.get() or var15.get() or var16.get() or var17.get() or var18.get():
        a = lien.get()
        b = name.get()
        if var13.get() == 1:
            color1 = "blue"
        if var14.get() == 1:
            color1 = "yellow"
        if var15.get() == 1:
            color1 = "black"
        if var16.get() == 1:
            color1 = "purple"
        if var17.get():
            color1 = "red"
        if var18.get():
            color1 = "green"
        
        qr = qrcode.QRCode(
            version = version1,
            error_correction=ERROR_CORRECT_L,
            box_size=3,
            border=5
        )

        qr.add_data(a)
        qr.make(fit=True)

        img = qr.make_image(fill_color=color, back_color=color1)
        file_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile=b, filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg;*.jpeg")])
        if file_path:
            img.save(file_path)

    else:
        a = lien.get()
        b = name.get()
        qr = qrcode.QRCode(
            version = 3,
            error_correction=ERROR_CORRECT_L,
            box_size=3,
            border=5
        )

        qr.add_data(a)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg;*.jpeg")])
        if file_path:
            img.save(file_path)

def color2():
    couleur = Label(window, text=('Color'), font=("Calibri", 10))
    couleur.place(x=20, y=80)

    check = Checkbutton(window, text=("blue"), variable=var)
    check.place(x=15, y=110)

    check1 = Checkbutton(window, text=("yellow"), variable=var2)
    check1.place(x=15, y=130)

    check2 = Checkbutton(window, text=("black"), variable=var3)
    check2.place(x=15, y=150)

    check3 = Checkbutton(window, text=("purple"), variable=var4)
    check3.place(x=15, y=170)

    check4 = Checkbutton(window, text=("red"), variable=var5)
    check4.place(x=15, y=190)

    check5 = Checkbutton(window, text=("green"), variable=var6)
    check5.place(x=15, y=210)

def carre():
    border = Label(window, text=('Size'), font=("Calibri", 10))
    border.place(x=205, y=80)

    check = Checkbutton(window, text=("5"), variable=var7)
    check.place(x=205, y=110)

    check1 = Checkbutton(window, text=("10"), variable=var8)
    check1.place(x=205, y=130)

    check2 = Checkbutton(window, text=("15"), variable=var9)
    check2.place(x=205, y=150)

    check3 = Checkbutton(window, text=("20"), variable=var10)
    check3.place(x=205, y=170)

    check4 = Checkbutton(window, text=("25"), variable=var11)
    check4.place(x=205, y=190)

    check5 = Checkbutton(window, text=("30"), variable=var12)
    check5.place(x=205, y=210)

def backcolor():
    border3 = Label(window, text=('Backcolor'), font=("Calibri", 10))
    border3.place(x=400, y=80)

    check = Checkbutton(window, text=("blue"), variable=var13)
    check.place(x=400, y=110)

    check1 = Checkbutton(window, text=("yellow"), variable=var14)
    check1.place(x=400, y=130)

    check2 = Checkbutton(window, text=("black"), variable=var15)
    check2.place(x=400, y=150)

    check3 = Checkbutton(window, text=("purple"), variable=var16)
    check3.place(x=400, y=170)

    check4 = Checkbutton(window, text=("red"), variable=var17)
    check4.place(x=400, y=190)

    check5 = Checkbutton(window, text=("green"), variable=var18)
    check5.place(x=400, y=210)

texte1 = Label(window, text=("Link :"), font=("Calibri", 10))
texte1.place(x=0, y= 12)

lien = Entry(window, font=("Calibri", 10))
lien.place(x=90, y=10, height=20, width=400)

texte2 = Label(window, text=("file name :"), font=("Calibri", 10))
texte2.place(x=0, y=37)

name = Entry(window, font=("Calibri", 10))
name.place(x=90, y=42, height=20, width=400)

generate2 = Button(window, text=("Generate and Download QRcode in specific path"), font=("Calibri", 10), command=generateqrcode)
generate2.place(x=15, y=247, height=50, width=470)

color2()
carre()
backcolor()

window.mainloop()
