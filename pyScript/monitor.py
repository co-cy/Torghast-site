from socket import socket, AF_INET, SOCK_STREAM
from main import config
from time import sleep


def request(adress, port):
    client_socket = socket(AF_INET, SOCK_STREAM)
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


def while_function():
    while True:
        for name_server in config['servers']:
            ip, port = config['servers'][name_server].split(':')
            # TODO заменить запись в файл на работу с памятью.
            k = request(ip, int(port))
            with open('monitor_info.txt', 'w') as f:
                f.write('&'.join(k))
            sleep(10)