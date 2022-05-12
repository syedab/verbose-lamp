#NAME- Abdulbari Syed
#Std Id - 1001995871
#importing socket connection to the program
import socket
#importing os interaction functions
import os
#importing lock functions from portalocker library
import portalocker
#Citation-Sockets Tutorial with Python 3 part 1 - sending and receiving data(https://www.youtube.com/watch?v=Lbfe3-v7yE0&list=PL6yCaejUzyZ3EtSvkwcYK5A3Fj2n1TVmV&index=1)
c = socket.socket(socket.AF_INET, socket. SOCK_STREAM) #creating socket connection for server A
c.connect(('localhost', 8485)) #assigning localhost and port number to connect to server A(port number needs to be changed while executing in every instance)
name = input('Enter LabAssignment/3') #printing the input from the user
c.send(bytes(name,'utf-8')) ##sending message through socket to server A to send directory 1 and directory 2
msg = c.recv(1024) # no. of bytes in message of socket being received from socket
print(msg.decode("utf-8")) #printing the message from server A
# Citation - https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory#
arr1 = os.listdir('sea_ex') #generating directory of server A
path = os.listdir('seb_ex') #generating directory of server B
def i():#creating module for concatenated directory 1 of server B and directory 2 of server A
    a1 = path + arr1 #concatenating directories from server a and server b
    # Citation – Python – Ways to remove duplicates from list-https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
    res = [] #implementing method
    for i in a1: #for loop for finding duplicate in directories
        if i not in res: #finding the duplicate files
            res.append(i) #finding recent modified file
    print("The list of directory 1 and 2 after removing duplicates : ") #printing the modified file after removal of the duplicate

    print(sorted(res)) #printing the modified file after removal of the duplicate
    #Citation-Portalocker Documentation - Release 2.3.2- (https://readthedocs.org/projects/portalocker/downloads/pdf/latest/)
    input('file to lock') #taking input to lock file
    file = open('/Users/abdulbari/Desktop/LAB3_Syed_axs5871/sea_ex/ldemoa.txt', 'r+') #directory location of text file to be locked
    portalocker.lock(file, portalocker.LOCK_EX) #lock function for locking the text file
    file.seek(12) #seeking update for locked file
    file.write('-----TESTING----') #appling update by writing on the locked file
    file.close() #unlocking the file after update
    print('file is locked')  ##print function for file being locked
    print(sorted(res)) #print function to display directory of a and b after locking.
    input('file to unlock') #taking input to unlock file
    print('file is unlocked')  ##print function for file being unlocked
    print(sorted(res)) ##print function to display directory of a and b after unlocking.
i() #calling module
