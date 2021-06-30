import requests

datalab_search_tc = {
    "startDate": "2017-01-01",
    "endDate": "2017-01-31",
    "timeUnit": "month",
    "keywordGroups": [ {
            "groupName": "한글",
            "keywords": [
                "한글",
                "korean"
            ]
        }
    ]
}
datalab_shopping_tc = {
    "startDate": "2017-08-01",
    "endDate": "2017-08-30",
    "timeUnit": "month",
    "category": [
        {"name": "패션의류", "param": [ "50000000"]}
    ]
}

class Auth :
    def __init__(self, ClientID, ClientSecret) :
        self.ClientID = ClientID
        self.ClientSecret = ClientSecret
    
    def check_auth(self) :
        check_dict = { 'datalab' : {}, }
        mainURL = 'https://openapi.naver.com/v1/'
        hds = { 
            'X-Naver-Client-Id' : self.ClientID,
            'X-Naver-Client-Secret' : self.ClientSecret 
        }
        
        '''데이터랩(검색어 트렌드) 테스트'''
        res = requests.post(mainURL + 'datalab/search', json=datalab_search_tc, headers=hds)
        if res.status_code == 200 :
            check_dict['datalab']['Search'] = True
        else :
            check_dict['datalab']['Search'] = False

        '''데이터랩(쇼핑인사이트) 테스트'''
        res = requests.post(mainURL + 'datalab/shopping/categories', headers=hds, json=datalab_shopping_tc)
        if res.status_code == 200 :
            check_dict['datalab']['Shopping'] = True
        else :
            check_dict['datalab']['Shopping'] = False

        '''검색 API 테스트'''
        res = requests.get(mainURL + 'search/blog.json', {'query' : 'Test', 'display' : 1}, headers=hds)
        if res.status_code == 200 :
            check_dict['search'] = True
        else :
            check_dict['search'] = False
        
        '''단축 URL 테스트'''
        res = requests.get(mainURL + 'util/shorturl', {'url' : 'https://naver.com'}, headers=hds)
        if res.status_code == 200 :
            check_dict['short_url'] = True
        else :
            check_dict['short_url'] = False
        return check_dict