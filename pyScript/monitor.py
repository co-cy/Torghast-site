import socket


def request(adress, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((adress, port))
    print(client_socket.send(b'\xba'))
    data = client_socket.recv(1024)
    print(data)
    client_socket.close()
    data = str(data).replace('x00', '').replace('xa7', ' ').replace('\\', '')[2:-1].split()
    print(data)
    del data[0]
    return data
