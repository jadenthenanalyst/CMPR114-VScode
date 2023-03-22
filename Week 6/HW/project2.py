def ReadInput():
    ReadFile = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\HW\\file\\things.txt','r')
    FileContent = ReadFile.read()
    ReadFile.close()
    print(FileContent)
ReadInput()