import socket


def request(adress, port):
    # TODO optimize time load
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((adress, port))
        client_socket.send(b"\xFE")
        data = client_socket.recv(1024)
        client_socket.close()
        data = str(data).replace('x00', '').replace('xa7', ' ').replace('\\', '')[2:-1].split()
        del data[0]
        data = [data[0] + ' ' + data[1], data[2] + '/' + data[3]]
        return data
    except ConnectionRefusedError:
        return ['Offline', '0/20']
