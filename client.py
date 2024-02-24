import socket

host = 'altai'
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    with open("client.py", "rb") as f:
        sock.sendfile(f)
