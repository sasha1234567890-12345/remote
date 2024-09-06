import socket
import threading
import subprocess

def handle_client(client_socket):
    while True:
        command = client_socket.recv(1024).decode('utf-8')
        if command.lower() == 'exit':
            break
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            client_socket.send(output)
        except Exception as e:
            client_socket.send(str(e).encode('utf-8'))
    client_socket.close()

def start_server():
    host = '0.0.0.0'  # Слушать на всех интерфейсах
    port = int(input("Введите порт для сервера: "))  # Запрос порта у пользователя
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Сервер запущен на {host}:{port} и ожидает подключения...")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Подключен к {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
