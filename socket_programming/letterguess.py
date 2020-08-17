import socket

lettersocket = socket.socket()
lettersocket.connect(('127.0.0.1',1234))
msg = lettersocket.recv(1024).decode()
print(msg)
msg = ''
while msg != 'Guessed correctly!':
    newletter = str(input("I guess this letter: "))
    lettersocket.sendall(newletter.encode())
    
    msg = lettersocket.recv(1024).decode()
    print(msg)
    
    
lettersocket.close()

