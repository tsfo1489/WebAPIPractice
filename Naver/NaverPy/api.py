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
        self, endpoint, query, ext, args
    ) :
        url = self.mainURL + endpoint

        if ext == 'json' :
            url += '.json'
        elif ext == 'xml' :
            url += '.xml'
        else :
            raise ArgumentError('\'ext\' must be json or xml')

        param = {'query' : query}
        param.update(args)
        res = self.request('GET', url, param)

        if res.status_code == 400 :
            raise ArgumentError('Wrong Argument {}'.format(param))

        if ext == 'json' :
            return json.loads(res.text)
        else :
            return self.xml_to_json(xmltodict.parse(res.text))


    def search_blog(
        self, query : str, display=10, start=1, sort='sim', ext='json'
    ) :
        args = {
            'display' : display,
            'start' : start,
            'sort' : sort
        }
        try :
            return self.__search_get('search/blog', query, ext, args)
        except Exception: 
            raise

    def search_news(
        self, query : str, display=10, start=1, sort='sim', ext='json'
    ) :
        args = {
            'display' : display,
            'start' : start,
            'sort' : sort
        }
        try :
            return self.__search_get('search/news', query, ext, args)
        except Exception: 
            raise
            
    def search_book(
        self, query : str, display=10, start=1, sort='sim', ext='json'
    ) :
        args = {
            'display' : display,
            'start' : start,
            'sort' : sort
        }
        try :
            return self.__search_get('search/book', query, ext, args)
        except Exception: 
            raise

    def search_encyc(
        self, query : str, display=10, start=1, ext='json'
    ) :
        args = {
            'display' : display,
            'start' : start
        }
        try :
            return self.__search_get('search/encyc', query, ext, args)
        except Exception: 
            raise