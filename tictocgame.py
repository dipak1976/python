from tkinter import *

import tkinter.messagebox as tmsg


root = Tk()
root.geometry('470x560')
root.resizable(0,0)
root.title('Shunya-Chokadi')
root.configure(background= "lightblue")

#function for disabled all butons when game rich to logic.
    
def stop():
    
    b1['state'] = DISABLED
    b2['state'] = DISABLED
    b3['state'] = DISABLED
    b4['state'] = DISABLED
    b5['state'] = DISABLED
    b6['state'] = DISABLED
    b7['state'] = DISABLED
    b8['state'] = DISABLED
    b9['state'] = DISABLED
    
# function for counting and display '0' and 'X'
count = 0
def show(b):
    global count
    
    if count % 2 == 0 :
         b.configure(background= "lightgreen")
         if b['text'] == " ":
            b['text'] = "0"
            b['state'] = DISABLED
         
    else :
         b.configure(background= "lightpink")
         if b['text'] == " ":
            b['text'] = "X"
            b['state'] = DISABLED
    
    count = count + 1 

# winner logic and display message:  
    if b1['text'] == "0" and b2['text'] == "0" and b3['text'] == "0" :
        tmsg.showinfo("congratulations !!", "Player One with '0' is winner.\n\nTo Play again press Restart")
        stop()
    elif b1['text'] == "X" and b2['text'] == "X" and b3['text'] == "X" :
        tmsg.showinfo("congratulations !!", "Player Two with 'X' is winner.\n\nTo Play again press Restart")
        stop()

    elif b4['text'] == "0" and b5['text'] == "0" and b6['text'] == "0" :
        tmsg.showinfo("congratulations !!", "Player One with '0' is winner.\n\nTo Play again press Restart")
        stop()
    elif b4['text'] == "X" and b5['text'] == "X" and b6['text'] == "X" :
        tmsg.showinfo("congratulations !!", "Player Two with 'X' is winner.\n\nTo Play again press Restart")
        stop()
    elif b7['text'] == "0" and b8['text'] == "0" and b9['text'] == "0" :
        tmsg.showinfo("congratulations !!", "Player One with '0' is winner.\n\nTo Play again press Restart")
        stop()
    elif b7['text'] == "X" and b8['text'] == "X" and b9['text'] == "X" :
        tmsg.showinfo("congratulations !!", "Player Two with 'X' is winner.\n\nTo Play again press Restart")
        stop()
    elif b1['text'] == "0" and b4['text'] == "0" and b7['text'] == "0" :
        tmsg.showinfo("congratulations !!", "Player One with '0' is winner.\n\nTo Play again press Restart")
        stop()
    elif b1['text'] == "X" and b4['text'] == "X" and b7['text'] == "X" :
        tmsg.showinfo("congratulations !!", "Player Two with 'X' is winner.\n\nTo Play again press Restart")
        stop()
    elif b2['text'] == "0" and b5['text'] == "0" and b8['text'] == "0" :
        tmsg.showinfo("congratulations !!", "Player One with '0' is winner.\n\nTo Play again press Restart")
        stop()
    elif b2['text'] == "X" and b5['text'] == "X" and b8['text'] == "X" :
        tmsg.showinfo("congratulations !!", "Player Two with 'X' is winner.\n\nTo Play again press Restart")
        stop()
    elif b3['text'] == "0" and b6['text'] == "0" and b9['text'] == "0" :
        tmsg.showinfo("congratulations !!", "Player One with '0' is winner.\n\nTo Play again press Restart")
        stop()
    elif b3['text'] == "X" and b6['text'] == "X" and b9['text'] == "X" :
        tmsg.showinfo("congratulations !!", "Player Two with 'X' is winner.\n\nTo Play again press Restart")
        stop()                
    elif b1['text'] == "0" and b5['text'] == "0" and b9['text'] == "0" :
        tmsg.showinfo("congratulations !!", "Player One with '0' is winner.\n\nTo Play again press Restart")
        stop()
    elif b1['text'] == "X" and b5['text'] == "X" and b9['text'] == "X" :
        tmsg.showinfo("congratulations !!", "Player Two with 'X' is winner.\n\nTo Play again press Restart")
        stop()                
    elif b3['text'] == "0" and b5['text'] == "0" and b7['text'] == "0" :
        tmsg.showinfo("congratulations !!", "Player One with '0' is winner.\n\nTo Play again press Restart")
        stop()
    elif b3['text'] == "X" and b5['text'] == "X" and b7['text'] == "X" :
        tmsg.showinfo("congratulations !!", "Player Two with 'X' is winner.\n\nTo Play again press Restart")
        stop() 
    else :
        if b1['text'] != " " and b1['text'] != " " and b1['text'] != " " and b2['text'] != " " and b3['text'] != " " and b4['text'] != " " and b5['text'] != " " and b6['text'] != " " and b7['text'] != " " and b8['text'] != " " and b9['text'] != " " :
            tmsg.showinfo("It`s a Draw","To Play again press Restart")
                                       
#function for restart game    
def restart():
    
    b1.configure(background = "yellow",text = " ",state = ACTIVE)
    b2.configure(background = "yellow",text = " ",state = ACTIVE)
    b3.configure(background = "yellow",text = " ",state = ACTIVE)
    b4.configure(background = "yellow",text = " ",state = ACTIVE)
    b5.configure(background = "yellow",text = " ",state = ACTIVE)
    b6.configure(background = "yellow",text = " ",state = ACTIVE)
    b7.configure(background = "yellow",text = " ",state = ACTIVE)
    b8.configure(background = "yellow",text = " ",state = ACTIVE)
    b9.configure(background = "yellow",text = " ",state = ACTIVE)

b1 =Button(root,text = " ",width = 20,height = 10,bg = "yellow",font = ("Arial bold",25),command = lambda : show(b1))
b1.place(x = 5,y = 5,width = 150,height = 150)

b2 =Button(root,text = " ",width = 20,height = 10,bg = "yellow",font = ("Arial bold",25),command = lambda : show(b2))
b2.place(x = 160,y = 5,width = 150,height = 150)

b3 =Button(root,text = " ",width = 20,height = 10,bg = "yellow",font = ("Arial bold",25),command = lambda : show(b3))
b3.place(x = 315,y = 5,width = 150,height = 150)

b4 =Button(root,text = " ",width = 20,height = 10,bg = "yellow",font = ("Arial bold",25),command = lambda : show(b4))
b4.place(x = 5,y = 160,width = 150,height = 150)

b5 =Button(root,text = " ",width = 20,height = 10,bg = "yellow",font = ("Arial bold",25),command = lambda : show(b5))
b5.place(x = 160,y = 160,width = 150,height = 150)

b6 =Button(root,text = " ",width = 20,height = 10,bg = "yellow",font = ("Arial bold",25),command = lambda : show(b6))
b6.place(x = 315,y = 160,width = 150,height = 150)

b7 =Button(root,text = " ",width = 20,height = 10,bg = "yellow",font = ("Arial bold",25),command = lambda : show(b7))
b7.place(x = 5,y = 315,width = 150,height = 150)

b8 =Button(root,text = " ",width = 20,height = 10,bg = "yellow",font = ("Arial bold",25),command = lambda : show(b8))
b8.place(x = 160,y = 315,width = 150,height = 150)

b9 =Button(root,text = " ",width = 20,height = 10,bg = "yellow",font = ("Arial bold",25),command = lambda : show(b9))
b9.place(x = 315,y = 315,width = 150,height = 150)

b10 =Button(root,text = "Restart",width = 20,height = 10,bg = "blue",font = ("Arial bold",25),command = restart)
b10.place(x = 5,y = 470,width = 150,height = 50)

b =Button(root,text = "End Game",width = 20,height = 5,bg = "blue",font = ("Arial bold",15),command = root.quit)
b.place(x = 315,y = 470,width = 150,height = 50)


lbl = Label(root,text = ("createdByDipakPrajapati"),bg = "lightblue",fg = "red",font = ("Arial bold",10))
lbl.place(x = 5,y = 525)

root.mainloop()
