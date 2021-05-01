import requests
from bs4 import BeautifulSoup
import urllib.request
import json
import re
import time


def Get_Name(uid):
    headers = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
    )
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    page = requests.get('https://api.bilibili.com/x/space/acc/info?mid=' + str(uid))

    info = json.loads(page.text)
    name = info['data']['name']
    return name


uid = 629660403
print(Get_Name(uid))