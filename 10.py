import tkinter
canvas = tkinter.Canvas(width=1000, height=800)
canvas.pack()
subor = open('slovne_hodnotenia.txt', 'r',encoding='utf-8')
subor1 = open('vynimky.txt', 'r',encoding='utf-8')
subor2 = open('pocetnost.txt', 'w',encoding='utf-8')

vynimky = []
pocetnost = {}
p=0

for riadok in subor:
    r = riadok.replace(',', '')
    slova = riadok.split()
    for slovo in slova:
        pocetnost[slovo] = pocetnost.get(slovo, 0) +1
        p+=1
subor.close()
for riadok in subor1:
    vynimky=riadok.split()
subor1.close()
zoznam=[]
for ntica in pocetnost.items():
    zoznam.append((ntica[1],ntica[0]))
zoznamm.sort(reverse=True)
kopia=[]
for i in zoznamm:
    if len(i[1])>=3 or i[1] in vynimmky:
        kopia.append(prvok)
    percento=(i[0]/p)*100
    subor2.write(i[1]+';'+str(prvok[0])+';'+str(percento)+'%'+'\n')
subor2.close()
def obdlznik(poradie,vyska,farba):
    canvas.create_rectangle(poradie*20+10,maxy-100,poradie*20+10+10,maxy-100-vyska//2,fill=farba,tags='obdlznik'+str(poradie))
poradie=0
maxy=800

for pocet,slovo in kopia[:40]:
    obdlznik(poradie,pocet,'blue')
    canvas.create_text(poradie*20+15,maxy-50,text=slovo,font='Arial 8',angle=90)
    poradie+=1
def mys(event):
    global rozsvietene
    if rozsvietene!=None:
        canvas.delete('obdlznik'+str(rozsvietene))
        obdlznik(rozsvietene,kopia[rozsvietene][0],'blue')
    canvas.delete('info')
    if event.y<700 and 10<sur.x<40*20:
        ktory=(sur.x-10)//20
        canvas.delete('obdlznik'+str(ktory))
        obdlznik(ktory,kopia[ktory][0],'red')
        canvas.create_text(500,100,text=kopia[ktory][1]+'\n'+str(kopia[ktory][0]),font='Arial 30',tags='info')
        rozsvietene=ktory
rozsvietene=None
canvas.bind('<Motion>',mys)
