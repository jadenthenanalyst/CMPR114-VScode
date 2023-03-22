def write():
    outFile = open('myFile.txt','w')
    outFile1 = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\myFile.txt','w')

    outFile.write('Jason\n')
    outFile.write('Jill\n')
    outFile.write('Jake\n')

    outFile1.write('Jason\n')
    outFile1.write('Jill\n')
    outFile1.write('Jake\n')

    outFile.close()
    outFile1.close()

    print('the names have been recorded')

write()

def read():
    infile = open('myFile.txt','r')
    infile1 = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\myFile.txt','r')

    fileContents = infile.read()
    fileContents1 = infile1.read()

    infile.close()
    infile1.close()

    print(fileContents)
    print(fileContents1)

read()
