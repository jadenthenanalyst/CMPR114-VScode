def WriteInput():

    firstname = input("Please enter your firstname: ")
    lastname = input("Please enter your lastname: ")
    age = input("Please enter your age: ")

    challenge1File = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\challenge1.txt','a')

    challenge1File.write(firstname + "\n")
    challenge1File.write(lastname + "\n")
    challenge1File.write(age + "\n")

    challenge1File.close()

    print('the information have been recorded')

WriteInput()

def ReadInput():

    InChallenge1 = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\challenge1.txt','r')

    Challenge1Contents = InChallenge1.read()

    InChallenge1.close()

    print(Challenge1Contents)

ReadInput()



    