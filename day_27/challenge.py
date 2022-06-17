from tkinter import *

window = Tk()
window.title("Unit converter")
window.minsize(width=100,height=100)
window.config(padx=15,pady=15)

input = Entry(width= 20)
input.grid(row=0,column=1)


ans = Label(width=20)
ans.grid(row=1,column=1)



label1 = Label(text= "Celcius")
label1.grid(row=0,column=2)


label2 = Label(text=" is equal to ")
label2.grid(row=1,column=0)


label3 = Label(text="Farhaneit")
label3.grid(row=1,column=2)

def calc(*args):
    x = float(input.get())
    print(x)
    ans.config(text = round((x *9/5) + 32 ))


button = Button(text="Calculate",command = calc)
button.grid(row=2,column=1)






window.mainloop()
