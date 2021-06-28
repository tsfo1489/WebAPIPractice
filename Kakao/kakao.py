import requests
import apikey
import json
headers = { 'Authorization' : 'KakaoAK ' + apikey.apikey }
query = {'query' : 'Test'}

res = requests.get('https://dapi.kakao.com/v2/search/web', params=query, headers=headers)
print(json.loads(res.text))