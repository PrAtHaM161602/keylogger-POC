import socket
import threading 

FORMAT = "utf-8"
def handle_client(client_socket):
    while True:
        keys = client_socket.recv(1024)
        keys = keys.decode(FORMAT)
        print("")
        print(keys,end="")

def listen():
    IP = "127.0.0.1"
    PORT = 9999
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen()
    print("Server listening on port 9999")
    while True:
        client,addr = server.accept()
        client_thread = threading.Thread(target = handle_client,args=(client,))
        client_thread.start()

if __name__ == "__main__":
    listen()
