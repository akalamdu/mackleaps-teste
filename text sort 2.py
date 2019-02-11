archive=open("/home/mackleaps/Documents/entrada.txt","r")
a=[]
b=[]
for x in archive:
    y=x.split(" ")
    b.append(y)
for z in b:
    for w in z:
        if z==b[0]:
            break
        b[0].append(w)
while len(b)>1:
    b.pop(1)
for li in b[0]:
    x=b[0].index(li)
    while b[0][x]=="" or b[0][x]=="\n":
        b[0].pop(x)
for c in b[0]:
    x=b[0].index(c)
    while b[0][x][-1]=="\n"or b[0][x][-1]=="." or b[0][x][-1]=="!" or b[0][x][-1]=="?" or b[0][x][-1]==",":
        b[0][x]=b[0][x][0:-1]
for d in b[0]:
    x=b[0].index(d)
    x+=1
    while x<len(b[0]):
        if d==b[0][x]:
            b[0].pop(x)
        else:
            x+=1
b[0].sort()
print(b)