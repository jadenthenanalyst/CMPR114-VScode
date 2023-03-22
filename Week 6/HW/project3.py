def write_list():
    list_file = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\HW\\file\\number_list.txt','w')
    for count in range(1, 101):
        list_file.write(str(count) + "\n")
    list_file.close()
write_list()

