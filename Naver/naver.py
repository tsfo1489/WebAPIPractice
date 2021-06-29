from typing import List
import requests
import apikey
import json
from datetime import datetime, timedelta

def book_search(book_name : str) :
    headers = { 'X-Naver-Client-Id' : apikey.client_ID,
                'X-Naver-Client-Secret' : apikey.client_secret }
    query = {'query' : '열혈C'}

    res = requests.get('https://openapi.naver.com/v1/search/book.json', params=query, headers=headers)
    return json.loads(res.text)

def to_timedelta(s : str) :
    tmp = 0
    day = 0
    month = 0
    year = 0
    for c in s :
        if c.isdigit() :
            tmp = tmp * 10 + int(c)
        if c == 'd' :
            day += int(tmp)
            tmp = 0
        if c == 'm' :
            month += int(tmp)
            tmp = 0
        if c == 'y' :
            year += int(tmp)
            tmp = 0
    return timedelta(day+(year*12+month)*30)

def Datalab_trend(title : str, keywords : list, period : str, timeUnit='date') :
    headers = { 'X-Naver-Client-Id' : apikey.client_ID,
                'X-Naver-Client-Secret' : apikey.client_secret }

    endDate = datetime.now().strftime('%Y-%m-%d')
    startDate = datetime.now() - to_timedelta(period)
    startDate = startDate.strftime('%Y-%m-%d')

    query = {
        'startDate' : startDate, 
        'endDate' : endDate, 
        'timeUnit' : timeUnit,
        'keywordGroups' : [
            {
                'groupName' : title,
                'keywords' : keywords
            },
        ]
        }

    res = requests.post('https://openapi.naver.com/v1/datalab/search', headers=headers, json=query)
    return json.loads(res.text)

def Search(keyword : str, target : str) :
    headers = { 'X-Naver-Client-Id' : apikey.client_ID,
                'X-Naver-Client-Secret' : apikey.client_secret }
    query = { 'query' : keyword }

    target_url = { 
        'blog' : 'blog', 
        'news' : 'news.json', 
        'book' : 'book.json', 
        'encyc' : 'encyc.json', 
        'movie' : 'movie.json', 
        'cafearticle' : 'cafearticle.json', 
        'kin' : 'kin.json', 
        'local' : 'local.json', 
        'webkr' : 'webkr.json', 
        'image' : 'image', 
        'shop' : 'show.json', 
        'doc' : 'doc.json'
    }

    if not target in target_url :
        raise Exception('Target Error {} is not available option'.format(target))

    res = requests.get('https://openapi.naver.com/v1/search/' + target_url[target], params=query, headers=headers)
    return json.loads(res.text)