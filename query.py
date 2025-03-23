import random
import requests
import json
import time
import os
import datetime
from colorama import Fore, init

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()
print("name tool by zante")

delay = 0


def generate_telepatia_username():
    return input("search name: ")

def check_username_availability(claim):
    url = "https://discord.com/api/v9/auth/register"

    payload = {
        "email": "znt@znt.com",
        "username": claim,
        "global_name": "znt",
        "password": "znt31313131313",
        "invite": None,
        "consent": True,
        "date_of_birth": "2005-05-06",
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response_data = response.json()

    if response_data.get('message') == "Invalid Form Body" and response_data.get('code') == 50035:
        username_errors = response_data['errors']['username']['_errors']
        for error in username_errors:
            if error['code'] == "USERNAME_ALREADY_TAKEN":
                print(Fore.RED + f"Username : {claim} used")
                return

    print(Fore.GREEN + f"Username : {claim} not used ")

if __name__ == "__main__":
    while True:
        time.sleep(delay)
        init(autoreset=True)
        username = generate_telepatia_username()
        check_username_availability(username)