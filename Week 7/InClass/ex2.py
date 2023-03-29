from tkinter import *

root = Tk()
root.geometry('180x200')

listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)

listbox.insert( 1, "Sandwich")
listbox.insert( 2, "Burger")
listbox.insert( 3, "Pizza")
listbox.insert( 4, "French Fries")
listbox.insert( 5, "Hot Dogs")
listbox.insert( 6, "CheseBurger")

def selected_item():

    for i in listbox.curselection():
        print(listbox.get(i))

btn = Button(root, text='Print selected', command=selected_item)

btn.pack(side='bottom')
listbox.pack()

root.mainloop()