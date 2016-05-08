# -*- coding: utf-8 -*-
import urllib2
import json


class weather_baidu(object):

    def __init__(self):
        pass

    def getweather(self, city=""):
        if city == "":
            return None
        else:
            url = 'http://apis.baidu.com/heweather/weather/free?city=' \
                + str(city)
            req = urllib2.Request(url)
            req.add_header("apikey", "8fd6ec8a914c0300695eb38809a19286")
            resp = urllib2.urlopen(req)
            content = resp.read()
            if(content):
                # content = json.dumps(content)
                content = json.loads(content)
                if content['HeWeather data service 3.0'][0].get('status') == 'ok':
                    city = content['HeWeather data service 3.0'][0].get('basic')['city']
                    status = content['HeWeather data service 3.0'][0].get('now')['cond'].get('txt')
                    feel_tmp = content['HeWeather data service 3.0'][0].get('now')['fl']
                    hum = content['HeWeather data service 3.0'][0].get('now')['hum']
                    pcpn = content['HeWeather data service 3.0'][0].get('now')['pcpn']
                    tmp = content['HeWeather data service 3.0'][0].get('now')['tmp']
                    vis = content['HeWeather data service 3.0'][0].get('now')['vis']
                    wind_deg = content['HeWeather data service 3.0'][0].get('now')['wind'].get('deg')
                    wind_dir = content['HeWeather data service 3.0'][0].get('now')['wind'].get('dir')
                    wind_spd = content['HeWeather data service 3.0'][0].get('now')['wind'].get('spd')
                    drsg_brf = content['HeWeather data service 3.0'][0].get('suggestion')['drsg'].get('brf')
                    drsg_txt = content['HeWeather data service 3.0'][0].get('suggestion')['drsg'].get('txt')

                    wea = u"当前查询城市:" + city + u"\n天气状态:" + status + u"\n体感温度:"\
                        + feel_tmp + u"\t相对湿度:" + hum + u"\t降水量:" + pcpn + \
                        u"\t温度:" + tmp + u"\t能见度:" + vis + u"\n风力(360度):" + \
                        wind_deg + u"\t风向" + wind_spd + u"\n穿衣指数  " + drsg_brf\
                        + "\t" + drsg_txt
                    return wea
                else:
                    return u"你查询的城市输入有误或者不存在呢~"
# http://www.heweather.com/documents/cn-city-list
# More data: http://apistore.baidu.com/apiworks/servicedetail/478.html
