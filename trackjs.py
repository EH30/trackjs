#!/usr/bin/env python
import os
import sys

def check_system():
    if sys.platform == "linux" or sys.platform == "linux2":
        # os.system("clear")
        return 0
    elif sys.platform == "win32":
        # os.system("cls")
        return 1

def run_server(os_plat):
    os.chdir("djserver/djsite")
    print("[*] Wait for the server to start on this window")
    print("[*] Send the https link that should open in a new termnal/cmd")
    print("[*] Make sure you're sending the https link not http\n")
    os.system("{0} manage.py runserver 127.0.0.1:9999".format(sys.executable.split("\\")[-1]))
    

if __name__ == "__main__":
    os_plat = check_system()

    if os_plat == 0:
        output = os.system("xterm -e ngrok_linux http 9999")

        if output >= 1:
            print("[-}Error You may need to install xterm")
        else:
            run_server(os_plat)

    elif os_plat == 1:
        output = os.system("start call ngrok_win32.exe http 9999")

        if output >= 1:
            print("[-]Error")
        else:
            run_server(os_plat)
