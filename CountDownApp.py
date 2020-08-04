from tkinter import *

t=0
def set_timer():
    global t
    t=t+int(el.get())
    return t

def count_down():
    global t
    if t>0:
        l1.config(text=t)
        t=t-1
        l1.after(1000,count_down)
    elif t==0:
        print("end")
        l1.config(text="Goo")
root=Tk()

root.geometry("180x150")

l1=Label(root,font="times 20")
l1.grid(row=1,column=2)

times=StringVar()
el=Entry(root,textvariable=times)
el.grid(row=3,column=2)

bl=Button(root,text="SET",width=20,command=set_timer)
bl.grid(row=4,column=2,padx=20)

b2=Button(root,text="START",width=20,command=count_down)
b2.grid(row=6,column=2,padx=20)

root.mainloop()