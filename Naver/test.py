from datetime import datetime
from NaverPy import API, DLTrendparam
from datetime import datetime
import apikey
import json

api = API(apikey.client_ID, apikey.client_secret)

test_keyword = '전쟁'
test_arg = {
    'display' : 100
}

dljson = DLTrendparam()

dljson.AddKeywordGroup('한글', ['한글', 'Korean'])
dljson.AddKeywordGroup('웹툰', ['작가', '장르'])
dljson.SetPeriodPrev(datetime.now(), '7d')
dljson.SetAgeRange(30, 49)
dljson.SetGender('m')
dljson.SetDevice('mo')

print(dljson)


f_jso = open('json.json', 'w', encoding='utf-8')
f_jso.write(json.dumps(api.DatalabSearch(dljson), ensure_ascii=False))