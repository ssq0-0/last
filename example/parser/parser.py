import requests
import time
import csv
import psycopg2
from db import  insert_data_into_table


def do_something():
    token = '22ee45a722ee45a722ee45a7e021f82e35222ee22ee45a7478ed2d49e454b6780cae1ba'
    ver = '5.199'
    count = '15'

    domain = 'gorodpermru'

    res_post = requests.get('https://api.vk.com/method/wall.get',
                 params={
                     'access_token': token,
                     'domain': domain,
                     'count': count,
                     'v': ver
                 })

    post_items = res_post.json()['response']['items']
    post_data = []

    print(str(len(post_items))+"-post_items")
    for item in post_items:
        post_data.append({'owner_id': item['owner_id'], 'post_id': item['id']})

    comments = []

    for x in post_data:
        res = requests.get('https://api.vk.com/method/wall.getComments',
                     params={
                         'access_token': token,
                         'owner_id': x['owner_id'],
                         'post_id': x['post_id'],
                         'v': ver
                     })

        com_items = res.json()['response']['items']
        print(str(len(com_items))+"-com_items")
        time.sleep(1)

        for item in com_items:
            data = item['text']
            comments.append(item["text"])
            insert_data_into_table((data))
            print(data)



while True:
    do_something()
    time.sleep(300)