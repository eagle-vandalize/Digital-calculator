from tkinter import *
def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() +text)
        screen.update()
root = Tk()
root.geometry("544x700")
root.title("Calculator by Abhishek singh")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X ,ipadx=3, pady=3,padx=3)

f = Frame(root , bg="red")
b = Button(f , text="=", padx=3,pady=3, font="lucida 40  bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT , padx =3, pady =3)



b = Button(f , text=".", padx=3 ,pady=3, font="lucida 40  bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT , padx =3, pady =3)

b = Button(f , text="c", padx=3,pady=3, font="lucida 40  bold")
b.pack(side = LEFT , padx =3, pady =3)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root , bg="orange")
b = Button(f, text="0", padx=3,pady=3,font="lucida 40 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT , padx =3, pady =3)

b = Button(f, text="1", padx=3,pady=3,font="lucida 40  bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT , padx =3, pady=3)

b = Button(f , text="2", padx=3 ,pady=3, font="lucida 40  bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT , padx =3, pady =3)

b = Button(f , text="3", padx=3,pady=3, font="lucida 40 bold")
b.pack(side = LEFT , padx =3, pady=3)
b.bind("<Button-1>",click)

b = Button(f, text="4", padx=3,pady=3,font="lucida 40 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT , padx=3, pady=3)
f.pack()

f = Frame(root , bg="orange")
b = Button(f, text="9", padx=3, pady=3, font="lucida 40 bold")
b.bind("<Button-1>", click , )
b.pack(side = LEFT, padx= 3, pady= 3)

b = Button(f , text="8", padx=3 ,pady=3, font="lucida 40 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT , padx = 3 , pady = 3)

b = Button(f , text="7", padx=3 ,pady=3, font="lucida 40  bold")
b.pack(side = LEFT , padx=3, pady=3)
b.bind("<Button-1>", click)



b = Button(f , text="6", padx=3 ,pady=3, font="lucida 40  bold")
b.pack(side = LEFT , padx =3, pady =3)
b.bind("<Button-1>",click)

b = Button(f , text="5", padx=3 ,pady=3, font="lucida 40  bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT , padx =3, pady=3)

#f = Frame(root , bg="orange")

f.pack()

#f = Frame(root , bg="orange")



#f.pack()

f = Frame(root , bg="grey")
b = Button(f, text="+", padx=3,pady=3,font="lucida 40  bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT , padx =3, pady =3)

b = Button(f , text="-", padx=5,pady=3, font="lucida 40  bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT , padx =5, pady=3)

b = Button(f , text="/", padx=3,pady=3, font="lucida 40  bold")
b.pack(side = LEFT , padx =5, pady=3)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root , bg="grey")
b = Button(f, text="%", padx=3, pady=3,font="lucida 40  bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT , padx =3, pady =3)



b = Button(f , text="* ", padx=3,pady=3, font="lucida 40  bold")
b.pack(side = LEFT , padx = 3, pady = 3)
b.bind("<Button-1>",click)
f.pack()
root.mainloop()

