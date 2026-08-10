import socket
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5000))
    server_socket.listen(1)
    print("Server started... Waiting for client")

    client_socket, addr = server_socket.accept()
    print("Client connected:", addr)

    message = client_socket.recv(1024).decode().strip()
    print("Received from client:", message)

    upper_message = message.upper()
    client_socket.sendall((upper_message + "\n").encode())
    print("Sent to client:", upper_message)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()