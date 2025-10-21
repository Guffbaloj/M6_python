import socket
import threading
import time

LISTEN_PORT = 1050

def game_server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server: Skapat socket!")
    listen_socket.bind(("127.0.0.1", LISTEN_PORT))
    listen_socket.listen()
    connection, addr = listen_socket.accept()
    print(f"Server: Ansluten till: {addr}")
    number = int.from_bytes(connection.recv(1))
    print(f"Server: fick talet {number}")
    connection.send(b'\x01')
    connection.close()
    listen_socket.close()

def game_client():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.connect(("127.0.0.1", LISTEN_PORT))
    print("Klient: Ansluten!")
    listen_socket.send(b'\x05')
    print("Klient: Skickade talet 5!")
    listen_socket.close()

t = threading.Thread(target=game_server)
t.start()
time.sleep(1)
game_client()
