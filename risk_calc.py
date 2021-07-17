import tkinter
from tkinter import *

root = Tk()
root.title("Risk Size Calculator")
root.geometry("500x400")

def Calculation():
    tpv = float(tpventry.get())
    cp = float(cpentry.get())
    sp = float(spentry.get())
    wtr = float(wtrentry.get())
    pos_size_in_asset = (tpv*wtr)/(cp-sp)
    pos_size = pos_size_in_asset*cp
    
    Label(text=f"{pos_size_in_asset}", font="arial 15 bold").place(x=250,y=220)
    Label(text=f"{pos_size}", font="arial 15 bold").place(x=250,y=250)

sub1=Label(root, text="Total Portfolio Value:", font="arial 10")
sub2=Label(root, text="Current Price:", font="arial 10")
sub3=Label(root, text="Stop Price:", font="arial 10")
sub4=Label(root, text="Willing to Risk:", font="arial 10")
output=Label(root, text="Size (USD):", font="arial 10")
output2=Label(root, text="Size (Asset):", font="arial 10")

sub1.place(x=50, y=20)
sub2.place(x=50, y=70)
sub3.place(x=50, y=120)
sub4.place(x=50, y=170)
output.place(x=50, y=250)
output2.place(x=50, y=220)

tpv_value=StringVar()
cp_value=StringVar()
sp_value=StringVar()
wtr_value=StringVar()

tpventry=Entry(root, textvariable=tpv_value, font="arial 15", width=15)
cpentry=Entry(root, textvariable=cp_value, font="arial 15", width=15)
spentry=Entry(root, textvariable=sp_value, font="arial 15", width=15)
wtrentry=Entry(root, textvariable=wtr_value, font="arial 15", width=15)

tpventry.place(x=250,y=20)
cpentry.place(x=250,y=70)
spentry.place(x=250,y=120)
wtrentry.place(x=250,y=170)

Button(text="Calculate", font="arial 15", bg="white",bd=10, command=Calculation).place(x=50,y=300)
Button(text="Exit", font="arial 15", bg="white",bd=10, width=8, command=lambda:exit()).place(x=350,y=300)


root.mainloop()
