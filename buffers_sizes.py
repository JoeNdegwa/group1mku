import socket

def modify_buffer_sizes(sock, send_buffer_size, receive_buffer_size):
    # Set the send buffer size
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, send_buffer_size)

    # Set the receive buffer size
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, receive_buffer_size)

def main():
    # Example server address
    server_address = ('localhost', 12345)

    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Print the default buffer sizes
    default_send_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    default_receive_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

    print(f"Default Send Buffer Size: {default_send_buffer_size} bytes")
    print(f"Default Receive Buffer Size: {default_receive_buffer_size} bytes")

    # Modify the buffer sizes
    new_send_buffer_size = 8192  # Set your desired send buffer size
    new_receive_buffer_size = 8192  # Set your desired receive buffer size

    modify_buffer_sizes(sock, new_send_buffer_size, new_receive_buffer_size)

    # Print the modified buffer sizes
    modified_send_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    modified_receive_buffer_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

    print(f"Modified Send Buffer Size: {modified_send_buffer_size} bytes")
    print(f"Modified Receive Buffer Size: {modified_receive_buffer_size} bytes")

    # Close the socket
    sock.close()

if __name__ == "__main__":
    main()
