import tweepy



api = twitter.Api(consumer_key=['mlIlDkXPFGsP0tAakd0opBQuJ'],
                  consumer_secret=['KsfFiZahmfgVY1qo3g0dKjlOA9ZGdxQYXtUShIaimiCXKuamCH'],
                  access_token_key=['1409319150137212928-kHr9zYzeYJi0n1s9lRNGaOTmkQWzMs'],
                  access_token_secret=['ya6zk5B2epswthBhOyf2l7aCWUZ92lcWPvKiKd7e3ePvk'])
results = api.GetSearch(
    raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")

print(results)