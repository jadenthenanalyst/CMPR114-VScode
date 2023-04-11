def WriteInput():

    brand = input("Please enter your favorite coffee brand: ")

    InProject2 = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Midterm\\Coffee.txt','a')
    InProject2.write("\n" + brand + ",99-8888,9.88")
    InProject2.close()
    print('the information have been recorded')

WriteInput()

def ReadInput():

    InProject2 = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Midterm\\Coffee.txt','r')

    Challenge2Contents = InProject2.read()

    InProject2.close()

    print(Challenge2Contents)

ReadInput()


