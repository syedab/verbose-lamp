#NAME- Abdulbari Syed
#Std Id - 1001995871
#importing socket connection to the program
import socket
#importing os interaction functions
import os
#Citation-Sockets Tutorial with Python 3 part 1 - sending and receiving data(https://www.youtube.com/watch?v=Lbfe3-v7yE0&list=PL6yCaejUzyZ3EtSvkwcYK5A3Fj2n1TVmV&index=1)
s = socket.socket(socket.AF_INET, socket. SOCK_STREAM) #creating socket connection for server A
s.bind(('localhost', 8086)) #assigning localhost and port number(port number needs to be changed while executing in every instance)
print('[serverB]connected to socket') # print function for connection to socket
s.listen(5) #socket listening for server A connection

#Citation - https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory#
print("directory1") #printing the directory name
arr = os.listdir('seb_ex') #generating directory of server B
print(sorted(arr)) #printing the directory of server B
arr1 = (sorted(os.listdir('sea_ex/')))#
a1 = arr + arr1 #concatenating directories
#Citation – Python – Ways to remove duplicates from list-https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
res = [] #implementing method
for i in a1: #for loop for finding duplicate in directories
    if i not in res: #finding the duplicate files
        res.append(i) #finding recent modified file
print("The list after removing duplicates from both server  : ") #printing the modified file after removal of the duplicate

print(sorted(res)) #printing the modified file after removal of the duplicate


#Citation-Sockets Tutorial with Python 3 part 1 - sending and receiving data(https://www.youtube.com/watch?v=Lbfe3-v7yE0&list=PL6yCaejUzyZ3EtSvkwcYK5A3Fj2n1TVmV&index=1)
while True: #introducing the while true function for connection to server A
    clientsocket, address = s.accept() #accepting the server A for socket connection
    print(f"Connection from {address} has been made!") #print function when connection to server A has been made
    clientsocket.send(bytes("Welcome to the server B!", "utf-8")) #sending message through socket to server A
    clientsocket.close() #closing the socket connection when operations are done
