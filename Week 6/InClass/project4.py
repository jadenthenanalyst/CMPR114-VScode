def main():
    num_emps = int(input("enter the number of employee records: "))

    emp_file = open ("C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\employees.txt", "w")

    for count in range(1, num_emps + 1):
        print('enter data for employee #', count)

        name = input("Name: ")
        id_num = input("ID NUMBER: ")
        dept = input("DEPARTMENT: ")

        emp_file.write("INFORMATION OF EMPLOYEE #"+ str(count) +" IS:\n")
        emp_file.write("Name: " + name + "\n")
        emp_file.write("ID: " + id_num + "\n")
        emp_file.write("Department: " + dept + "\n" +"\n")

        print()

    emp_file.close()
    print('recorded\n')
main()

def read():
    read_file = open ("C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\employees.txt", "r")
    read_content = read_file.read()
    read_file.close()
    print(read_content)
read()