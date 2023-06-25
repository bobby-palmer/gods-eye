# the main logic file for the gods eye project
import instagrapi
import requests
from dotenv import load_dotenv
from instagrapi import Client
import os

load_dotenv()

INSTAUSER = os.getenv('INSTAUSER')
INSTAPASS = os.getenv("INSTAPASS")

cl = Client()
if INSTAPASS is not None and INSTAUSER is not None:
    cl.login(INSTAUSER, INSTAPASS)

    info = cl.user_info_by_username("simeonbirnbaum")

    print(info)
else: 
    print("failed to get login")
