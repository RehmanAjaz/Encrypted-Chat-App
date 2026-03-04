Encrypted Chat Application 🔐💬

A secure client-server chat application built using Python, TCP Socket Programming, and AES Encryption.
This project demonstrates how encrypted communication can be implemented to protect messages from interception during transmission.

The application includes a graphical user interface (GUI) built with Tkinter, allowing users to send and receive encrypted messages in real time.

Project Overview

This project implements a secure messaging system where:

Messages are encrypted before sending

The server receives encrypted data

Messages are decrypted and displayed

Multiple clients can communicate with the server simultaneously

The goal of this project is to demonstrate secure communication using cryptography and socket programming.

Features

AES-based encryption using cryptography library

TCP socket communication

Client-Server architecture

Multi-client support using threading

Tkinter GUI interface

Encrypted and decrypted message display

Real-time messaging

Message timestamp support

Technologies Used
Technology	Purpose
Python	Programming language
Socket	Network communication
Threading	Handle multiple clients
Cryptography (Fernet)	AES encryption
Tkinter	GUI interface
Datetime	Message timestamps
System Architecture
Client 1  ----\
               \
Client 2  ------->  Server  ----> Broadcast Messages
               /
Client 3  ----/

Workflow:

Server starts and listens on a specific port

Clients connect to the server

Client encrypts message using AES key

Encrypted message is sent to the server

Server decrypts and displays the message

Server broadcasts the message to other clients

Installation
1 Install Python

Download Python from:

https://www.python.org/downloads/

2 Install Required Library

Run the following command:

pip install cryptography
Running the Application
Step 1: Start the Server
python server.py

Server will start listening for incoming client connections.

Step 2: Start the Client

Open another terminal and run:

python client.py

You can run multiple clients to simulate multiple users.

Example Output

Server receives encrypted message:

Encrypted:
b'gAAAAABl...'

Server decrypts message:

[14:32:10] Client: Hello Server
Project Structure
Encrypted-Chat-App
│
├── server.py
├── client.py
├── README.md
└── screenshots
Security Implementation

This project uses Fernet encryption from the cryptography library, which is based on AES (Advanced Encryption Standard).

Security benefits:

Ensures message confidentiality

Prevents unauthorized access

Protects communication from network sniffing

Future Improvements

Possible improvements include:

User authentication system

End-to-end encryption

File sharing support

Group chat functionality

Dark mode interface

Database for message history

Deployment on cloud server

Learning Outcomes

This project helps understand:

Socket programming in Python

Client-server communication

Cryptographic encryption

GUI development with Tkinter

Multi-threaded applications

Author

Your Name

License

This project is for educational purposes and can be freely modified and used for learning.
