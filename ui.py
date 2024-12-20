import tkinter as tk

# Function to create the UI
def create_ui():
    root = tk.Tk()
    root.title("IP Messenger")

    # Message display area
    message_display = tk.Text(root, height=15, width=50, state=tk.DISABLED)
    message_display.grid(row=0, column=0, padx=10, pady=10)

    # Message entry field
    message_entry = tk.Entry(root, width=40)
    message_entry.grid(row=1, column=0, padx=10, pady=10)

    # Send button
    send_button = tk.Button(root, text="Send", width=20)
    send_button.grid(row=2, column=0, padx=10, pady=10)

    # File button
    file_button = tk.Button(root, text="Send File", width=20)
    file_button.grid(row=3, column=0, padx=10, pady=10)

    # User list box
    user_listbox = tk.Listbox(root, height=10, width=20)
    user_listbox.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

    # Name entry field
    name_label = tk.Label(root, text="Enter your name:")
    name_label.grid(row=4, column=0, padx=10, pady=10)
    name_entry = tk.Entry(root, width=20)
    name_entry.grid(row=4, column=1, padx=10, pady=10)

    return root, message_display, message_entry, send_button, file_button, name_entry, user_listbox
