#!/usr/bin/env python
import requests
import time

method = 'wall.post'
token = '' #your vk.com token
version = 5.103

url = 'https://your-domain.ru/file.json'
x = requests.get(url)
data = x.json()

for i in data:
    data={
        'access_token': token,
        'owner_id': -111534444,
        'from_group': 1,
        'message': i['message'],
        'attachments': i['photo'],
        'publish_date': i['data'],
        'signed': 0,

        'v':version}
    time.sleep(2)
    r = requests.post('https://api.vk.com/method/wall.post', data).json()

    print(r)
