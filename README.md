# Soul Console
Soul Console: A simple backdoor console (3 options) to start pentesting and experimenting


Python Reqs
>python 3.6+


How to use:
Install dependencies onto your machine using:
>pip install -r requirements.txt


**Setup:**

Navigate to /default
Navigate to Windows or Linux
Replace line 68 (windows.py), or line 76 (linux.py) with your discord webhook!



**How to hide console (windows.py only):**

Uncomment line 84



**What does it do? :**

Allows you access to the 'victim's' computer!



**Not getting connect information? :**

Ensure your discord webhook is setup properly and your link is in the file!



**How to connect:**

Input the port/tunnel addr into the client!

NgrokTunnel: "tcp://4.tcp.ngrok.io:14352" -> "localhost:5050" your port here would be: "14352", tunnel would be: "4.tcp.ngrok.io"



**Running SoulMain.py**

Open SoulMain.py
Select the option based on your targets OS
Navigate to /dist
Send the given file(s) to your target!
