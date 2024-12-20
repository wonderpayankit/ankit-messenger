import tkinter as tk

# Function to create the user interface (UI)
def create_ui():
    root = tk.Tk()
    root.title("Ankit Massanger")

    # Name input field
    name_label = tk.Label(root, text="Enter your name:")
    name_label.pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    # Message display area
    message_display = tk.Text(root, height=15, width=50)
    message_display.pack(pady=5)
    message_display.config(state=tk.DISABLED)  # Make text widget non-editable

    # Message input field
    message_entry = tk.Entry(root, width=40)
    message_entry.pack(pady=5)

    # Send button
    send_button = tk.Button(root, text="Send")
    send_button.pack(pady=5)

    # File send button (optional)
    file_button = tk.Button(root, text="Send File")
    file_button.pack(pady=5)

    # Return all necessary UI elements
    return root, message_display, message_entry, send_button, file_button, name_entry
