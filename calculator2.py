from tkinter import *
root = Tk()
root.geometry('425x300')
root.resizable(0,0)
root.title("Calculator v 2.0")
root.configure(background = "orange")

a =StringVar()
def show(c):
    a.set(a.get() + c)
def eql():
    x = eval(a.get())
    a.set(x)

def cl():
    a.set("")

             
e1 = Entry(font = ("",30),justify = "right",bg = "orange",textvariable = a)
e1.place(x = 0,y = 0,width = 425,height = 50)


b1 = Button(root,text = "7",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b1.place(x = 5,y = 55,width = 100,height = 50)
b1.configure(command = lambda: show("7"))# function to print button to entry
b2 = Button(root,text = "8",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b2.place(x = 110,y = 55,width = 100,height = 50)
b2.configure(command = lambda: show("8"))
b3 = Button(root,text = "9",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b3.place(x = 215,y = 55,width = 100,height = 50)
b3.configure(command = lambda: show("9"))
b4 = Button(root,text = "+",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b4.place(x = 320,y = 55,width = 100,height = 50)
b4.configure(command = lambda: show("+"))


b5 = Button(root,text = "4",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b5.place(x = 5,y = 110,width = 100,height = 50)
b5.configure(command = lambda: show("4"))
b6 = Button(root,text = "5",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b6.place(x = 110,y = 110,width = 100,height = 50)
b6.configure(command = lambda: show("5"))
b7 = Button(root,text = "6",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b7.place(x = 215,y = 110,width = 100,height = 50)
b7.configure(command = lambda: show("6"))
b8 = Button(root,text = "-",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b8.place(x = 320,y = 110,width = 100,height = 50)
b8.configure(command = lambda: show("-"))

b9 = Button(root,text = "1",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b9.place(x = 5,y = 165,width = 100,height = 50)
b9.configure(command = lambda: show("1"))
b10 = Button(root,text = "2",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b10.place(x = 110,y = 165,width = 100,height = 50)
b10.configure(command = lambda: show("2"))
b11 = Button(root,text = "3",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b11.place(x = 215,y = 165,width = 100,height = 50)
b11.configure(command = lambda: show("3"))
b12 = Button(root,text = "*",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b12.place(x = 320,y = 165,width = 100,height = 50)
b12.configure(command = lambda: show("*"))

b13 = Button(root,text = "C",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b13.place(x = 5,y = 220,width = 100,height = 50)
b13.configure(command = cl)
b14 = Button(root,text = "0",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b14.place(x = 110,y = 220,width = 100,height = 50)
b14.configure(command = lambda: show("0"))
b15 = Button(root,text = "=",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b15.place(x = 215,y = 220,width = 100,height = 50)
b15.configure(command = eql)
b16 = Button(root,text = "/",bg = "grey",font = ("",25),fg = "white",activebackground = "yellow",activeforeground = "red")
b16.place(x = 320,y = 220,width = 100,height = 50)
b16.configure(command = lambda: show("/"))

lab_1 = Label(root,text = "createdByDipakPrajapati",bg = "White",fg = "red")
lab_1.place(x= 5,y =280)


root.mainloop()
