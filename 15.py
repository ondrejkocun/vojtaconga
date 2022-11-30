subor=open('osoby.csv','r')
osoby=[]
for riadok in subor:
    info=riadok.strip()
    info=info.replace(';','')
    info=info.split(' ')
    osoba={}
    osoba['meno']=info[0]
    osoba['priezvisko']=info[1]
    osoby.append(osoba)
print(osoby)

