#!/usr/bin/env python3
Server = __import__('1-simple_pagination').Server
server = Server()
print(server.get_page(1, 3))
print(server.get_page(3, 2))
