from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("250x250")
root.resizable(0,0)
root.title("Log in Form")
root.configure(background = "pink")

name = StringVar()
email = StringVar()
pasword = StringVar()


count = 1
def login():
    global count
    if name.get() =='' or email.get() =='' or pasword.get() =='':
        tmsg.showerror('Error','Please Fill all Details')
    else:
        
        print("Loged Person:",count)
        print("Name:",name.get())
        print("Email:",email.get())
        print("Passwor:",pasword.get())
        name.set('')
        email.set('')
        pasword.set('')
        count = count+1
    

lbl_1 = Label(root,text = "Name:",font = ('',15),bg = "pink",fg = "brown").grid(row = 0,column = 0,padx =5,pady = 10)
ent_1 = Entry(root,width = 15,font = ('',10),textvariable = name).grid(row = 0,column = 1,padx =5,pady = 10)


lbl_2 = Label(root,text = "Email:",font = ('',15),bg = "pink",fg = "brown").grid(row = 2,column = 0,padx =5,pady = 10)
ent_2 = Entry(root,width = 15,font = ('',10),textvariable = email).grid(row = 2,column = 1,padx =5,pady = 10)

lbl_3 = Label(root,text = "Password:",font = ('',15),bg = "pink",fg = "brown").grid(row = 3,column = 0,padx =5,pady = 10)
ent_3 = Entry(root,width = 15,font = ('',10),textvariable = pasword).grid(row = 3,column = 1,padx =5,pady = 10)

btn = Button(root,text = "Login",font = ('',12),command = login).grid(row = 4,columnspan = 2,padx = 5,pady = 10)





root.mainloop()
