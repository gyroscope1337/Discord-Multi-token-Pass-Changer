import os
import json
import string
from pystyle import *
import tls_client
import requests
import ctypes
import random
import easygui
from itertools import cycle
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

class xyzraid:
    def __init__(self):
        self.tokens = self.load_tokens()
        self.nowtimer = datetime.today().strftime('%H:%M:%S')
        os.system("mode 130, 30")
        self.clear()
        self.setTitle("Polar Boosting | Password Changer")
        self.banner()

        with open("config.json", "r") as config_file:
            config = json.load(config_file)
            self.password_prefix = config.get("PASSWORD_PREFIX", "")

        useproxy = Write.Input(f'[{self.nowtimer}] Use Proxies? (y/n): ', Colors.cyan, interval=0.03).lower()

        if useproxy == "y":
            Write.Print("~ Using Proxy", Colors.cyan, interval=0.03)
            proxy = self.get_proxy_list()

            self.session = tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True)
            self.session.proxies = {
                "http": proxy,
                "https": proxy
            }
        else:
            Write.Print("~ Using Proxyless", Colors.cyan, interval=0.03)
            self.session = tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True)
        # ---
        self.xyz_main()

    def load_tokens(self):
        with open("tokens.txt", "r", encoding="utf-8") as file:
            return file.read().splitlines()

    def banner(self):
        banner = f'''

 █    ██  ██▓  ▄▄▄█████▓ ██▓ ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓▓█████ 
 ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀ 
▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒███   
▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ 
▒▒█████▓ ░██████▒▒██▒ ░ ░██░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒
░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░
░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░░  ░      ░  ▒   ▒▒ ░   ░     ░ ░  ░
 ░░░ ░ ░   ░ ░   ░       ▒ ░░      ░     ░   ▒    ░         ░   
   ░         ░  ░        ░         ░         ░  ░           ░  ░
Tokens to password change: {len(self.tokens)} | ultimate
'''
        print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter(banner)))

    def clear(self):
        os.system("cls")

    def setTitle(self, _str):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")

    def get_proxy_list(self):
        useproxy = Write.Input(f'\n{self.nowtimer} (y) Own Proxies or (n) Generate some ', Colors.blue_to_purple, interval=0.03).lower()

        if useproxy == "y":
            proxylist = easygui.fileopenbox(msg="Choose your Proxy List", title="Proxy List Opener", filetypes=".txt")
            proxies = open(proxylist, "r", encoding="utf-8").read().splitlines()
            return "http://" + random.choice(proxies) or "https://" + random.choice(proxies)
        else:
            try:
                api = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=ipport&format=text"
                proxies = requests.get(api).text.splitlines()
                return "http://" + cycle(proxies) or "https://" + cycle(proxies)
            except:
                pass

    @staticmethod
    def get_cookie():
        response = requests.Session().get('https://discord.com/app')
        cookie = str(response.cookies)
        return cookie.split('dcfduid=')[1].split(' ')[0], cookie.split('sdcfduid=')[1].split(' ')[0], cookie.split('cfruid=')[1].split(' ')[0]

    @staticmethod
    def get_headers(token):
        headers = {
            "authority": "discord.com",
            "accept": "*/*",
            "accept-language": "en-US",
            "authorization": token,
            "cookie": "__dcfduid=%s; __sdcfduid=%s; locale=en-US; __cfruid=%s" % xyzraid.get_cookie(),
            "connection": "keep-alive",
            "content-type": "application/json",
            "origin": "https://discord.com",
            "referer": "https://discord.com/",
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-discord-timezone": "America/New_York",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDExIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTc5ODgyLCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMDMwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
        }
        return headers

    @staticmethod
    def check_status(status_code: int):
        status_messages = {
            200: "Success",
            201: "Success",
            204: "Success",
            400: "Detected Captcha",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method not allowed",
            429: "Too many Requests"
        }
        return status_messages.get(status_code, "Unknown Status")

    def generate_random_password(self):
        letters_and_digits = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(letters_and_digits) for i in range(8))
        return self.password_prefix + random_string

    def xyz_main(self):
        self.clear()
        self.banner()

        threads = float(Write.Input(f'{self.nowtimer} Threads: ', Colors.cyan_to_green, interval=0.03))

        def pwchanger(token, password, email):
            new_pass = self.generate_random_password()
            url = 'https://discord.com/api/v9/users/@me'
            payload = {'password': password, 'new_password': new_pass}
            headerz = xyzraid.get_headers(token)

            r = self.session.patch(url, json=payload, headers=headerz)
            if r.status_code == 200:
                new_token = r.json()['token']
                tk = new_token[:32] + "*" * 3
                print(Colorate.Vertical(Colors.cyan_to_green, f'{self.nowtimer} ({xyzraid.check_status(r.status_code)}) → {tk} [{new_pass}]'))
                open("new_tokens.txt", "a").write(f"{email}:{new_pass}:{new_token}" + "\n")
            else:
                print(Colorate.Horizontal(Colors.red_to_yellow, f'{self.nowtimer} ({xyzraid.check_status(r.status_code)}) → {tk}'))

        tokens = list(set(self.tokens))

        with ThreadPoolExecutor(max_workers=threads) as executor:
            for account in tokens:
                email, password, token = account.split(':')[:3]
                executor.submit(pwchanger, token, password, email)

xyzraid()
input("")