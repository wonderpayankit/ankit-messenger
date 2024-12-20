import socket
import threading
import tkinter as tk
from ui import create_ui
from file_transfer import send_file, receive_file

# Global variables
SERVER_IP = '127.0.0.1'  # Local IP address (for testing on your own machine)
SERVER_PORT = 5000       # Port for communication
client_socket = None
name = "User"  # Default name

# Create the GUI
root, message_display, message_entry, send_button, file_button, name_entry = create_ui()

# Function to update the message display area
def update_message_display(sender_name, message):
    message_display.config(state=tk.NORMAL)
    message_display.insert(tk.END, f"{sender_name}: {message}\n")
    message_display.config(state=tk.DISABLED)
    message_display.yview(tk.END)  # Scroll to the latest message

# Function to send message to the server
def send_message():
    global name
    message = message_entry.get()
    if message:
        try:
            # Send message along with the sender's name
            message_to_send = f"{name}: {message}"
            client_socket.sendto(message_to_send.encode('utf-8'), (SERVER_IP, SERVER_PORT))
            update_message_display("You", message)
            message_entry.delete(0, 'end')
        except Exception as e:
            print(f"Error sending message: {e}")

# Function to handle incoming messages from the server (other clients)
def receive_message():
    while True:
        message, _ = client_socket.recvfrom(1024)
        update_message_display("Friend", message.decode('utf-8'))

# Function to start the client and listen for messages
def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
    client_socket.bind(('', 0))  # Bind to any available port

    # Start a thread to listen for incoming messages
    receive_thread = threading.Thread(target=receive_message, daemon=True)
    receive_thread.start()

# Function to send file
def send_file_dialog():
    filename = filedialog.askopenfilename()  # Opens file explorer
    if filename:
        send_file(filename, SERVER_IP, SERVER_PORT)  # Send file using the IP and port

# Function to receive file
def receive_file_dialog():
    receive_file(SERVER_IP, SERVER_PORT, save_as="received_file")

# Function to update the name
def update_name():
    global name
    name = name_entry.get()
    print(f"Name updated to: {name}")

# Set up the send button to trigger the send_message function
send_button.config(command=send_message)

# Set up the file buttons for sending and receiving
file_button.config(command=send_file_dialog)

# Set up the name update functionality
name_entry.bind("<Return>", lambda event: update_name())  # Press Enter to update name

# Start the client and listen for incoming messages
start_client()

# Start the Tkinter UI
root.mainloop()
