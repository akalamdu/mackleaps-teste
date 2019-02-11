arquivo=open("/home/mackleaps/Documents/entrada.txt","r")
a=[]
b=0
x=0
z="0"
for y in arquivo:
    a.append(y)
y=0

for y in a:
    b=(y.split(" "))

print(b)

while x<len(b):
    z=b[x]
    z=z.lower()
    if z[-1]==",":
        b[x]=z[0:-1]
    if z[-1]=="\n":
         b[x]=z[0:-1]
    x+=1

x=0
while x<len(b):
    t=0
    while t<len(b)-1:
        if b[x]==b[t+1]:
            print(b)
            b.pop(t+1)
        t+=1
    x+=1

x=0

print(b)
