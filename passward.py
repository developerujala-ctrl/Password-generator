import tkinter as tk
import random
import string

root=tk.Tk()
root.title("python GUI Calculator")
root.geometry("700x900")
root.config(bg="white")

length_var=tk.IntVar()

def password_generator():
    character=string.ascii_letters+string.digits+"!&%^$@"
    password=""
    for i in range(length_var.get()):
        password += random.choice(character)
    result.config(text=f"{password}")
    
    
heading=tk.Label(root,text="Create a strong password",font=("Calibri",25),bg="white",fg="black")
heading.place(x=20,y=90)

heading2=tk.Label(root,text="Password length",font=("Calibri",20),bg="white",fg="darkblue")
heading2.place(x=20,y=160)  

length=tk.Entry(root,textvariable=length_var,font=("Calibri",40),bg="white",fg="blue")
length.place(x=20,y=220)

line=tk.Label(root,text="Iclude letter, number &symbole",font=("Calibri",16),bg="white",fg="darkblue")
line.place(x=20,y=290)  

pasword_gen=tk.Button(root,text="password Generator",font=("Calibri",20),bg="blue",fg="black",command=lambda:password_generator())
pasword_gen.place(x=20,y=340)

length_var=tk.Spinbox(root,font=("Calibri",40),bg="white",fg="blue")
length_var.place(x=20,y=420)


pasword_gen=tk.Button(root,text="Copy to Clipboard",font=("Calibri",20),bg="blue",fg="black")
pasword_gen.place(x=20,y=540)

result=tk.Label(root,text="                         ",font=("calibri",36))
result.place(x=22,y=420)







root.mainloop()