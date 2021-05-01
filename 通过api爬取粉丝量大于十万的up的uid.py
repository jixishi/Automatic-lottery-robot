import requests
import bs4
import json
import urllib.request
import time


def get_fans_data(uid):  # 查询当前uid的粉丝量
    # 伪造浏览器请求头
    headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    page = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' + str(uid))

    info = json.loads(page.text)

    fans = info['data']['follower']

    return fans

def Get_fans(target,uid_0,uid_1):#返回一个字典
    dic={'uid','fans'}
    while uid_0<uid_1:
        dic.append(get_fans_data(uid_0))
    return dic

print (Get_fans(100000,1,10))

# def Get_fansOver(target, uid_0, uid_1):  # uid_range
#     while uid_0 < uid_1:

#         time.sleep(1)

#         if int(get_fans_data(uid_0)) > target:
#             return get_fans_data(uid_0)

#         uid_0 += 1
#         # 返回 wu



# 基本成功 但是频率过高会被b站封杀
