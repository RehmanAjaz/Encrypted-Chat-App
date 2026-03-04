import socket
import threading
import tkinter as tk
from cryptography.fernet import Fernet
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5555

key = Fernet.generate_key()
cipher = Fernet(key)

clients = []

# GUI
window = tk.Tk()
window.title("Encrypted Chat Server")
window.geometry("650x450")

chat_area = tk.Text(window, height=22, width=75)
chat_area.pack(pady=10)

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            clients.remove(client)

def handle_client(client, addr):
    while True:
        try:
            encrypted_message = client.recv(1024)

            # show encrypted message
            chat_area.insert(tk.END, f"\nEncrypted from {addr}:\n{encrypted_message}\n")

            decrypted_message = cipher.decrypt(encrypted_message).decode()

            # show decrypted message with timestamp
            chat_area.insert(tk.END, f"Decrypted:\n{decrypted_message}\n")

            broadcast(encrypted_message)

        except:
            clients.remove(client)
            client.close()
            break

def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    chat_area.insert(tk.END, "Server Started...\n")
    chat_area.insert(tk.END, f"Encryption Key: {key.decode()}\n\n")

    def accept_clients():
        while True:
            client, addr = server.accept()
            clients.append(client)

            chat_area.insert(tk.END, f"Client Connected: {addr}\n")

            client.send(key)

            thread = threading.Thread(target=handle_client, args=(client, addr))
            thread.start()

    threading.Thread(target=accept_clients).start()

start_button = tk.Button(window, text="Start Server", command=start_server)
start_button.pack()

window.mainloop()