from tkinter import *
from tkinter import messagebox
from turtle import width
import webbrowser
import os
import sys
a=Tk()
coul="#6A0888"

bottumcolor="#F7BE81"

a.geometry('800x480+280+50')

a.resizable(False,False)

a.title("super market" )

a.iconbitmap('icon.ico')

title=Label(a,text="welcome to my super market ",fg="white",bg="black",font=(16))
title.pack(fill=X)

def open1():
    webbrowser.open_new('https://www.facebook.com/profile.php?id=100013359993271')
def open2():
    webbrowser.open_new('https://www.instagram.com/yousri.meftah/?hl=fr')
def login():
    user=e1.get()
    pss=e2.get()
    messagebox.showinfo("hello",f"username : {user} and pass : {pss}")

f=Frame(a,width=230,height=460,bg=coul)
f.place(x=570,y=24)


t1=Label(f,text="super market project ",fg="white",bg=coul,font=('Arial',13,'bold'))
t1.place(x=22,y=20)


t2=Label(f,text="devlopper yousri meftah",fg="white",bg=coul,font=('Arial',13,'bold'))
t2.place(x=22,y=60)


t3=Label(f,text="social media accounts ",fg="white",bg=coul,font=('Arial',13,'bold'))
t3.place(x=22,y=100)


b1=Button(f,text='Facebook',width=21,height=2,fg="white",bg=bottumcolor,font=('Arial',13,'bold'),command=open1)
b1.place(x=5,y=140)


b2=Button(f,text='Instagram',width=21,height=2,fg="white",bg=bottumcolor,font=('Arial',13,'bold'),command=open2)
b2.place(x=5,y=200)


b3=Button(f,text='telephone',width=21,height=2,fg="white",bg=bottumcolor,font=('Arial',13,'bold'))
b3.place(x=5,y=260)


b4=Button(f,text='close super market',width=21,height=6,fg="white",bg=bottumcolor,font=('Arial',13,'bold'),command=quit)
b4.place(x=5,y=320)



photo=PhotoImage(file="logo.PNG")
picturelabel=Label(a,image=photo)
picturelabel.place(x=0,y=25,width=570,height=320)


f2=Frame(a,width=570,height=150,bg=coul)
f2.place(x=0,y=330)


b5=Button(f2,text='login',width=15,height=5,fg="white",bg=bottumcolor,font=('Arial',13,'bold'),command=login)
b5.place(x=10,y=20)


login=PhotoImage(file="login.png")
loginlabel=Label(f2,image=login)
loginlabel.place(x=435,y=10,width=130,height=130)

l1=Label(f2,text="Name : ",fg="gold",bg=coul,font=('Arial',13,'bold'))
l1.place(x=214,y=30)

l2=Label(f2,text="Password : ",fg="gold",bg=coul,font=('Arial',13,'bold'))
l2.place(x=180,y=80)

e1=Entry(f2,font=('Arial',13),justify='center')
e1.place(x=275,y=30,width=150,height=25)

e2=Entry(f2,font=('Arial',13),justify='center')
e2.place(x=275,y=80,width=150,height=25)
a.mainloop()