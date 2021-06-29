import requests
from NaverPy.errors import ArgumentError
import json

class API :
    mainURL = 'https://openapi.naver.com/v1/'
    def __init__(self, ClientID : str, ClientSecret : str) :
        self.ClientID = ClientID
        self.ClientSecret = ClientSecret
        
    def search_blog(
        self, query : str, display=10, start=1, sort='sim', ext='json'
        ) :
        url = self.mainURL + 'search/blog.'
    
        if ext == 'json' :
            url += 'json'
        else :
            url += 'xml'

        if display > 100 or display < 1:
            raise ArgumentError('\'display\' arg must be between 1 and 100')
        if start < 1 or start > 1000 :
            raise ArgumentError('\'start\' arg must be between 1 and 1000')
        if not(sort == 'sim' or sort == 'date') :
            raise ArgumentError('\'sort\' arg must be sim or date')

        hds = { 
            'X-Naver-Client-Id' : self.ClientID,
            'X-Naver-Client-Secret' : self.ClientSecret 
        }
        param = {
            'query' : query,
            'display' : display,
            'start' : start,
            'sort' : sort
        }

        res = requests.get(url, headers=hds, params=param)
        return json.loads(res.text)

        
