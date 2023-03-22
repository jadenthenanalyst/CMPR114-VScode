def WriteInput():
    print("Enter the name of your friends: ")
    writeMoreFriends = 'Y'

    while writeMoreFriends == 'Y' or writeMoreFriends == 'y':

        name1 = input("Friend #1 ")
        name2 = input("Friend #2 ")
        name3 = input("Friend #3 ")

        FriendFile = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\friends.txt','a')

        FriendFile.write (name1 + '\n')
        FriendFile.write (name2 + '\n')
        FriendFile.write (name3 + '\n')

        FriendFile.close()

        print('friends recorded')

        writeMoreFriends = input('do you want to write more friends? type Y or y: ')

WriteInput()

def read():
    inFriends = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 6\\InClass\\file\\friends.txt','r')

    FriendsContent = inFriends.read()

    inFriends.close()

    print("Your list of friends: "+"\n" +FriendsContent)

read()