import socket

HOST = "127.0.0.1" #hostname
PORT = 65432 #port to be used by server

def run_func(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # s.sendall(b"Hello, Demitrus")
        s.sendall(bytes(data, 'utf-8'))
        data = s.recv(1024)

    print(f"Received: {data!r}")

run_func("this is a string")