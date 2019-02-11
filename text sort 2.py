archive=open("/home/mackleaps/Documents/entrada.txt","r")
a=[]
b=[]
#copia as linhas do texto para uma lista
for x in archive:     
    y=x.split(" ")
    b.append(y)
#copia todos os itens das listas para a primeira
for z in b:
    for w in z:
        if z==b[0]:
            break
        b[0].append(w)
#apaga as listas que nao sejam a primeira
while len(b)>1:
    b.pop(1)
#retira termos inuteis como espaços em branco
for li in b[0]:
    x=b[0].index(li)
    while b[0][x]=="" or b[0][x]=="\n":
        b[0].pop(x)
#checa o ultimo termo da list e o retira se nao for uma letra
for c in b[0]:
    x=b[0].index(c)
    while b[0][x][-1]=="\n"or b[0][x][-1]=="." or b[0][x][-1]=="!" or b[0][x][-1]=="?" or b[0][x][-1]==",":
        b[0][x]=b[0][x][0:-1]
#apaga os termos repetidos
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