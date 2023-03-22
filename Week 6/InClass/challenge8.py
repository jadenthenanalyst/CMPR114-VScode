def WriteNum():
    import random
    num1 = random.randint(1, 10)
    outfile = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\challenge8.txt', 'w')
    outfile.write(str(num1))
WriteNum()

def ReadNum():
    infile = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\challenge8.txt', 'r')
    filecontent = infile.read()
    infile.close()
    print(filecontent)
ReadNum()



