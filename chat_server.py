import socket
import threading

HOST = '127.0.0.1'  # localhost
PORT = 12345        # Port to listen on

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"[{addr}] {msg}")
        except:
            break
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

def send_messages(conn):
    while True:
        msg = input()
        conn.send(msg.encode())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    conn, addr = server.accept()
    
    # Start receiving and sending threads
    threading.Thread(target=handle_client, args=(conn, addr)).start()
    threading.Thread(target=send_messages, args=(conn,)).start()

if __name__ == "__main__":
    main()



