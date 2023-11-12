import socket

# Create a non-blocking socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)

# Connect to a server
server_address = ('example.com', 8080)
try:
    sock.connect(server_address)
except BlockingIOError:
    pass  # Connection in progress, not an error in non-blocking mode

# Set up a non-blocking socket for reading
sock.settimeout(0.0)

while True:
    try:
        data = sock.recv(1024)
        if data:
            print("Received:", data)
        else:
            break  # No more data, connection closed
    except BlockingIOError:
        # No data available, continue with other tasks
        pass

# Continue with other tasks or close the socket as needed
