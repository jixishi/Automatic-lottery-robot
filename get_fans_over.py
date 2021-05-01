import json
import time
import requests

def get_fans(uid):
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    name_url = 'https://api.bilibili.com/x/space/acc/info?mid={}'.format(uid)
    fans_url = 'https://api.bilibili.com/x/relation/stat?vmid={}'.format(uid)
    name_response = requests.get(name_url,headers=headers).text
    fans_response = requests.get(fans_url,headers=headers).text
    name_json = json.loads(name_response)
    fans_json = json.loads(fans_response)
    name = name_json['data']['name']
    fans = fans_json['data']['follower']
    info_list = {'name':name, 'fans':fans}
    time.sleep(0.9)
    return info_list

def get_fans_over(target):#从零开始
    dict = {}
    for uid in range (1,target+1):
        info_list = get_fans(uid)
        if(info_list['fans']>10000):
            dict['{}'.format(info_list['name'])] = info_list['fans']
    return dict

target = 10
print(get_fans_over(target))
