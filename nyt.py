from nytimesarticle import articleAPI
api = articleAPI("391f118fad27467d8b193a6686e1b3d1")

articles = api.search(q = 'Obama',
    fq = {'headline':'Obama', 'source': ['Reuters','The New York Times']},
    begin_date = 20111231, page = 3)
