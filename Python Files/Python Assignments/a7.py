import urllib.request, urllib.parse, urllib.error
import json

msrc = "http://py4e-data.dr-chuck.net/json?"

while True:
    address = input('Enter : ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    parms['key'] = 42
    url = msrc + urllib.parse.urlencode(parms)
    files = urllib.request.urlopen(url).read().decode()
    try:
        file = json.loads(files)
    except:
        file = None

    print(file['results'][0]['place_id'])
