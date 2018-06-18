from nytimesarticle import articleAPI
api = articleAPI("391f118fad27467d8b193a6686e1b3d1")

articles = api.search(q = 'Trump',
    fq = {'headline':'Trump', 'source': ['The New York Times']},
    begin_date = 20180618)



print articles


#prints the url to the trending article and the details of the whole article
