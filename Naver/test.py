from NaverPy import API
import apikey
import json

api = API(apikey.client_ID, apikey.client_secret)

test_keyword = '전쟁'
test_arg = {
    'display' : 100
}


f_jso = open('json.json', 'w', encoding='utf-8')
f_jso.write(json.dumps(api.search('blog', test_keyword, 'json', test_arg), ensure_ascii=False))