from tkinter import *
root = Tk()
root.title("ANEEQ'S CALCULATOR")
e=Entry(root,width=40,borderwidth=6)
e.grid(row=0,column=0,columnspan=3)
def click(number):
    currentnumber=e.get()
    e.delete(0, END)
    e.insert(0,str(currentnumber)+str(number))
def clear():
    e.delete(0,END)
def equal():
    second_number= e.get()
    e.delete(0, END)

    if math =="sum":
        e.insert(0,f_num + int(second_number))

    if math == "difference":
        e.insert(0, f_num - int(second_number))

    if math == "divide":
        e.insert(0, f_num / int(second_number))

def sum():
    first_number= e.get()
    global f_num
    global math
    math="sum"
    f_num = int(first_number)
    e.delete(0,END)
def difference():
    first_number = e.get()
    global f_num
    global math
    math="difference"
    f_num = int(first_number)
    e.delete(0, END)
    return
def divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)
    return


button_1=Button(root,text="7",padx=40,pady=20,command=lambda:click(7))
button_2=Button(root,text="8",padx=40,pady=20,command=lambda:click(8))
button_3=Button(root,text="9",padx=40,pady=20,command=lambda:click(9))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:click(6))
button_7=Button(root,text="1",padx=40,pady=20,command=lambda:click(1))
button_8=Button(root,text="2",padx=40,pady=20,command=lambda:click(2))
button_9=Button(root,text="3",padx=40,pady=20,command=lambda:click(3))
button_10=Button(root,text="+",padx=40,pady=20,command=sum)
button_11=Button(root,text="/",padx=40,pady=20,command=divide)
button_12=Button(root,text="-",padx=40,pady=20,command=difference)
button_13=Button(root,text="DEL",padx=34,pady=20,command=clear)
button_14=Button(root,text="ANS",padx=32,pady=20,command=equal)
button_15=Button(root,text="=",padx=39,pady=20,command=equal)

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)

button_10.grid(row=4,column=0)
button_11.grid(row=4,column=1)
button_12.grid(row=4,column=2)

button_13.grid(row=5,column=0)
button_14.grid(row=5,column=1)
button_15.grid(row=5,column=2)


root.mainloop()