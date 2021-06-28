import requests
import apikey
import json

headers = { 'X-Naver-Client-Id' : apikey.client_ID,
            'X-Naver-Client-Secret' : apikey.client_secret }
query = {'query' : '열혈C'}

res = requests.get('https://openapi.naver.com/v1/search/book.json', params=query, headers=headers)
ans = json.loads(res.text)
print(ans)