import socket 
import threading

class ServerNode:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12345)
        self.node.bind(port_and_ip)
        self.node.listen(5)
        self.connection, addr = self.node.accept()

    def send_sms(self, SMS):
        self.connection.send(SMS.encode())

    def receive_sms(self):
        while True:
            data = self.connection.recv(1024).decode()
            print(data)

    def main(self):
        while True:
            message = input()
            self.send_sms(message)

server = ServerNode()
always_receive = threading.Thread(target=server.receive_sms)
always_receive.daemon = True
always_receive.start()
server.main()