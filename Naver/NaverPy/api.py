import requests
from NaverPy.errors import ArgumentError, InternalServerError
from NaverPy.auth import Auth
import json
import xmltodict

class API :
    mainURL = 'https://openapi.naver.com/v1/'
    def __init__(self, auth : Auth) :
        self.auth = auth
    
    def request(
        self, method, endpoint, params=None, json_payload=None
    ) :
        hds = { 
            'X-Naver-Client-Id' : self.auth.ClientID,
            'X-Naver-Client-Secret' : self.auth.ClientSecret 
        }

        if method == 'GET' :
            return requests.get(endpoint, params=params, headers=hds)
        if method == 'POST' :
            return requests.post(endpoint, json=json_payload, headers=hds)
            
    def xml_to_json(self, xml : dict) -> dict :
        temp_json = {}
        raw_xml = xml['rss']['channel']
        temp_json['lastBuildDate'] = raw_xml['lastBuildDate']
        temp_json['total'] = int(raw_xml['total'])
        temp_json['start'] = int(raw_xml['start'])
        temp_json['display'] = int(raw_xml['display'])
        temp_json['items'] = raw_xml['item']
        return temp_json
    
    def Search(
        self, target, query, ext, args
    ) :
        url = self.mainURL + 'search/' + target

        if ext == 'json' :
            url += '.json'
        elif ext == 'xml' :
            url += '.xml'
        else :
            raise ArgumentError('\'ext\' must be json or xml')

        param = {'query' : query}
        param.update(args)
        res = self.request('GET', url, param)

        if ext == 'json' :
            ans = json.loads(res.text)
        else :
            ans = self.xml_to_json(xmltodict.parse(res.text))
        
        if res.status_code != 200 :
            if res.status_code == 400 :
                raise ArgumentError(ans['errorMessage'])
            if res.status_code == 401 : 
                raise ArgumentError(ans['errorMessage'])
            if res.status_code == 500 :
                raise InternalServerError()
            raise Exception(ans['errorMessage'])

        return ans

    def DatalabSearch(
        self, params
    ) :
        url = self.mainURL + 'datalab/search'
        res = self.request('POST', url, json_payload=params)

        ans = json.loads(res.text)
        
        if res.status_code != 200 :
            if res.status_code == 400 :
                raise ArgumentError(ans['errMsg'])
            if res.status_code == 401 : 
                raise ArgumentError(ans['errMsg'])
            if res.status_code == 500 :
                raise InternalServerError()
        
        return ans
    
    def ShortURL(self, url) :
        endpoint = self.mainURL + 'util/shorturl.json'
        res = self.request('GET', endpoint, {'url' : url})

        ans = json.loads(res.text)
        
        if res.status_code != 200 :
            if res.status_code == 400 :
                raise ArgumentError(ans['errorMessage'])
            if res.status_code == 401 : 
                raise ArgumentError(ans['errorMessage'])
            if res.status_code == 500 :
                raise InternalServerError()
            raise Exception(ans['errorMessage'])
        
        return ans