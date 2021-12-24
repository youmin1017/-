import socket
import sys

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8888

print('輸入Exit以結束遊戲（不分大小寫）')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
    sys.exit()

Response = ClientSocket.recv(1024)

try:
    while True:
        Input = input('輸入四位數字： ')
        ClientSocket.send(str.encode(Input))
        res = ClientSocket.recv(1024)
        res = res.decode('utf-8')
        if res == 'WIN':
            print(f"恭喜！正確答案為：{Input}")
            print("遊戲結束！")
            break
        else:
            print(res)
        if Input.lower()  == 'exit':
            break
except KeyboardInterrupt as e:
    print(f'KeyboardInterrupt: {e}')
finally:
    ClientSocket.close()
