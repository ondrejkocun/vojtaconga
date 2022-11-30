subor = open('osoby.txt', 'r')
osoby = []
rok=int(input('zadaj rok narodenia '))
miesto=input('zadaj miesto narodenia ')
vybrany=''
najvyssi=0
najmladsi=100
nc1=' '
nc=' '
for riadok in subor:
    info = riadok.split(';')
    osoba = {}
    osoba['meno'] = info[0]
    osoba['vyska'] = int(info[1])
    osoba['roknarodenia'] = int(info[2])
    osoba['rodisko'] = info[3].strip()
    osoby.append(osoba)
    if najvyssi <int(info[1]):
        najvyssi=int(info[1])
        nc=info[0]
    if int(info[2])==rok:
        vybrany+=info[0]+' '
    if info[3]==miesto:
        vybrany+=info[0]+' '
    if 2022-int(info[2])<najmladsi:
        najmladsi=2022-int(info[2])
        nc1=info[0]
subor.close()
print(osoby)
print(vybrany)
print('Najvyssi clovek je ',nc,'a meria',najvyssi)
print('Najmladsi clovek je ',nc1,'a ma',najmladsi)
