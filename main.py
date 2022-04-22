import random
import requests
import time
from datetime import datetime
from pyrogram import Client

app = Client("my_account")
TARGET_USER = 'lkatekk'
CAT_API_URL = 'https://api.thecatapi.com/v1/images/search?mime_types=png,jpg'
MIN_TIME = 1800  # in sec
MAX_TIME = 10800  # in sec


def get_datetime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


async def send_photo(cat_img):
    async with app:
        await app.send_photo(TARGET_USER, cat_img)
        print(f'sent {cat_img} in {get_datetime()}')


while True:
    r = requests.get(CAT_API_URL)
    img = r.json()[0]['url']
    app.run(send_photo(img))
    time.sleep(random.randrange(MIN_TIME, MAX_TIME))
