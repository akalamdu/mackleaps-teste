archive=open("/home/mackleaps/Documents/entrada.txt","r")
a=[]
x=0
for line in archive:
    a.append(line)
while x<len(a):
    a[x]=a[x].split(" ")
    if a[x][0]=="\n":
        a.pop(x)
        x-=1
    x+=1
    
x=0
while x<len(a):
    y=0
    while y<len(a[x]):
        if a[x][y]=="" or a[x][y]=="\n":
            a[x].pop(y)
            y-=1
        y+=1
    x+=1
x=0
while x<len(a):
    y=0
    while y<len(a[x]):
        if a[x][y][-1]=="\n" or a[x][y][-1]=="." or a[x][y][-1]=="!" or a[x][y][-1]=="?" or a[x][y][-1]==",":
            while a[x][y][-1]=="\n" or a[x][y][-1]=="." or a[x][y][-1]=="!" or a[x][y][-1]=="?" or a[x][y][-1]==",":
                a[x][y]=a[x][y][0:-1]
        y+=1
    x+=1

y=0
x=0
z=1
while z<len(a):
    y=0
    while y<len(a[z]):
        a[x].append(a[z][y])
        y+=1
    z+=1

while x<len(a):
    y=0
    while y<len(a[x])-1:
        z=y+1
        while z<len(a[x]):
            if a[x][y]==a[x][z]:
                a[x].pop(z)
            else:
                z+=1
        y+=1
    x+=1

while len(a)>1:
    a.pop(1)

a[0].sort()
print(a)