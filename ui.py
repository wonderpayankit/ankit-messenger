import tkinter as tk
from tkinter import ttk, filedialog

# Function to create the modern UI layout
def create_ui():
    root = tk.Tk()
    root.title("Ankit Messenger")
    root.geometry("400x500")
    root.config(bg="#333")

    # Title label
    title_label = tk.Label(root, text="Ankit Messenger", font=("Helvetica", 16), fg="white", bg="#333")
    title_label.pack(pady=10)

    # User name input field
    name_label = tk.Label(root, text="Enter your name:", fg="white", bg="#333")
    name_label.pack(pady=5)
    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=5)

    # Listbox to show available users (for LAN discovery)
    user_listbox = tk.Listbox(root, height=10, width=30, font=("Helvetica", 12))
    user_listbox.pack(pady=5)
    user_listbox.insert(tk.END, "Discovering users...")

    # Message display area (Chat window)
    message_display = tk.Text(root, height=10, width=40, font=("Helvetica", 12), wrap=tk.WORD)
    message_display.pack(pady=5)
    message_display.config(state=tk.DISABLED)  # Make text widget non-editable

    # Message input field
    message_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
    message_entry.pack(pady=5)

    # Send button
    send_button = tk.Button(root, text="Send", width=15, bg="#4CAF50", fg="white", font=("Helvetica", 12))
    send_button.pack(pady=5)

    # File send button
    file_button = tk.Button(root, text="Send File", width=15, bg="#4CAF50", fg="white", font=("Helvetica", 12))
    file_button.pack(pady=5)

    # Return all UI elements
    return root, message_display, message_entry, send_button, file_button, name_entry, user_listbox
