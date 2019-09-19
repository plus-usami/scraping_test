import urllib.request as request
import datetime
import json

API = "http://api.aoikujira.com/time/get.php"
data = request.urlopen(API).read()

data = data.decode('utf-8') + "test"

t = datetime.date.today()
fname = t.strftime("%Y-%m-%d") + ".json"

with open(fname, "w", encoding="utf-8") as f:
  f.write(data)
