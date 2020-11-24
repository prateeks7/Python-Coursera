import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter Url : ')
file = urllib.request.urlopen(url).read()
files = json.loads(file)
sum=0

for i in files['comments']:
    sum = sum + int(i['count'])
print(sum)
