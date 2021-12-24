import sys
import socket
from _thread import start_new_thread
from game import game

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8888
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))
    sys.exit()

print('Waitiing for a Connection..')
ServerSocket.listen(20)

def new_game(connection, addr):
    connection.send(str.encode('歡迎來到1A2B！'))
    # Initialize the new game 1A2B!
    Game = game()
    print("The password is : ", Game.passwd)
    while True:
        code = connection.recv(1024)
        msg = str(code.decode('utf-8'))
        if not code or msg.lower() == 'exit':
            connection.sendall('遊戲結束!'.encode('utf-8'))
            break
        res = Game.play(msg)
        if res == 'WIN':
            print(addr, "win the game.", msg, "is the password")
        else:
            print(msg, f"is {res}")
        connection.sendall(res.encode('utf-8'))
    connection.close()

try:
    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(new_game, (Client, address, ))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
except KeyboardInterrupt as e:
    print(f'KeyboardInterrupt: {e}')
finally:
    ServerSocket.close()
