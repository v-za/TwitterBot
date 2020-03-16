import tweepy

#creating the API object so we can interact with twitter
#this will allow us to read and write data from twitter

API_KEY = 'qHDtt2bohqIjPH5DBMQNDsTeD'
API_SECRET = 'cpXicpIV87THnt7lxdTUKNxpQxaNXhg3c9RpMyP1tKiZoHIeJE'
ACCESS_KEY = '1237955463385247745-3oke3z4TL0oPrSyLKEzcZt8x2jAJir'
ACCESS_SECRET = 'yXhUcDYepyLx4uFn6W2A3vcHhXbDGqKKtPn9fTmTecb0A'


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    if mention.user.screen_name == 'SarahTech7':
        print(mention.text)
        api.update_status("@SarahTech7 hello Sarah!",mention.id)
