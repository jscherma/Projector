from TwitterAPI import TwitterAPI


consumer_key = 'znFlqUAAnZOsls1QmaQamm0Q0'
consumer_secret = '7FV3OhO6JZhM6sbaKPq5ckNSf8Zq3vqRiMXy4kEDylB7Be45th'
token = "704777239204749312-Ikxdp9qPAErYz7tmAYlQ5x4mYZxtYzf"
token_secret = "6IEyoRzH5taO4Q2pZMy7RZUqZNhvti97WogJlHxbv3JIt"
track_term = "Radical Media"

api = TwitterAPI(consumer_key, consumer_secret, token, token_secret)

r= api.request('statuses/filter', {'locations':'-74,40,-73,41', 'track': track_term, 'count':100})
for item in r:
    print(item['text'] if 'text' in item else item)

#option to either stream tweets, or post the RadicalMedia timeline
