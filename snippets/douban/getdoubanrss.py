# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:34:27 2021
@author: yonniye
"""

import xmltodict
import requests
import json
from datetime import datetime, timedelta

def xml2dict(xmldata):
    data = xmltodict.parse(xmldata, process_namespaces = True)
    return dict(data)

def formatGMTime(gtime):
    G_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    format_dt = datetime.strptime(gtime, G_FORMAT) + timedelta(hours=8)
    str_dt = format_dt.strftime('%Y-%m-%d') # 仅保留年-月-日
    return str_dt

def setImgSrc(txt):
    strtxt = str(txt)
    start = strtxt.find('<img src=') + 10
    end = strtxt.find('alt=') - 2
    return strtxt[start:end]

def getJsonStr(lst):
    """
    返回json格式的`字符串`
    """
    return json.dumps(lst, ensure_ascii=False, separators=(',', ': '))

def getMovieList(url):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}
    movielist = []
    
    r = requests.get(url, headers = headers)
    xml = xml2dict(r.text)
    items = xml['rss']['channel']['item']
    for i in range(10):
        t = {}
        t["title"] = items[i]['title'][2:]
        t["link"] = items[i]['link']
        t["pubdate"] = formatGMTime(items[i]['pubDate'])
        t["imgsrc"] = setImgSrc(items[i]['description'])
        movielist.append(t)
    return movielist
    
def main():
    # 仅需要把url中people后面的数字就是自己的id
    url = 'https://www.douban.com/feed/people/163310540/interests'
    t = getMovieList(url)
    x = getJsonStr(t)
    print(x)
    
if __name__ == '__main__':
    main()










    
