import requests
import apikey
import json

headers = { 'Authorization' : 'KakaoAK ' + apikey.apikey }
query = {'query' : '열혈C'}

res = requests.get('https://dapi.kakao.com/v3/search/book', params=query, headers=headers)
ans = json.loads(res.text)
print(ans)