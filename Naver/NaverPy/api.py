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
            
    def xml_to_json(self, xml : dict) -> dict :
        temp_json = {}
        raw_xml = xml['rss']['channel']
        temp_json['lastBuildDate'] = raw_xml['lastBuildDate']
        temp_json['total'] = int(raw_xml['total'])
        temp_json['start'] = int(raw_xml['start'])
        temp_json['display'] = int(raw_xml['display'])
        temp_json['items'] = raw_xml['item']
        return temp_json
    
    def __search_get(
        self, endpoint, query, display, start, sort, ext
    ) :
        url = self.mainURL + endpoint
    
        if ext == 'json' :
            url += '.json'
        elif ext == 'xml' :
            url += '.xml'
        else :
            raise ArgumentError('\'ext\' must be json or xml')

        if display > 100 or display < 1:
            raise ArgumentError('\'display\' arg must be between 1 and 100')
        if start < 1 or start > 1000 :
            raise ArgumentError('\'start\' arg must be between 1 and 1000')
        if not(sort == 'sim' or sort == 'date') and not (sort is None):
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
            return self.xml_to_json(xmltodict.parse(res.text))


    def search_blog(
        self, query : str, display=10, start=1, sort='sim', ext='json'
    ) :
        try :
            return self.__search_get('search/blog', query, display, start, sort, ext)
        except Exception: 
            raise

    def search_news(
        self, query : str, display=10, start=1, sort='sim', ext='json'
    ) :
        try :
            return self.__search_get('search/news', query, display, start, sort, ext)
        except Exception: 
            raise
            
    def search_book(
        self, query : str, display=10, start=1, sort='sim', ext='json'
    ) :
        try :
            return self.__search_get('search/book', query, display, start, sort, ext)
        except Exception: 
            raise

    def search_encyc(
        self, query : str, display=10, start=1, ext='json'
    ) :
        try :
            return self.__search_get('search/encyc', query, display, start, None, ext)
        except Exception: 
            raise