import socket

host = ''
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        with conn:
            print("connected:", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode("utf-8"))
