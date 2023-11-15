import socket
import sys
import threading

class IRCClient:
    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.nick = None
        self.password = None
        self.channel = "#home"

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server, self.port))
        self.send_message(f"USER {self.nick} 0 * :{self.nick}\r\n")
        self.send_message(f"NICK {self.nick}\r\n")
        self.send_message(f"JOIN {self.channel}\r\n")

    def send_message(self, message):
        self.sock.send(message.encode("utf-8"))

    def receive_messages(self):
        while True:
            data = self.sock.recv(4096).decode("utf-8")
            if not data:
                break
            print(data)

    def start(self):
        try:
            self.nick = input("Enter your nickname: ")
            self.password = input("Enter your password: ")
            self.connect()

            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()

            while True:
                message = input()
                if not message:
                    break
                self.send_message(f"PRIVMSG {self.channel} :{message}\r\n")

        except KeyboardInterrupt:
            print("\nExiting...")
        finally:
            self.sock.close()

print("\x1bc\x1b[43;30mstart application:")

if __name__ == "__main__":
    server_ip = "192.168.1.5"
    server_port = 6667

    irc_client = IRCClient(server_ip, server_port)
    irc_client.start()

