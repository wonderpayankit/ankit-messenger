import socket
import threading
import tkinter as tk
from ui import create_ui
from file_transfer import send_file, receive_file

# Global variables
SERVER_IP = '255.255.255.255'  # Broadcast IP for LAN communication
SERVER_PORT = 5000  # Port for communication
client_socket = None
user_name = "User"
discovered_users = {}  # Stores discovered users by their IP

# Create the GUI
root, message_display, message_entry, send_button, file_button, name_entry, user_listbox = create_ui()

# Function to update the message display area
def update_message_display(sender_name, message):
    message_display.config(state=tk.NORMAL)
    message_display.insert(tk.END, f"{sender_name}: {message}\n")
    message_display.config(state=tk.DISABLED)
    message_display.yview(tk.END)

# Function to send message
def send_message():
    global user_name
    message = message_entry.get()
    if message:
        selected_user = user_listbox.get(tk.ACTIVE)
        if selected_user in discovered_users:
            recipient_ip = discovered_users[selected_user]
            message_to_send = f"{user_name}: {message}"
            try:
                client_socket.sendto(message_to_send.encode('utf-8'), (recipient_ip, SERVER_PORT))
                update_message_display("You", message)
                message_entry.delete(0, 'end')
            except Exception as e:
                print(f"Error sending message: {e}")

# Function to handle incoming messages
def receive_message():
    while True:
        message, address = client_socket.recvfrom(1024)
        sender_name = f"Device {address[0]}"
        update_message_display(sender_name, message.decode('utf-8'))

# Start client and listen for incoming messages
def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client_socket.bind(('', SERVER_PORT))

    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_message, daemon=True)
    receive_thread.start()

    # Start a thread for device discovery
    discovery_thread = threading.Thread(target=discover_devices, daemon=True)
    discovery_thread.start()

# Function to discover devices
def discover_devices():
    global discovered_users
    while True:
        client_socket.sendto(f"DISCOVER:{user_name}".encode('utf-8'), (SERVER_IP, SERVER_PORT))
        message, address = client_socket.recvfrom(1024)
        if message.decode('utf-8').startswith("DISCOVER_REPLY"):
            device_name = message.decode('utf-8').split(":")[1]
            discovered_users[device_name] = address[0]
            user_listbox.insert(tk.END, device_name)

# Function to send file
def send_file_dialog(event=None):
    filename = filedialog.askopenfilename()  # Opens file explorer
    if filename:
        send_file(filename, SERVER_IP, SERVER_PORT)

# Function to receive file
def receive_file_dialog():
    receive_file(SERVER_IP, SERVER_PORT, save_as="received_file")

# Update name function
def update_name():
    global user_name
    user_name = name_entry.get()

# Set up send button
send_button.config(command=send_message)

# Set up file buttons
file_button.config(command=send_file_dialog)

# Set up name change
name_entry.bind("<Return>", lambda event: update_name())

# Start the client
start_client()

# Start the UI
root.mainloop()
