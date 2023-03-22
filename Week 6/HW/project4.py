import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.withdraw()

f = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\HW\\file\\numbers.txt','r')
list = []
for line in f:
    list.append(int(line.strip("\n")))
sum = sum(list)

messagebox.showinfo("Numbers inside file: " + str(list), "The sum is: " + str(sum))

win.deiconify()
win.destroy()
win.quit()



