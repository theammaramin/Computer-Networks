

import socket
import threading
import tkinter as tk
port=5555 #initial Value
# create the main window
window = tk.Tk()

# create the input box and button
label = tk.Label(window, text="Enter the port number...")
label.pack()
entry = tk.Entry(window)
entry.insert(0, "5555")
button = tk.Button(window, text="Submit", command=window.quit)

# add the input box and button to the window
entry.pack()

button.pack()

# start the main event loop
window.mainloop()

# get the value of the input box and assign it to a variable
port =int( entry.get())

print("User input stored:", port)



# Define server settings
host = '127.0.0.1'
#port = 8089

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket object to a specific IP address and port number
# binding is the process of associating a network socket with a specific network interface and port number on a local machine.
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen()

# Create a list to store all connected client sockets
client_sockets = []

# function to handle incoming client connections
def handle_client_connection(client_socket, client_address):
    # Add the client socket to the list of connected client sockets
    client_sockets.append(client_socket)
    print(f'New client connected: {client_address}')

    while True:
        # Receive data from the client socket
        data = client_socket.recv(1024).decode('utf-8')

        if not data:
            # If no data was received, remove the client socket 
            client_sockets.remove(client_socket)
            print(f'Client disconnected: {client_address}')
            break

        # Send the received data to all connected client sockets except the sender
        for socket in client_sockets:
            if socket != client_socket:
                socket.sendall(f'{client_address[0]}:{client_address[1]} > {data}'.encode('utf-8'))


# Main loop to handle incoming connections
while True:
    # Wait for an incoming client connection
    client_socket, client_address = server_socket.accept()

    # Create a new thread to handle the incoming client connection
    client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, client_address))
    client_thread.start()

