from requests import post
import colorama
from colorama import Fore
import os
from pystyle import *
import sys

colorama.init(autoreset=False)

banner = Fore.MAGENTA + """
 ▄█     █▄     ▄████████    ▄████████  ▄█      ███        ▄█    █▄    
███     ███   ███    ███   ███    ███ ███  ▀█████████▄   ███    ███   
███     ███   ███    ███   ███    ███ ███▌    ▀███▀▀██   ███    ███   
███     ███  ▄███▄▄▄▄██▀   ███    ███ ███▌     ███   ▀  ▄███▄▄▄▄███▄▄ 
███     ███ ▀▀███▀▀▀▀▀   ▀███████████ ███▌     ███     ▀▀███▀▀▀▀███▀  
███     ███ ▀███████████   ███    ███ ███      ███       ███    ███   
███ ▄█▄ ███   ███    ███   ███    ███ ███      ███       ███    ███   
 ▀███▀███▀    ███    ███   ███    █▀  █▀      ▄████▀     ███    █▀    
              ███    ███                                              """ + "\n\n" + Fore.CYAN + "  -------> Original By RigMatter12 | ReDesigned By Oxyru <-------\n" + Fore.RESET

if __name__ == "__main__":
    os.system("title Wraith Code Tester v1" if os.name == "nt" else "")
    os.system("cls" if os.name == "nt" else "clear")
    Cursor.HideCursor()
    print(Center.XCenter(banner))
    while True:
        Cursor.HideCursor()
        key = input(Fore.CYAN + ' [?] Type in a wraith code : ').replace(' ', '')
        Cursor.HideCursor()
        if not key == "exit":
            print(Fore.YELLOW + ' [i] Testing This Code...', end='\r')
            Cursor.HideCursor()
            if post('https://www.boomlings.com/database/getGJSecretReward.php', data={'rewardKey': key, 'udid': '1', 'chk': 'g6f2zAAwHCgMG', 'secret': 'Wmfd2893gb7'}, headers={'User-Agent': ''}).content.decode() != '-1':
                print(Fore.GREEN + ' [+] Code Works!         ')
                Cursor.HideCursor()
            else:
                print(Fore.RED + ' [x] This Code Doesn\'t Works!')
                Cursor.HideCursor()
        else:
            sys.exit()
