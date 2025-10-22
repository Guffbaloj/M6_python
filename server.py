import socket
import struct
import sys
import threading
import time

MESSAGE_NONE = 0
MESSAGE_PLAYER_JOIN = 1
MESSAGE_PLAYER_MOVE = 2

class Message:
    def apply():
        pass
    def get_type():
        return MESSAGE_NONE
    def get_bytes():
        return b""

class PlayerJoinMessage(Message):
    def __init__(self, data):
        ...
    def get_type(): return MESSAGE_PLAYER_JOIN
    def get_bytes(): return b''

# Tuppel av (x,y)
MOVE_MESSAGE_STRUCT = ">ii"
class PlayerMoveMessage(Message):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_type(self): return MESSAGE_PLAYER_MOVE
    def get_bytes(self):
        return struct.pack(MOVE_MESSAGE_STRUCT, self.x, self.y)

# Tuppel av (antal bytes, meddelandetyp)
MESSAGE_HEADER_STRUCT = ">hh"

def send_message(sock: socket.socket, message: Message):
    data = message.get_bytes()
    type = message.get_type()
    header_data = struct.pack(MESSAGE_HEADER_STRUCT, len(data), type)
    print(f"Skickar meddelande: {header_data}")
    sock.sendall(header_data)
    sock.sendall(data)

def read_message(sock: socket.socket):
    header = sock.recv(struct.calcsize(MESSAGE_HEADER_STRUCT))
    if len(header) == 0:
        return None

    size, message_type = struct.unpack(MESSAGE_HEADER_STRUCT, header)
    data = sock.recv(size)
    if message_type == MESSAGE_PLAYER_MOVE:
        x, y = struct.unpack(MOVE_MESSAGE_STRUCT, data)
        return PlayerMoveMessage(x, y)

LISTEN_PORT = 1050

def game_server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server: Skapat socket!")
    listen_socket.bind(("0.0.0.0", LISTEN_PORT))
    listen_socket.listen()
    connection, addr = listen_socket.accept()
    print(f"Server: Ansluten till: {addr}")
    while True:
        msg = read_message(connection)
        if msg:
            if msg.get_type() == MESSAGE_PLAYER_MOVE:
                print(f"Msg: PLAYER_MOVE: {msg.x}, {msg.y}")
        # data = connection.recv(1)
        # if len(data) == 1:
        #     number = int.from_bytes(data)
        #     print(f"Server: fick talet {number}")
    connection.close()
    listen_socket.close()

def game_client():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.connect(("le-serv", LISTEN_PORT))
    print("Klient: Ansluten!")
    send_message(listen_socket, PlayerMoveMessage(4,7))
    print("Klient: Skickade talet 5!")
    listen_socket.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'server':
            game_server()
        elif sys.argv[1] == 'client':
            game_client()
    else:
        t = threading.Thread(target=game_server)
        t.start()
        time.sleep(1)
        game_client()
