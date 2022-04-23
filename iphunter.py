import socket
import os
from templates import *

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

art = r'''
      _               _                       _                      
     (_)             | |                     | |                
      _   _ __       | |__    _   _   _ __   | |_    ___   _ __ 
     | | | '_ \      | '_ \  | | | | | '_ \  | __|  / _ \ | '__|
     | | | |_) |     | | | | | |_| | | | | | | |_  |  __/ | |   
     |_| | .__/      |_| |_|  \__,_| |_| |_|  \__|  \___| |_|   
         | |                                                    
         |_|                                                    '''



def iptracker():
    try:
        url = input(f'{G}Enter url> {W}')
        print(f"Ip4 address of this url is {socket.gethostbyname(url)}")
    except Exception:
        print(f"{R} There was an error, either with the url or with your internet connection{W}")

def LocationTracker():
    os.system("cls||clear")
    print(f"{G}{art}{W}\n\n")

    print(f"{Y}[!] Select a template:\n\n{W}")
    print(f"{G}[1]{W}", end=" ")
    print(f"{C}Whatsapp{W}")
    print(f"{G}[2]{W}", end=" ")
    print(f"{C}Telegram{W}")
    print(f"{G}[3]{W}", end=" ")
    print(f"{C}Zoom{W}")


    while True:
        entry = input(f"{G}[>] {W}")

        if entry == '1':
            WhatsAppPhish()

        if entry == '2':
            TelegramPhish()

        if entry == '3':
            ZoomPhish()

def main():

    try:
        os.system("cls||clear")

        # Checking if modules are present
        from flask import Flask, render_template, request
        from rich.console import Console
        from rich.table import Table

        print(f"{G}{art}{W}\n\n")

        print(f"{C} Version   —> 0.1{W}\n")

        print(f"{Y}[!] Select a command:\n\n")

        print(f"{G}[1]{W}", end=" ")
        print(f"{C}Track ip with url{W}")
        print(f"{G}[2]{W}", end=" ")
        print(f"{C}Location Tracker{W}")

        while True:
            entry = input(f"{G}[>] {W}")

            if entry == '1':
                iptracker()

            elif entry == '2':
                LocationTracker()

            elif entry == 'exit':
                print("Bye")
                break

            else:
                print(f"{R}Invalid Input please try again!{W}")

    except ModuleNotFoundError:
        print(f"{G}Installing Modules{W}")
        os.system("pip install flask")
        os.system("pip install rich")
        os.system("cls||clear")
        main()

main()

