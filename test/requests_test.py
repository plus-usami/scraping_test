import requests
r = requests.get("https://news.yahoo.co.jp/")

text = r.text
print(text)
