import requests
from NaverPy.errors import ArgumentError
import json
import xmltodict

class API :
    mainURL = 'https://openapi.naver.com/v1/'
    def __init__(self, ClientID : str, ClientSecret : str) :
        self.ClientID = ClientID
        self.ClientSecret = ClientSecret
    
    def request(
        self, method, endpoint, params=None, json_payload=None
    ) :
        hds = { 
            'X-Naver-Client-Id' : self.ClientID,
            'X-Naver-Client-Secret' : self.ClientSecret 
        }

        if method == 'GET' :
            return requests.get(endpoint, params=params, headers=hds)
            
        
    def search_blog(
        self, query : str, display=10, start=1, sort='sim', ext='json'
        ) :
        url = self.mainURL + 'search/blog.'
    
        if ext == 'json' :
            url += 'json'
        elif ext == 'xml' :
            url += 'xml'
        else :
            raise ArgumentError('\'ext\' must be json or xml')

        if display > 100 or display < 1:
            raise ArgumentError('\'display\' arg must be between 1 and 100')
        if start < 1 or start > 1000 :
            raise ArgumentError('\'start\' arg must be between 1 and 1000')
        if not(sort == 'sim' or sort == 'date') :
            raise ArgumentError('\'sort\' arg must be sim or date')

        param = {
            'query' : query,
            'display' : display,
            'start' : start,
            'sort' : sort
        }
        res = self.request('GET', url, param)

        if ext == 'json' :
            return json.loads(res.text)
        else :
            return json.loads(json.dumps(xmltodict.parse(res.text), ensure_ascii=False))


        
