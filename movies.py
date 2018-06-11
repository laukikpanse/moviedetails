import tmdbsimple as tmdb
import json

#myPersonal API Key (NOTE: THIS IS NOT A PUBLIC API KEY DO NOT SHARE)
tmdb.API_KEY = '27a2ac6447494634cf14c5079a7da80b'

search = tmdb.Search()
response = search.movie(query=input("Please Enter your Movie name: "))
print("The Details of your movie are as follows: \n")
for s in search.results:
	print("\n\n Title: {0},\n\n ID: {1},\n\n Release Date: {2},\n\n Popularity: {3},\n\n Overview: \n {4:2}".format(s['title'], s['id'], s['release_date'], s['popularity'], s['overview']))


data = list(search.results)
with open('data.txt', 'w') as f:
  json.dump(data, f, ensure_ascii=False)
