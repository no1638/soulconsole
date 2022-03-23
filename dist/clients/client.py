import socket
import os
from os import name as os_name, system
from colorama import init, Fore as cc
import select
import time
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET
HEADER = 64
clear = lambda: system('cls') if os_name == 'nt' else system('clear')
clear()
PORT = input("Enter Port Number > ")
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!disconnect"
SERVER = input("Enter Tunnel Address > ")
PORT1 = int(PORT)
ADDR = (SERVER, PORT1)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

clear()
print("To disconnect type !disconnect\n")
def sendmsg():
    inp = input("\nInput Command > ")
    if inp == "clear":
        clear()
    if inp:
        client.send(str.encode(inp))
        print("\n" + client.recv(2048).decode(FORMAT))
        sendmsg()
    if not inp:
        print(f"{r}INVALID INPUT{w}")
        sendmsg()
sendmsg()
exit()
    