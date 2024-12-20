import tkinter as tk
import tkinter.filedialog

def create_ui():
    # Set up the main window
    root = tk.Tk()
    root.title("Ankit Messenger")

    # Add a text box to display the messages
    text_box = tk.Text(root, width=50, height=15, state='disabled')
    text_box.pack(padx=10, pady=10)

    # Add an entry box to type messages
    message_entry = tk.Entry(root, width=40)
    message_entry.pack(padx=10, pady=10)

    # Add a send button
    send_button = tk.Button(root, text="Send")
    send_button.pack(padx=10, pady=10)

    # Add a button to send files
    file_button = tk.Button(root, text="Send File")
    file_button.pack(padx=10, pady=10)

    # Add a button to receive files
    receive_file_button = tk.Button(root, text="Receive File")
    receive_file_button.pack(padx=10, pady=10)

    # Function to update the display with new messages
    def update_message_display(message):
        text_box.config(state='normal')
        text_box.insert(tk.END, message + "\n")
        text_box.config(state='disabled')
        text_box.yview(tk.END)

    # Return necessary components for use in main.py
    return root, message_entry, send_button, update_message_display, file_button, receive_file_button
