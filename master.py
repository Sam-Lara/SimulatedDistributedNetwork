import socket
import threading  # for handling multiple clients
import time  # for consistent sending of messages

# source: https://huichen-cs.github.io/course/CISC7334X/20FA/lecture/pymcast/
def master_mc():
    grpIP = '224.1.1.1'
    grpPort = 5007
    sender = socket.socket(family= socket.AF_INET, type= socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP, fileno=None)
    sender.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    msg = b"Master sends this multicast message!"
    while True:
        mcgrp = (grpIP, grpPort)
        sender.sendto(msg, mcgrp)
        time.sleep(1)

# sources for unicast
# https://docs.python.org/3/library/socket.html
# CECS 326 Lab 01
def initialize_master_unicast():
    # create a socket object and bind it to a socket address
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = "0.0.0.0"
    server_port = 10000
    server_socket_address = (server_address, server_port)
    server_socket.bind(server_socket_address)

    # listen for up to 5 client connections
    server_socket.listen(5)
    print(f"Server is listening for connections on {server_address}:{server_port}")
    try:
        # continuously connect up to the 5 clients
        while True:
            client_socket, client_address = server_socket.accept()
            # create a thread for each client connection to allow all clients to communicate simultaneously
            client = threading.Thread(target=client_connection, args=(client_socket, client_address))
            # start running the client -> calls client_connection()
            client.start()
    except KeyboardInterrupt:
        print("\nServer is shutting down...")
        # Close the server socket
        server_socket.close()


def client_connection(client_socket, client_address):
    print(f"Connected to {client_address}")
    # accept messages from client until disconnection
    while True:
        message = client_socket.recv(1024)
        # check if the message is None
        if not message:
            print(f"Client {client_address} disconnected", flush=True)
            break
        print(f"{client_address}: {message.decode()}", flush=True)
        # acknowledge message was received from client
        client_socket.sendall(bytes(f"receieved message '{message}'", "ASCII"))
        # sleep the thread 1 second to have slower messaging
        time.sleep(1)
    # close the client socket once it disconnects
    client_socket.close()

# Threading Source: https://docs.python.org/3/library/threading.html
def main():
    unicast_thread = threading.Thread(target=initialize_master_unicast)
    multicast_thread = threading.Thread(target=master_mc)

    # Start the threads
    unicast_thread.start()
    multicast_thread.start()

    # Wait for the threads to complete if they even do
    unicast_thread.join()
    multicast_thread.join()


if __name__ == "__main__":
    main()
