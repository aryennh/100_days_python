#TKINTER
#default arguments
# *args
# **kwargs
from tkinter import *

window = Tk()
window.title("GUI program")
window.minsize(width = 500, height=500)
#window.config(padx=100,pady=100)
#Label

#DEFAULT PARAMETERS ->>>>>>>
# you can define a function like def fun(a=1,b=2,c=3) :
#     {
#         etc etc
#     }
#
# and call that function like fun()
# if wanna chanege default values call as fun(4,,)
# if a function has optional arguments, that means those values already have default values set
#
#6TH LECTURE
#NORMAL ADD FUNCTION
'''
def add(n1,n2):
    return n1 + n2 
'''

# *args tells that function can accept any number of arguments
# using args isnt compulsory , but * is
# args is a tuple
"""
def add(*args):

    for n in args:
        print(n)
"""

my_label = Label(text="I am a label",font=("Arial",26,"italic"))
my_label.pack() # Shows the label on the screen


my_label['text'] = "NEW text"
my_label.config(text="NEW text")
my_label.grid(column =0,row = 0) #Grid is relative
#my_label.config(padx=40,pady=12)

#BUTTON"""



#my_label['text'] = "Someone clicked the button"




#entry
input = Entry(width = 20)
#input.pack()
#x = input.get
input.grid(column = 3, row =3)

def clicks():
    # print("I got clicked")
    my_label.config(text=input.get())

button = Button(text='spank me papi!', command=clicks)
button.grid(column=1,row=1)
new_button = Button(text = "New button")
new_button.grid(column=2,row=0)




window.mainloop()












'''
# from tkinter import *
# 
# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
# 
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
# 
# #Buttons
# def action():
#     print("Do something")
# 
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
# 
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
# 
# #Text -- > textbox for user to use
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END)) #END is an index , 1.0 refers to text at first line from the 0th character
# text.pack()
# 
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
# 
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
# 
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
# 
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
# 
# 
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
# 
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()
# asd
'''
