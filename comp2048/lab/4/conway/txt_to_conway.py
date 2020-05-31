

import requests
url="http://www.conwaylife.com/patterns/5enginecordership.cells"
r=requests.get(url)
content=r.content.decode('utf8').strip()
stuff=[]
j=0
print(content)
for line in content.split('\r\n'):
    if line=="":
        j+=1
    elif line[0] == '!':
        j=-1
        next
    i=0
    for ch in line:
        if ch == "O":
             stuff.append((j,i))
        i+=1
    j+=1

print(stuff)
