import socket
import threading

HOST = '127.0.0.1'  # Server's IP address
PORT = 12345        # Server's port

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(f"[Server] {msg}")
        except:
            print("Connection closed.")
            break

def send_messages(sock):
    while True:
        msg = input()
        sock.send(msg.encode())

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    threading.Thread(target=receive_messages, args=(client,)).start()
    threading.Thread(target=send_messages, args=(client,)).start()

if __name__ == "__main__":
    main()

