import socket
import threading
import tkinter as tk

# Define a function to connect the client socket to the server's IP address and port number
def connect_to_server():
    # Get the host and port from the user input
    host = host_entry.get()
    port = int(port_entry.get())

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the client socket to the server's IP address and port number
    try:
        client_socket.connect((host, port))
    except:
        message_listbox.insert(tk.END, 'Error: Could not connect to server')
        return

    # Define a function to handle receiving messages from the server
    def receive_messages():
        while True:
            # Receive data from the server socket
            #UTF-8 is a character encoding 
            #buffer=1024
            data = client_socket.recv(1024).decode('utf-8')
            message_listbox.insert(tk.END, 'Received: ' + data)

    # Define a function to handle sending messages to the server
    def send_message():
        # Get input from the user
        message = message_entry.get()

        # Send the input to the server socket
        client_socket.sendall(message.encode('utf-8'))

        # Add the sent message to the chat box
        message_listbox.insert(tk.END, 'Sent: ' + message)

        # Clear the input field
        message_entry.delete(0, tk.END)

    # Create the GUI
    root = tk.Tk()
    root.title('Chat Box')

    # Create the message listbox
    message_listbox = tk.Listbox(root, height=20, width=80)
    message_listbox.pack(padx=10, pady=10)

    # Create the message entry field
    message_entry = tk.Entry(root, width=80)
    message_entry.pack(side=tk.LEFT, padx=10, pady=10)

    # Create the send button
    send_button = tk.Button(root, text='Send', command=send_message)
    send_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Start a new thread to handle receiving messages from the server
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    # Start the GUI main loop
    root.mainloop()

# Create the GUI for getting the host and port number from the user
connect_root = tk.Tk()
connect_root.title('Connect to Server')

# Create the host entry field
host_label = tk.Label(connect_root, text='Host:')
host_label.pack(side=tk.LEFT, padx=10, pady=10)

host_entry = tk.Entry(connect_root, width=50)
host_entry.pack(side=tk.LEFT, padx=10, pady=10)

# Create the port entry field
port_label = tk.Label(connect_root, text='Port:')
port_label.pack(side=tk.LEFT, padx=10, pady=10)

port_entry = tk.Entry(connect_root, width=10)
port_entry.pack(side=tk.LEFT, padx=10, pady=10)

# Create the connect button
connect_button = tk.Button(connect_root, text='Connect', command=connect_to_server)
connect_button.pack(side=tk.LEFT, padx=10, pady=10)

# Start the GUI main loop for getting the host and port number from the user
connect_root.mainloop()
