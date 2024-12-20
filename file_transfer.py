import socket

# Function to send files
def send_file(filename, server_ip, server_port):
    try:
        with open(filename, 'rb') as file:
            file_data = file.read()
        # Send file data
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            client_socket.sendto(file_data, (server_ip, server_port))
        print(f"File {filename} sent successfully.")
    except Exception as e:
        print(f"Error sending file: {e}")

# Function to receive files
def receive_file(server_ip, server_port, save_as="received_file"):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
            server_socket.bind((server_ip, server_port))
            file_data, address = server_socket.recvfrom(1024 * 1024)  # Receive file data
            with open(save_as, 'wb') as f:
                f.write(file_data)
        print(f"File received and saved as {save_as}.")
    except Exception as e:
        print(f"Error receiving file: {e}")
