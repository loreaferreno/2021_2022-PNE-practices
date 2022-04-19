class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK!")

    def talk(self, msg):
        import socket

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.ip, self.port))

        msg_bytes = str.encode(msg)
        client_socket.send(msg_bytes)

        response_bytes = client_socket.recv(2048)
        response = response_bytes.decode("utf-8")

        client_socket.close()

        return response

    def debug_talk(self, msg):
        import socket
        import termcolor

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.ip, self.port))

        print("To server: ", end="")
        termcolor.cprint(msg, 'blue')
        msg_bytes = str.encode(msg)
        client_socket.send(msg_bytes)

        response_bytes = client_socket.recv(2048)
        response = response_bytes.decode("utf-8")
        print("From server: ", end="")
        termcolor.cprint(response, 'green')

        client_socket.close()

        return response

