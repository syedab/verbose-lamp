#NAME- Abdulbari Syed
#Std Id - 1001995871
#importing socket connection to the program
import socket
#importing os interaction functions
import os
#importing os filepath interaction functions
import os.path

#Citation-Sockets Tutorial with Python 3 part 1 - sending and receiving data(https://www.youtube.com/watch?v=Lbfe3-v7yE0&list=PL6yCaejUzyZ3EtSvkwcYK5A3Fj2n1TVmV&index=1)
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket connection for client
c.bind(('localhost', 8485)) #assigning localhost and port number(port number needs to be changed while executing in every instance)
print('[SERVERA]connected to the socket') # print function for connection to socket
c.listen(1000) #socket listening for client connection

#Citation - https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory#
print("directory2") #printing the directory name
arr1 = (sorted(os.listdir('sea_ex/')))
print(arr1)#printing the directory of server B
path = os.listdir('seb_ex')  #generating directory of server B
a1 = path + arr1 #concatenating directories
#Citation – Python – Ways to remove duplicates from list-https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
res = [] #implementing method
for i in a1: #for loop for finding duplicate in directories
    if i not in res: #finding the duplicate files
        res.append(i) #finding recent modified file
print("The list after removing duplicates from both servers : ") #printing the modified file after removal of the duplicate

print(sorted(res))#printing the modified file after removal of the duplicate


#Citation-Sockets Tutorial with Python 3 part 1 - sending and receiving data(https://www.youtube.com/watch?v=Lbfe3-v7yE0&list=PL6yCaejUzyZ3EtSvkwcYK5A3Fj2n1TVmV&index=1)
while True: #introducing the while true function for connection to client
    clientsocket, address = c.accept() #accepting the client for socket connection
    print(f"Connection from {address} has been made!", ) #print function when connection to client has been made
    clientsocket.send(bytes("Welcome to the server A!", "utf-8")) #sending message through socket to client
    s = socket.socket (socket.AF_INET, socket. SOCK_STREAM) #creating socket connection
    s.connect(('localhost', 8086)) #assigning localhost and port number(port number needs to be changed while executing in every instance)
    # Citation - https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory#
    path = os.listdir('seb_ex') #generating directory of server A
    def i(): #creating module for concatenating directory 1 of server B and directory 2 of server A
        a1 = path + arr1 #concatenating the directory 1 and directory 2 together
        # Citation – Python – Ways to remove duplicates from list-https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
        res = [] #implementing method
        for i in a1: #for loop for finding duplicate in directories
            if i not in res: #finding the duplicate files
                res.append(i) #finding recent modified file
        print("The list sent to client after removing duplicates : ") #printing the modified file after removal of the duplicate

        print(sorted(res)) #printing the modified file after removal of the duplicate

    i() #calling module
    s.recv(1024).decode('utf-8') #socket for receiving from server B
    msg = s.recv(1024) # no. of bytes in message of socket being received from socket
    print(msg.decode("utf-8")) #printing the message from server B

