#拠点間のルート取得
encoding = 'utf-8'

import urllib
import urllib2
import json

url = urllib2.urlopen("https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key=APIkey")
route = str(url.read())
jroute = json.loads(route)
print jroute.keys()
test = jroute['routes']
test = test.lstrip('[')
test = test.rstrip(']')
test = json.loads(test)

#天気情報の取得
tenkiurl = urllib2.urlopen("https://api.yumake.jp/1.1/forecastPref.php?code=13&key=APIkey&format=json")
tenki = tenkiurl.read()
jtenki = json.loads(tenki)

#どちらもjsonの処理が上手くいかない
