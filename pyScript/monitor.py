from socket import socket, AF_INET, SOCK_STREAM
from json import load
from time import sleep

servers = {}


def info_all_servers():
    return servers


def request(ip, port) -> tuple:
    client_socket = socket(AF_INET, SOCK_STREAM)
    try:
        client_socket.connect((ip, port))
        client_socket.send(b"\xFE")
        data = client_socket.recv(1024)
        client_socket.close()
        data = str(data).replace('x00', '').replace('xa7', ' ').replace('\\', '')[2:-1].split()
        return data[3], data[4]
    except ConnectionRefusedError:
        return 'Offline', 'Offline'


def endless_checking_servers(config):
    global servers

    count = 0
    while True:
        if count == 5:
            # Каждые 5 минут автоподгрузка серверов
            try:
                # TODO сделать безопастное открытие
                with open('config.json') as file:
                    config = load(file)
            except Exception as a:
                print('Ну пофикси', a)
            count = 0
        # TODO доделать добавление в базу данных
        new_servers = {}
        for server in config['minecraft_servers']:
            new_servers[server['name']] = request(server['ip'], server['port'])
        servers = new_servers

        sleep(60)