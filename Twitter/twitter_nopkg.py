import requests
import apikey
import base64
import json

raw_key = '{}:{}'.format(apikey.consumer_key, apikey.consumer_secret).encode('ascii')
b64_key = base64.b64encode(raw_key)
b64_key = b64_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

# HEADER 구성하기
auth_headers = {
    'Authorization': 'Basic {}'.format(b64_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_res = requests.post(auth_url, headers=auth_headers, data=auth_data)
access_token = auth_res.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_params = {
    'q':'우한폐렴 OR 코로나',
    'result_type': 'mixed',
    'count': 1,
    'retryonratelimit':True,
}

search_url = '{}1.1/search/tweets.json'.format(base_url)
search_res = requests.get(
    search_url, headers=search_headers, 
    params=search_params
)

res_json = json.loads(search_res.text)

print(res_json)