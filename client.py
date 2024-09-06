import socket

def start_client():
    host = input("Введите хост сервера: ")  # Запрос хоста у пользователя
    port = int(input("Введите порт сервера: "))  # Запрос порта у пользователя
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        command = input("Введите команду: ")
        client.send(command.encode('utf-8'))
        if command.lower() == 'exit':
            break
        
        # Получение данных от сервера
        output = b""
        while True:
            part = client.recv(4096)
            output += part
            if len(part) < 4096:  # Если полученный пакет меньше максимального размера, значит, это последний пакет
                break
        
        try:
            print(output.decode('utf-8'))
        except UnicodeDecodeError:
            try:
                print(output.decode('latin-1'))  # Попробуйте другую кодировку
            except UnicodeDecodeError:
                print("Ошибка декодирования. Полученные данные не являются текстом.")

    client.close()

if __name__ == "__main__":
    start_client()
