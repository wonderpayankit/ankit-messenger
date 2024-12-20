import os
import socket

def send_file(filename, server_ip, server_port):
    try:
        with open(filename, 'rb') as file:
            file_data = file.read()
        # Send file data to the server
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            client_socket.sendto(file_data, (server_ip, server_port))
        print(f"File {filename} sent successfully.")
    except Exception as e:
        print(f"Error sending file: {e}")

def receive_file(server_ip, server_port, save_as):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
            server_socket.bind((server_ip, server_port))
            file_data, address = server_socket.recvfrom(1024 * 1024)  # Receive file data (up to 1MB)
            with open(save_as, 'wb') as f:
                f.write(file_data)
        print(f"File received and saved as {save_as}.")
    except Exception as e:
        print(f"Error receiving file: {e}")
