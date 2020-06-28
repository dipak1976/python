from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('260x365')
root.title("Table Creater")
root.resizable(0,0)
root.configure(background = "pink")

lbl = Label(root,text = "Enter your NUBMER to creat table :",bg = "cyan",fg = "red",font = (',bold',12))
lbl.pack(pady = 5)

a = StringVar()
#b = StringVar()

ent = Entry(root,width =5,bg = "yellow",fg = "black",font = (',bold',15),justify = "center", textvariable = a)
ent.pack(pady = 5)
ent.focus()

def count():
    t.delete('1.0',END)
    
    if a.get() == '':
        t.insert(END,"Please, \nEnter \nnumber \nfirst!!")
        messagebox.showinfo("માહીતી"," પિળા બોક્સ મા નમ્બર નાખો!!!")
    x = a.get()
    #p = type(x)
    #print(p)
    #if p == 'float':
     #   messagebox.showinfo("Information","Please enter whole Number")
    x = int(x)      
                      
    for i in range (1,11):
        y = (str(x) +"X"+str(i)+ "=", x*i)
        y1 = "\n"
        t.insert(END,y)  
        t.insert(END,y1)
        a.set('')
        
btn = Button(root,text = "Creat Table",bg = "skyblue",fg = "black",font = (',bold',10), command = count)
btn.pack(pady = 5)

t = Text(width = 15,height = 10,bg = "cyan",fg = "red",font = (',bold',12))
t.pack(pady = 5)

btn = Button(root,text = "End",bg = "skyblue",fg = "black",font = (',bold',10), command = root.quit)
btn.pack(pady = 5)

lbl_d = Label(root,text= "createdByDipakPrajapati",fg = "red")
lbl_d.pack()

root.mainloop()
