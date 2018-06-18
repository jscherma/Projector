#newsapi


import requests

print "=============Top Headlines in the U.S.==============="

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=a0aadd1074af4669a1dce1d5099d283d'
       'totalResults()')
response = requests.get(url)
print response.json()
