import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 12345

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Server listening on port", PORT)
    conn, addr = server_socket.accept()
    print("Client connected:", addr)

    while True:
        data = conn.recv(1024).decode()
        if not data or data == "exit":
            break
        print("Server received:", data)
        conn.send(data.encode())

    conn.close()
    server_socket.close()

def client():
    time.sleep(1)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    messages = ["hello", "world", "exit"]

    for msg in messages:
        client_socket.send(msg.encode())
        if msg == "exit":
            break
        data = client_socket.recv(1024).decode()
        print("Client received:", data)

    client_socket.close()

t1 = threading.Thread(target=server)
t2 = threading.Thread(target=client)

t1.start()
t2.start()

t1.join()
t2.join()
