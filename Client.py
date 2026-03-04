import socket
import threading
import tkinter as tk
from cryptography.fernet import Fernet
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

key = client.recv(1024)
cipher = Fernet(key)

# GUI
window = tk.Tk()
window.title("Encrypted Chat Client")
window.geometry("650x450")

chat_area = tk.Text(window, height=22, width=75)
chat_area.pack(pady=10)

message_entry = tk.Entry(window, width=50)
message_entry.pack(side=tk.LEFT, padx=10)

username = "Client"

def receive_messages():
    while True:
        try:
            encrypted_message = client.recv(1024)
            decrypted_message = cipher.decrypt(encrypted_message).decode()

            chat_area.insert(tk.END, f"\nEncrypted:\n{encrypted_message}\n")
            chat_area.insert(tk.END, f"Message:\n{decrypted_message}\n")

        except:
            break

def send_message():

    message = message_entry.get()

    timestamp = datetime.now().strftime("%H:%M:%S")

    formatted_message = f"[{timestamp}] {username}: {message}"

    encrypted_message = cipher.encrypt(formatted_message.encode())

    client.send(encrypted_message)

    message_entry.delete(0, tk.END)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

thread = threading.Thread(target=receive_messages)
thread.start()

window.mainloop()