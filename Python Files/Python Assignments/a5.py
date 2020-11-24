import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input("Enter - ")
xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)
lst = tree.findall('comments/comment')
sum=0
for i in lst:
    sum= sum+int(i.find('count').text)
print(sum)
