from NaverPy import API
import apikey

api = API(apikey.client_ID, apikey.client_secret)
print(api.search_blog('Test'))