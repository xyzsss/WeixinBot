# -*- coding: utf-8 -*-
"""Exyum Robot
This is used for deal with text request from weixin robot

=== TEST ===
er = ERobot()
print er.dealContent()

# FOR IMPORTED
er = ERobot.ERobot()
print er.dealContent()

Copyright (c) 2016-2020, Mike Xia.
"""
import weather_baidu

__author__ = "Mike Xia (exuxu@exyum.com)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2016-2020 Mike Xia"
__license__ = "New-style BSD"


class ERobot (object):

    def __init__(self):
        pass

    def getName(self):
        return self.name

    def __str__(self):
        return "%s is a %s" % (self.name, self.name)

    def dealContent(self, content=""):
        if content == "":
            return "empty request ???"
        else:
            content = content.strip()
            if content == "H" or content == "h":
                re_string = ""
                re_string += "Hia,Hia,Hia....功能列表\n\n"
                re_string += "\t天气查询，wr city ,eg:(wr 南京;wr nanjin)"
                re_string += "\n\n更多功能可以和我提啊"
                return re_string
            elif content.find('wr ') != -1:
                city = content.lstrip('wr ').strip()
                we = weather_baidu.weather_baidu()
                res = we.getweather(city)
                return res
            elif content.isdigit():
                res = int(content) + 1
                return str(res)
            else:
                return "Robot is repairing now .... " + content
