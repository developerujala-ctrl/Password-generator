import tkinter as tk
root=tk.Tk()
root.title("python GUI Calculator")
root.geometry("600x800")
root.config(bg="white")
r=""
def Onclick(x):
        global r
        match(x):
            case"1":
                r += "1"
                result.config(text=f"{r}")
            case"2":
                r += "2"
                result.config(text=f"{r}")
            case"3":
                r += "3"
                result.config(text=f"{r}")
            case"4":
                r += "4"
                result.config(text=f"{r}")
            case"5":
                r += "5"
                result.config(text=f"{r}")
            case"6":
                r += "6"
                result.config(text=f"{r}")
            case"7":
                r += "7"
                result.config(text=f"{r}")
            case"8":
                r += "8"
                result.config(text=f"{r}")
            case"9":
                r += "9"
                result.config(text=f"{r}")
            case"0":
                r += "0"
                result.config(text=f"{r}")
            case"+":
                r += "+"
                result.config(text=f"{r}")
            case"-":
                r += "-"
                result.config(text=f"{r}")
            case"*":
                r += "*"
                result.config(text=f"{r}")
            case"/":
                r += "/"
                result.config(text=f"{r}")
            case"=":
                result.config(text=f"{eval(r)}")
            case"c":
                r = ""
                result.config(text="                               ")

heading=tk.Label(root,text="Python GUI clculator",font=("Arial",30),bg="pink",fg="white")
heading.pack(pady=24)

result=tk.Label(root,text="                                ",font=("Arial",37),bg="pink")
result.pack(pady=24)

btn1=tk.Button(root,text=" 7 ",font=("Arial",30), bg="pink",command=lambda:Onclick("7"))
btn1.place(x=40,y=200)

btn2=tk.Button(root,text=" 8 ",font=("Arial",30), bg="pink",command=lambda:Onclick("8"))
btn2.place(x=160,y=200)

btn3=tk.Button(root,text=" 9 ",font=("Arial",30), bg="pink",command=lambda:Onclick("9"))
btn3.place(x=270,y=200)

btn4=tk.Button(root,text=" /  ",font=("Arial",30), bg="pink",command=lambda:Onclick("/"))
btn4.place(x=380,y=200)

btn5=tk.Button(root,text=" 4 ",font=("Arial",30), bg="pink",command=lambda:Onclick("4"))
btn5.place(x=40,y=300)

btn6=tk.Button(root,text=" 5 ",font=("Arial",30), bg="pink",command=lambda:Onclick("5"))
btn6.place(x=160,y=300)

btn7=tk.Button(root,text="  * ",font=("Arial",30), bg="pink",command=lambda:Onclick("*"))
btn7.place(x=270,y=300)

btn8=tk.Button(root,text=" 1 ",font=("Arial",30), bg="pink",command=lambda:Onclick("1"))
btn8.place(x=380,y=300)

btn9=tk.Button(root,text=" 2 ",font=("Arial",30), bg="pink",command=lambda:Onclick("2"))
btn9.place(x=40,y=400)

btn9=tk.Button(root,text=" 3 ",font=("Arial",30), bg="pink",command=lambda:Onclick("3"))
btn9.place(x=160,y=400)

btn9=tk.Button(root,text=" - ",font=("Arial",30), bg="pink",command=lambda:Onclick("-"))
btn9.place(x=270,y=400)

btn9=tk.Button(root,text=" 0 ",font=("Arial",30), bg="pink",command=lambda:Onclick("0"))
btn9.place(x=380,y=400)

btn9=tk.Button(root,text=" . ",font=("Arial",30), bg="pink",command=lambda:Onclick("."))
btn9.place(x=40,y=500)

btn9=tk.Button(root,text=" = ",font=("Arial",30), bg="pink",command=lambda:Onclick("="))
btn9.place(x=160,y=500)

btn9=tk.Button(root,text=" + ",font=("Arial",30), bg="pink",command=lambda:Onclick("+"))
btn9.place(x=270,y=500)

btn9=tk.Button(root,text=" c ",font=("Arial",30), bg="pink",command=lambda:Onclick("c"))
btn9.place(x=380,y=500)

btn9=tk.Button(root,text=" 6 ",font=("Arial",30), bg="pink",command=lambda:Onclick("6"))
btn9.place(x=160,y=600)

root.mainloop()

