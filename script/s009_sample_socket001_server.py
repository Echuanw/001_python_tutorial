"""
            Server                                                                            Client
        1 create Socket
        2 bind(protocol, address, port) 
        3 listen(request from clent)                                                       
        4 accept()                                                                         1 socket
   ---> 5 block or wait request     <---------Three-way handshake-----------------         2 connect()
   |    6 recv()                    <---------------------------------------------         3 send()
   ---- 7 send()                    --------------------------------------------->         4 recv()
        8 close()                   <---------------------------------------------         5 close()
"""

import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000,))
server.listen()
sock, addr = server.accept()

# 接受数据
data = b""
while True:
     d = sock.recv(1024)
     if d:
          data += d
     else:
          break

# 输出数据
data = data.decode("utf8")
print(data)

# 关闭
server.close()
sock.close()