import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry("300x200")
win.title("Customer Information")

lblLastname = tk.Label(win, text="enter the lastname").grid(column = 0, row = 0)
lblFirstname = tk.Label(win, text="enter the firstname:").grid(column =0, row = 1)
lblAdress = tk.Label(win, text="enter the adress:").grid(column =0, row = 2)
lblCity = tk.Label(win, text="enter the city:").grid(column =0, row = 3)
lblState= tk.Label(win, text="enter the state:").grid(column =0, row = 4)
lblZipcode = tk.Label(win, text="enter the zipcode:").grid(column =0, row = 5)

def write():
    text_file = open("C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\Customers.txt","a")
    content = text_file.write("\nConfirmation: "+ str(LN.get()) + "," + str(FN.get()) + "," + str(AD.get()) + "," + str(CT.get()) + "," + str(ST.get()) + "," + str(ZIP.get()))
    text_file.close()
    messagebox.showinfo("information","Data Recorded")

def quit():
    messagebox.showinfo("information","Thank you...")
    win.destroy()

def submit():
    messagebox.showinfo("information","entered :" + LN.get() + "," + FN.get() + ","  + AD.get() + "," + CT.get() + "," + ST.get() + "," + ZIP.get())

LN = tk.StringVar()
txtLastname = tk.Entry(win, width = 12, textvariable = LN).grid(column = 1, row = 0)
FN = tk.StringVar()
txtFirstname = tk.Entry(win, width = 12, textvariable= FN).grid(column = 1, row = 1)
AD = tk.StringVar()
txtAdress = tk.Entry(win, width = 12, textvariable = AD).grid(column = 1, row = 2)
CT = tk.StringVar()
txtCity = tk.Entry(win, width = 12, textvariable = CT).grid(column = 1, row = 3)
ST = tk.StringVar()
txtState = tk.Entry(win, width = 12, textvariable = ST).grid(column = 1, row = 4)
ZIP = tk.StringVar()
txtZip = tk.Entry(win, width = 12, textvariable = ZIP).grid(column = 1, row = 5)

btnSubmit = tk.Button(win, text="submit", command=submit).grid(column = 0, row = 7)

btnQuit = tk.Button(win, text= "quit", command= quit).grid(column = 1, row = 7)

btnWrite = tk.Button(win, text = "transfer", command = write).grid(column = 2, row = 7)

win.mainloop()
submit()