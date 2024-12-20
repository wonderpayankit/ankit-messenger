import socket

# Function to send a file
def send_file(filename, target_ip, target_port):
    try:
        with open(filename, 'rb') as file:
            file_data = file.read(1024)  # Read in chunks of 1024 bytes
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while file_data:
                client_socket.sendto(file_data, (target_ip, target_port))  # Send data chunk
                file_data = file.read(1024)
            print("File sent successfully!")
            client_socket.close()
    except Exception as e:
        print(f"Error sending file: {e}")

# Function to receive a file
def receive_file(target_ip, target_port, save_as="received_file"):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((target_ip, target_port))

        with open(save_as, 'wb') as file:
            while True:
                file_data, address = server_socket.recvfrom(1024)
                if not file_data:
                    break
                file.write(file_data)  # Write received data to file
            print(f"File received and saved as {save_as}")
        server_socket.close()
    except Exception as e:
        print(f"Error receiving file: {e}")
