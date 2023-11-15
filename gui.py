import socket
import sys
import threading
import tkinter as tk
from tkinter import simpledialog

class IRCClientGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("IRC Client")

        # Variáveis
        self.nick = None
        self.password = None
        self.channel = "#home"
        self.server = "192.168.1.5"
        self.port = 6667
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server, self.port))
        

        # Configuração da GUI
        self.setup_gui()

        # Configuração do cliente IRC
        self.setup_irc_client()

    def setup_gui(self):
        # Área de texto para exibir mensagens
        self.message_area = tk.Text(self.master, state="disabled", wrap="word", height=10, width=40)
        self.message_area.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Caixa de entrada para nova mensagem
        self.message_entry = tk.Entry(self.master, width=30)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10)

        # Botão para enviar mensagem
        send_button = tk.Button(self.master, text="Send", command=self.send_message)
        send_button.grid(row=1, column=1, padx=10, pady=10)

    def setup_irc_client(self):
        self.nick = simpledialog.askstring("Nickname", "Enter your nickname:")
        self.password = simpledialog.askstring("Password", "Enter your password:")

        # Aqui você pode iniciar seu cliente IRC, usar self.nick e self.password
        # para se conectar ao servidor IRC, juntar a um canal, etc.
        
        
        self.send_messages(f"USER {self.nick} 0 * :{self.nick}\r\n")
        self.send_messages(f"NICK {self.nick}\r\n")
        self.send_messages(f"JOIN {self.channel}\r\n")
 

    

    def send_message(self):
        message:str = str(self.message_entry.get())
        msg=f"PRIVMSG {self.channel} :{message}\r\n"
        self.sock.send(msg.encode("utf-8"))
        self.display_message(f"> {self.nick}: {message}")
        # Aqui você pode enviar a mensagem para o servidor IRC

    def display_message(self, message):
        self.message_area.config(state="normal")
        self.message_area.insert("end", f"{message}\n")
        self.message_area.config(state="disabled")
    def send_messages(self, message:str):
        self.sock.send(message.encode("utf-8"))

if __name__ == "__main__":
    root = tk.Tk()
    irc_gui = IRCClientGUI(root)
    root.configure(bg="brown", width=800, height=600)  # Define a cor de 

    root.mainloop()
