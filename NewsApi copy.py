import requests
import json

query= input("topic: ")
response = requests.get(f'https://newsapi.org/v2/everything?q={query}&from=2023-12-08&sortBy=publishedAt&apiKey=3d639551b6a3412387cc791df7f9d913')
news = json.loads(response.text)
print(news)

for article in news['articles']:
    print(article['title'])
    print(article['description'])
    print('----------------------------------------------------------------')