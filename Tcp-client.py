import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 12345

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Server started...")
    conn, addr = server_socket.accept()
    print("Client connected")

    while True:
        message = conn.recv(1024).decode()

        if message == "bye":
            reply = "Goodbye Client!"
            conn.send(reply.encode())
            break
        elif message == "hai":
            reply = "Hello Client!"
        elif message == "how are you":
            reply = "I'm fine, thank you!"
        elif message == "what's your name":
            reply = "I am the chat server"
        else:
            reply = "I didn't understand that."

        print("Client:", message)
        conn.send(reply.encode())

    conn.close()
    server_socket.close()

def client():
    time.sleep(1)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Client connected to server")

    while True:
        msg = input("Client: ")
        client_socket.send(msg.encode())

        response = client_socket.recv(1024).decode()
        print("Server:", response)

        if msg == "bye":
            break

    client_socket.close()

t1 = threading.Thread(target=server)
t2 = threading.Thread(target=client)

t1.start()
t2.start()

t1.join()
t2.join()
