import socket
import os

# Function to send a file
def send_file(file_path, server_ip, server_port):
    try:
        file_size = os.path.getsize(file_path)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        with open(file_path, 'rb') as file:
            # Send file size first
            client_socket.sendto(str(file_size).encode('utf-8'), (server_ip, server_port))
            # Send the actual file
            while (data := file.read(1024)):
                client_socket.sendto(data, (server_ip, server_port))
        print(f"File '{file_path}' sent successfully.")
    except Exception as e:
        print(f"Error sending file: {e}")

# Function to receive a file
def receive_file(server_ip, server_port, save_as="received_file"):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((server_ip, server_port))

        # Receive file size
        file_size, _ = server_socket.recvfrom(1024)
        file_size = int(file_size.decode('utf-8'))

        # Receive the file data
        with open(save_as, 'wb') as file:
            bytes_received = 0
            while bytes_received < file_size:
                data, _ = server_socket.recvfrom(1024)
                file.write(data)
                bytes_received += len(data)
        print(f"File received and saved as {save_as}.")
    except Exception as e:
        print(f"Error receiving file: {e}")
