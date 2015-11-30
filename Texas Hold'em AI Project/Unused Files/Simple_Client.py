#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     This program tests the connection to a local server using sockets.
#              It's pointless really.
#
# Author:      carricktel
#
# Created:     03/10/2015
# Copyright:   (c) carricktel 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket

Host = '127.0.0.1'
Port = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host,Port))

while 1:
    gamestate = raw_input("game state: ")
    if gamestate == "close":
        break
    s.sendall(str(gamestate))
    data = s.recv(1024)
    print repr(data)
s.close()
