from NaverPy import API
import apikey
import json

api = API(apikey.client_ID, apikey.client_secret)

f_xml = open('xml.json', 'w', encoding='utf-8')
f_xml.write(json.dumps(api.search_blog('Test', ext='xml'), ensure_ascii=False))

f_jso = open('json.json', 'w', encoding='utf-8')
f_jso.write(json.dumps(api.search_blog('Test', ext='json'), ensure_ascii=False))