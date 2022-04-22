import random

import requests
import time
from datetime import datetime
from pyrogram import Client

app = Client("my_account")
TARGET_USER = 'lkatekk'


def get_datetime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


async def send_photo(cat_img):
    async with app:
        await app.send_photo(TARGET_USER, cat_img)
        print(f'sent {cat_img} in {get_datetime()}')


while True:
    r = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=png,jpg')
    img = r.json()[0]['url']
    app.run(send_photo(img))
    time.sleep(random.randrange(1800, 10800))
