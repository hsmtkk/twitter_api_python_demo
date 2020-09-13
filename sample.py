import os
import twitter

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_key = os.getenv('ACCESS_KEY')
access_secret = os.getenv('ACCESS_SECRET')

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_key, access_token_secret=access_secret)

results = api.GetSearch(raw_query="q=どうぶつの森&result_type=recent&count=100")

#result = results[0]
#print(result)
#print(type(result))
#print(result.text)

#for result in results:
#    print(result)

for result in results[:10]:
    print(result.text)
