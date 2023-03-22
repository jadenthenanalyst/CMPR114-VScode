def WriteNumbers():

    outfile = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\challenge7.txt', 'a')

    name = input('enter your name: ')
    midterm = int(input('enter midterm grade: '))
    final = int(input('enter final grade: '))
    avg = ((midterm + final)/2)
    grades = []
    if avg >= 90:
        grades.append('A')
    elif avg >= 80:
        grades.append('B')
    elif avg >= 70:
        grades.append('C')
    elif avg >= 60:
        grades.append('D')
    elif avg < 60:
        grades.append('F')

    outfile.write("Student Name: " + name + "\n")
    outfile.write("Midterm grade is: " + str(midterm) + "\n")
    outfile.write("Final grade is: " + str(final) + "\n")
    outfile.write("Average grade is: " + str(avg) + "\n")
    outfile.write("Letter grade is: " + str(grades) + "\n")

    print("data recorded")

WriteNumbers()

def ReadNumbers():
    readfile = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\challenge7.txt', 'r')
    filecontent = readfile.read()
    readfile.close()
    print(filecontent)
ReadNumbers()

