import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(('127.0.0.1', 8000))
client.send("echuan".encode("utf8"))
client.close()