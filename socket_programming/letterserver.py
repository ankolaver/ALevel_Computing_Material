import socket
import random

lettersocket = socket.socket()
lettersocket.bind(('127.0.0.1', 1234))
lettersocket.listen()
conn, addr = lettersocket.accept()

letter = chr(random.randint(ord('a'),ord('z')))
print("To guess: ", letter)
complete = False
conn.send(b'=======GAME===GUESS=A=LETTER========')
while not complete:
    data = conn.recv(1024).decode().lower()
    print(data)
    if ord(data) > ord(letter):
        conn.send(b'Letter too high')
    elif ord(data) < ord(letter):
        conn.send(b'Letter too low')
    else:
        conn.send(b'Guessed correctly!')
        complete = True

conn.close()
lettersocket.close()
        
