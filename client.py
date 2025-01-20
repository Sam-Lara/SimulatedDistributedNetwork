import socket
import threading

# source: https://huichen-cs.github.io/course/CISC7334X/20FA/lecture/pymcast/
def receive_multicast():
    grpIP = '224.1.1.1' # Specifying our master node for multicast 
    grpPort = 5007
    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    receiver.bind((grpIP, grpPort))
    mreq = socket.inet_aton(grpIP) + socket.inet_aton('0.0.0.0')
    receiver.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        data, _ = receiver.recvfrom(1024)
        print("Received multicast message:", data.decode(), flush=True)


# sources for unicast
# https://docs.python.org/3/library/socket.html
# CECS 326 Lab 01
def initialize_client_unicast():
    try:
        # initalize a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect client socket to the server socket
        server_socket_address = ("master", 10000)
        client_socket.connect(server_socket_address)

        # infinite while loop to continue messaging server
        while 1:
            client_message = "Yay Area!!!"
            # send and receieve messages
            client_socket.sendall(client_message.encode())
            data = client_socket.recv(512)
            print(f"Received unicast message: {data.decode()}", flush=True)
    except KeyboardInterrupt as error:
        print(f"\nDiscconnected from server {error}")
        client_socket.close()


def main():
    unicast_client = threading.Thread(target=initialize_client_unicast)
    multicast_client = threading.Thread(target=receive_multicast)

    unicast_client.start()
    multicast_client.start()


if __name__ == "__main__":
    main()
