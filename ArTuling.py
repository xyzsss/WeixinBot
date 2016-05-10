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
            res_cont = json.loads(response.content)
            return res_cont['text']

# TODO： add user sesssion