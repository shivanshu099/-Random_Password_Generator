from tkinter import font
from ttkbootstrap import*
import ttkbootstrap as tb
import random
import pyperclip

def genrat(num):
     pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
     paord=""
     for x in range(num):
           paord+=random.choice(pass1)
           pyperclip.copy(paord)
     return paord


def pri():
      lbl.config(text="\npassword :- "+genrat(12))

root=tb.Window(themename="cyborg")
name_var=tk.IntVar()
root.title('password_genrator')
root.geometry('300x300')
root.minsize(300,300)
root.maxsize(300,300)
my_label=tb.Label(text="password_gen",font=("Comic Sans MS",20))
my_label.pack(pady=20)
my_button=tb.Button(text="genrate",bootstyle="danger,outline",command=pri)
my_button.pack(pady=(10,1))
lbl = tk.Label(text = "",font=("Helvetica",10)) 
lbl.pack(pady=18)
#print(font.families())
root.mainloop()

#print(f"password is ",genrat(12)) 

"""
tk special fonts
Jokerman
Lucida Calligraphy
Comic Sans MS
"""    