import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
import requests
url = input("Please Url Webhook (Link) : ")
body_nuke = {
  "content": "Welcome to Multi Tools. Multi Tools are bot and Smart\nYou need one Url Webhook (link) for use",
  "tts": False,
  "embeds": [
    {
      "id": 301618555,
      "title": "Our Discord Server",
      "description": "Discord Multi Tools\n",
      "url": "https://discord.gg/2G2tdf65kx",
      "color": 16711680,
      "image": {
        "url": "https://i.postimg.cc/Kz438R05/Our-Bot.png"
      },
      "fields": [],
      "footer": {
        "icon_url": "https://i.postimg.cc/L4vJ6mGZ/Feliz-anivers-rio.png",
        "text": "Ran By Cxrve"
      }
    }
  ],
  "components": [],
  "actions": {},
  "username": "Multi Tools",
  "avatar_url": "https://i.postimg.cc/L4vJ6mGZ/Feliz-anivers-rio.png"
}
b0 = "                                     By Multi Tools Server                                V1.3          "
b1 = "          ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗          "
b2 = "          ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝          "
b3 = "          ██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     ███████╗          "
b4 = "          ██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     ╚════██║          "
b5 = "          ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║          "
b6 = "          ║═╝     ╚═╝ ╚═════╝ ╚═══║══╝╚═╝   ╚═╝       ╚═╝    ║═════╝  ╚═════╝ ╚══════╝╚══════╝          "
b7 = "          ║                       ║                          ║                                          "
b8 = "          ║═════(1) Send Text     ║═════(4) Change Name      ║═════(7) Change Avatar                    "
b9 = "          ║                       ║                          ║                                          "
b10="          ║═════(2) Spam Chat     ║═════(5) Nuke Channel     ║═════(8) Ping People                       "
b11="          ║                       ║                          ║                                           "
b12="          ║═════(3) Url Webhook   ╚═════(6) Info             ╚═════(9) Exit                              "
b13="          ║                                                                                              "
b14="          ╚═════════════════>                                                                            "

def banner():
    print(f"{Fore.RED}"+b0)
    print(f"{Fore.RED}"+b1)
    print(f"{Fore.RED}"+b2)
    print(f"{Fore.RED}"+b3)
    print(f"{Fore.RED}"+b4)
    print(f"{Fore.RED}"+b5)
    print(f"{Fore.RED}"+b6)
    print(f"{Fore.LIGHTYELLOW_EX}"+b7)
    print(f"{Fore.LIGHTYELLOW_EX}"+b8)
    print(f"{Fore.LIGHTYELLOW_EX}"+b9)
    print(f"{Fore.LIGHTYELLOW_EX}"+b10)
    print(f"{Fore.YELLOW}"+b11)
    print(f"{Fore.YELLOW}"+b12)
    print(f"{Fore.YELLOW}"+b13)
def restart():
    for x in range (3):
        print()
banner()
name = "Multi Tools"
avatar_url = "https://i.postimg.cc/L4vJ6mGZ/Feliz-anivers-rio.png"
while True:
    main_input = input(f"{Fore.YELLOW}          ║═════════════════>")
    if main_input == "1":
        text = input(f"{Fore.YELLOW}          ╚Text═════════════>")
        requests.post(url, json=
        {
            "avatar_url" : avatar_url,
            "username" : name,
            "content" : text
        })
        print(Fore.LIGHTGREEN_EX + "-Send-")
        restart()
        banner()
    if main_input == "2":
        count = input(f"{Fore.YELLOW}          ║Count════════════>")
        text = input(f"{Fore.YELLOW}          ╚Text═════════════>")
        for i in range(int(count)):
            requests.post(url, json=
            {
                "avatar_url": avatar_url,
                "username": name,
                "content": text
            })
            print(f"{Fore.LIGHTGREEN_EX}-Send- {i+1}")
        print(f"{Fore.LIGHTGREEN_EX}-Done-")
        restart()
        banner()
    if main_input == "3":
        url = input("          ╚Url══════════════>")
        print(f"{Fore.LIGHTGREEN_EX}-Url Bot : {url} -")
        restart()
        banner()
    if main_input == "4":
        name = input("          ╚Name═════════════>")
        print(f"{Fore.LIGHTGREEN_EX}-Name Bot : {name} -")
        restart()
        banner()
    if main_input == "5":
        yn = input(f"{Fore.YELLOW}          ║You Want do it? [Y/N] : ")
        if yn == "N":
            quit()
        spam = input(f"{Fore.YELLOW}          ║Count════════════>")
        countdown = input(f"{Fore.YELLOW}          ╚Countdown════════>")
        for i in range(int(spam)):
            requests.post(url, json=body_nuke)
            print(f"{Fore.LIGHTGREEN_EX}-Send- {i+1}")
        print(f"{Fore.LIGHTGREEN_EX}-Done-")
        restart()
        banner()
    if main_input == "6":
        print(f"{Fore.YELLOW}1 is Send Message. 2 is SPAM Message. 3 is Change Url Webhook (Link). 4 is Change Name Bot. 5 is SPAM Message Our Discord and Flood. 6 is Info Multi Tools")
        restart()
        banner()
    if main_input == "7":
        avatar_url = input("          ╚Avatar═Url═Link═══>")
        print(f"{Fore.LIGHTGREEN_EX}-Avatar Bot (Link) : {avatar_url} -")
        restart()
        banner()
    if main_input == "8":
        count = input(f"{Fore.YELLOW}          ║Count════════════>")
        your_name = input(f"{Fore.YELLOW}          ║Your Name════════>")
        people = input(f"{Fore.YELLOW}          ║People ID════════>")
        for i in range(int(count)):
            requests.post(url, json=
            {
                "avatar_url": avatar_url,
                "username": name,
                "content": f"Hey <@{people}> Wake up. {your_name} wanna talk you"
            })
            print(f"{Fore.LIGHTGREEN_EX}-Send- {i+1}")
        print(f"{Fore.LIGHTGREEN_EX}-Done-")
        restart()
        banner()
    if main_input == "9":
        quit()
banner()