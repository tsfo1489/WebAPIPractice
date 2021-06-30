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

        if res.status_code == 400 :
            raise ArgumentError('Wrong Argument {}'.format(param))

        if ext == 'json' :
            return json.loads(res.text)
        else :
            return self.xml_to_json(xmltodict.parse(res.text))

    def DatalabSearch(
        self, params
    ) :
        url = self.mainURL + 'datalab/search'
        res = self.request('POST', url, json_payload=params)
        return json.loads(res.text)