from NaverPy import API
import apikey
import json

api = API(apikey.client_ID, apikey.client_secret)

test_keyword = '대선'

f_jso = open('json.json', 'w', encoding='utf-8')
f_jso.write(json.dumps(api.search_book(test_keyword, display=100, ext='json'), ensure_ascii=False))