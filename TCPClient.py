import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 5000))

    message = input("Enter message: ")
    client_socket.sendall((message + "\n").encode())

    response = client_socket.recv(1024).decode().strip()
    print("From Server:", response)

    client_socket.close()

if __name__ == "__main__":
    main()