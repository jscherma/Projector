from TwitterAPI import TwitterAPI

consumer_key = 'znFlqUAAnZOsls1QmaQamm0Q0'
consumer_secret = '7FV3OhO6JZhM6sbaKPq5ckNSf8Zq3vqRiMXy4kEDylB7Be45th'
token = "704777239204749312-Ikxdp9qPAErYz7tmAYlQ5x4mYZxtYzf"
token_secret = "6IEyoRzH5taO4Q2pZMy7RZUqZNhvti97WogJlHxbv3JIt"

api = TwitterAPI(consumer_key, consumer_secret, token, token_secret)

SEARCH_TERM = "Advertising"

r = api.request('search/tweets', {'q': SEARCH_TERM})

for item in r:
    print(item)

print('\nQUOTA: %s' % r.get_quota())
