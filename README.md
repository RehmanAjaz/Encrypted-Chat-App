# 🔐 Encrypted Chat Application

A secure client-server chat application built with **Python**, **TCP Socket Programming**, and **AES Encryption** (via Fernet). Messages are encrypted before transmission, ensuring confidentiality even if intercepted on the network. A **Tkinter GUI** provides a clean, real-time messaging interface.

---

## 📌 Project Overview

This project demonstrates secure communication using cryptography and socket programming. The core workflow is:

1. Server starts and listens on a specified port
2. Clients connect to the server
3. Client encrypts the message using an AES (Fernet) key
4. Encrypted message is sent over TCP to the server
5. Server decrypts and displays the message
6. Server broadcasts the decrypted message to all connected clients

```
Client 1 ──┐
Client 2 ──┼──▶  Server  ──▶  Broadcast to All Clients
Client 3 ──┘
```

---

## ✨ Features

- 🔒 AES-based encryption using the `cryptography` (Fernet) library
- 🌐 TCP socket communication
- 🖥️ Client-Server architecture
- 👥 Multi-client support via threading
- 🖼️ Tkinter GUI with encrypted and decrypted message display
- ⏱️ Real-time messaging with message timestamps

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Socket | TCP network communication |
| Threading | Handle multiple simultaneous clients |
| Cryptography (Fernet) | AES-based symmetric encryption |
| Tkinter | Graphical user interface |
| Datetime | Message timestamps |

---

## 📁 Project Structure

```
Encrypted-Chat-App/
│
├── server.py        # Server-side logic (accept, decrypt, broadcast)
├── client.py        # Client-side GUI and encryption logic
├── README.md        # Project documentation
└── screenshots/     # UI screenshots (optional)
```

---

## ⚙️ Installation

### 1. Prerequisites

- Python 3.7 or higher — [Download here](https://www.python.org/downloads/)

### 2. Install Required Library

```bash
pip install cryptography
```

---

## 🚀 Running the Application

### Step 1 — Start the Server

```bash
python server.py
```

The server will begin listening for incoming client connections.

### Step 2 — Start a Client

Open a **new terminal** and run:

```bash
python client.py
```

Repeat this step in additional terminals to simulate multiple users.

---

## 🖥️ Example Output

**Server terminal — encrypted message received and decrypted:**

```
[*] Waiting for connections...
[+] Client connected: ('127.0.0.1', 54321)

Encrypted : b'gAAAAABl...'
Decrypted : [14:32:10] Client: Hello Server
```

---

## 🔐 Security Implementation

This project uses **Fernet encryption** from Python's `cryptography` library, which is built on top of AES-128 in CBC mode with HMAC-SHA256 for authentication.

**Security benefits:**
- Ensures message **confidentiality** — data is unreadable in transit
- Provides **integrity checking** — tampered messages are rejected
- Protects against **network sniffing and packet capture**
- Uses a **shared symmetric key** for encryption and decryption

> ⚠️ **Note:** This project uses a pre-shared symmetric key for simplicity. For production use, consider asymmetric key exchange (e.g., Diffie-Hellman) to establish the key securely.

---

## 🔮 Future Improvements

- [ ] User authentication (username + password)
- [ ] End-to-end encryption with asymmetric key exchange
- [ ] File and image sharing support
- [ ] Group chat / channel support
- [ ] Dark mode GUI theme
- [ ] Persistent message history with database integration
- [ ] Cloud deployment (AWS / DigitalOcean)

---

## 📚 Learning Outcomes

Working on this project helps you understand:

- TCP socket programming in Python
- Client-server communication architecture
- Symmetric cryptographic encryption (AES/Fernet)
- GUI development with Tkinter
- Multi-threaded server design

---



---

## 📄 License

This project is intended for **educational purposes**. Feel free to use, modify, and build upon it for learning and non-commercial applications.
