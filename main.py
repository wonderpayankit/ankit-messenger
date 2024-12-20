import socket
import threading
import tkinter as tk
from tkinter import filedialog
from ui import create_ui  # Only import create_ui now
from file_transfer import send_file, receive_file

# Global variables
SERVER_IP = '127.0.0.1'  # Local IP address (for testing on your own machine)
SERVER_PORT = 5000       # Port for communication
client_socket = None

# Create the GUI
root, message_entry, send_button, update_message_display, file_button, receive_file_button = create_ui()

# Function to send message to server
def send_message():
    message = message_entry.get()
    if message:
        try:
            client_socket.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))
            message_entry.delete(0, 'end')
            update_message_display(f"You: {message}")
        except Exception as e:
            print(f"Error sending message: {e}")

# Server communication - Listening for messages
def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(('0.0.0.0', SERVER_PORT))

    while True:
        data, address = client_socket.recvfrom(1024)  # Receive message from server
        update_message_display(f"Friend: {data.decode('utf-8')}")

# Start the client and listen for incoming messages
client_thread = threading.Thread(target=start_client, daemon=True)
client_thread.start()

# Set up the send button to trigger the send_message function
send_button.config(command=send_message)

# File transfer button functionality
def send_file_dialog():
    filename = filedialog.askopenfilename()  # Opens file explorer
    if filename:
        send_file(filename, SERVER_IP, SERVER_PORT)  # Send file using the IP and port

# File reception functionality
def receive_file_dialog():
    receive_file(SERVER_IP, SERVER_PORT, save_as="received_file")

# Set up the file buttons for sending and receiving
file_button.config(command=send_file_dialog)
receive_file_button.config(command=receive_file_dialog)

# Start the Tkinter UI
root.mainloop()
