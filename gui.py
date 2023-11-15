
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

    def send_message(self):
        message = self.message_entry.get()
        self.display_message(f"> {self.nick}: {message}")
        # Aqui você pode enviar a mensagem para o servidor IRC

    def display_message(self, message):
        self.message_area.config(state="normal")
        self.message_area.insert("end", f"{message}\n")
        self.message_area.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    irc_gui = IRCClientGUI(root)
    root.configure(bg="brown", width=800, height=600)  # Define a cor de 

    root.mainloop()
