import socket
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind((socket.gethostname(),1347))
sk.listen()
while True:
    client,address=sk.accept()
    print("connection established")
    print(address)
    client.send(b"socket programming")