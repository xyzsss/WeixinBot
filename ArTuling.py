# -*- coding: utf-8 -*-
import requests
import json
from time import sleep


class ArTuling(object):

    def __init__(self):
        pass

    def replays(self, info=""):
        tuling_key = "09029ac10ee52f1a0da20e08629972bb"
        api_url = 'http://www.tuling123.com/openapi/api'
        if info == "":
            return "你说了什么?风太大了，我听不清啊!"
        else:
            data = dict(key=tuling_key, info=info)
            while True:
                try:
                    response = requests.post(
                        api_url, data=data, allow_redirects=True)
                    break
                except Exception:
                    print "The api url request failed."
                    sleep(3)
            contents = json.loads(response.content)
            if contents['code'] == 100000:  # text only
                return contents['text']
            elif contents['code'] == 200000:
                return_string = u"点此查看图片" + contents['url']
                return return_string
            elif contents['code'] == 302000:  # news list
                news_content = ""
                for x in contents['list']:
                    news_content = news_content + u"【" + x['source'] + u"】 " +\
                        x['article'] + "\t" + x['detailurl'] + "\n"
                return news_content
            else:
                return "大概，可能，也许是我累了，让我休息好不好..."
# TODO： add user sesssion
