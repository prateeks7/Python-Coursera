import re
hand = open('assignment1.txt')
ans=0
alll = hand.read()
col = re.findall('[0-9]+',alll)
for i in col:
    ans = ans + int(i)
print(ans)
