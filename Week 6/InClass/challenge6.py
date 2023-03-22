import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry("300x200")
win.title("Gui Numbers")

lblNum1 = tk.Label(win, text="enter first number: ").grid(column = 0, row = 0)
lblNum2 = tk.Label(win, text="enter second number: ").grid(column =0, row = 1)
lblNum3 = tk.Label(win, text="enter third number: ").grid(column =0, row = 2)

def write():
    text_file = open("C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\GUI_numbers.txt","a")
    sum = N1.get() + N2.get() + N3.get()
    avg = sum / 3
    content = text_file.write("The three number are: " + str(N1.get()) + ", " + str(N2.get()) + ", " + str(N3.get()) + "\n" + "The total is " + str(sum)+ "\n" + "The average is " + str(avg))
    text_file.close()
    messagebox.showinfo("information", "Data Recorded")

def quit():
    messagebox.showinfo("information","Thank you...")
    win.destroy()

def submit():
    messagebox.showinfo("information","entered :" + str(N1.get()) + "," + str(N2.get()) + ","  + str(N3.get()))

N1 = tk.IntVar()
intNumber1 = tk.Entry(win, width = 12, textvariable = N1).grid(column = 1, row = 0)
N2 = tk.IntVar()
intNumber2 = tk.Entry(win, width = 12, textvariable = N2).grid(column = 1, row = 1)
N3 = tk.IntVar()
intNumber3 = tk.Entry(win, width = 12, textvariable = N3).grid(column = 1, row = 2)

btnSubmit = tk.Button(win, text="submit", command=submit).grid(column = 0, row = 7)

btnQuit = tk.Button(win, text= "quit", command= quit).grid(column = 1, row = 7)

btnWrite = tk.Button(win, text = "transfer", command = write).grid(column = 2, row = 7)

win.mainloop()
submit()