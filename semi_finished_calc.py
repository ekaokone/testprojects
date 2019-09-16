# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:05:38 2019

@author: Mavis
"""

from tkinter import *
from tkinter import ttk
from math import sqrt
master=Tk(className=" Standard calculator")
operate=""
def display_values(x):
    global operate
    operate +=x
    display.delete(0,"end")
    display.insert("end",operate)
    
def evaluate():
    global operate
    display.delete(0,"end")
    if "^" in operate:
        operate=operate.replace("^","**")
    try:
        result=eval(operate)
    except ZeroDivisionError:
        display.insert("end","maths error!")
        operate=""
    else:
        operate=str(result)
        display.insert("end",str(result))
def clear_all():
    global operate
    display.delete(0,"end")
    operate=""
    display.insert("end",0)
def remove_one():
    global operate
    if len(operate)<=1:
        clear_all()
    else:
        
        operate=operate[:-1]
        display.delete(0,"end")
        display.insert("end",operate)
def get_square_root():
    global operate
    operate=str(sqrt(float(operate)))
    display.delete(0,"end")
    display.insert("end",operate)
    

# master.config(width=450,height=450) ## specifies the width and height of a widget
#master.geometry("600x500+100+0")
menu_bar=Menu(master)
file_menu=Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Scientific")
file_menu.add_command(label="Standard")
file_menu.add_separator()
file_menu.add_command(label="Exit")

master.config(menu=menu_bar)

display=Entry(master,width=45,bd=8,justify="right")
display.grid(row=0,column=0)
btn_frame=Frame(master,bd=10,relief="raised")
btn_frame.grid(row=1,column=0)

#================Row one==================================
btn1=ttk.Button(btn_frame,text="1",command=lambda: display_values("1")).grid(row=1,column=0)
btn2=ttk.Button(btn_frame,text="2",command=lambda: display_values("2")).grid(row=1,column=1)
btn3=ttk.Button(btn_frame,text="3",command=lambda: display_values("3")).grid(row=1,column=2)
btn_plus=ttk.Button(btn_frame,text="+",command=lambda: display_values("+")).grid(row=1,column=3)

#==============Row two==============================
btn4=ttk.Button(btn_frame,text="4",command=lambda: display_values("4")).grid(row=2,column=0)
btn5=ttk.Button(btn_frame,text="5",command=lambda: display_values("5")).grid(row=2,column=1)
btn6=ttk.Button(btn_frame,text="6",command=lambda: display_values("6")).grid(row=2,column=2)
btn_minus=ttk.Button(btn_frame,text="-",command=lambda: display_values("-")).grid(row=2,column=3)

#==============Row three==============================
btn7=ttk.Button(btn_frame,text="7",command=lambda: display_values("7")).grid(row=3,column=0)
btn8=ttk.Button(btn_frame,text="8",command=lambda: display_values("8")).grid(row=3,column=1)
btn9=ttk.Button(btn_frame,text="9",command=lambda: display_values("9")).grid(row=3,column=2)
btn_mult=ttk.Button(btn_frame,text="x",command=lambda: display_values("*")).grid(row=3,column=3)

#==============Row three==============================
btn7=ttk.Button(btn_frame,text="0",command=lambda: display_values("0")).grid(row=4,column=0)
btn8=ttk.Button(btn_frame,text="=",width=25,command=evaluate).grid(row=4,column=1,columnspan=2)
btn_divide=ttk.Button(btn_frame,text="/",command=lambda: display_values("/")).grid(row=4,column=3)

side_frame=Frame(master,bd=10,relief="raised")
side_frame.grid(row=1,column=1)

btn_ac=ttk.Button(side_frame,text="AC",command=clear_all).grid(row=0,column=0)
btn_del=ttk.Button(side_frame,text="DEL",command=remove_one).grid(row=1,column=0)
btn_sqrt=ttk.Button(side_frame,text="√",command=get_square_root).grid(row=2,column=0)
btn_square=ttk.Button(side_frame,text="^",command=lambda: display_values("^")).grid(row=3,column=0)
master.resizable(width=False,height=False)


                                         



master.mainloop()