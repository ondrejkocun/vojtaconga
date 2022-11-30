import tkinter
canvas = tkinter.Canvas(width=700, height=320)
canvas.pack()

def analyzuj(meno_suboru):
    subor = open(meno_suboru, 'r',encoding='utf-8')
    frekvencia = {}
    pocet = 0
    for riadok in subor:
        riadok = riadok.lower()
        for znak in riadok:
            if 'a' <= znak <= 'z':
                frekvencia[znak] = frekvencia.get(znak, 0) + 1
                pocet += 1
    subor.close()
    zoradene = sorted(frekvencia, key=frekvencia.get, reverse=True)
    vystup = []
    for kluc in zoradene:
        podiel = frekvencia.get(kluc) / pocet * 1000
        vystup.append((kluc, frekvencia.get(kluc), podiel))
    return vystup

def histogram(x, y, dx, f, meno_suboru):
    udaje = analyzuj(meno_suboru)
    pocet = 0
    for znak, frekv, podiel in udaje:
        canvas.create_rectangle(x+pocet*dx, y, x+pocet*dx+10, y-podiel*2, fill=f)
        canvas.create_text(x+pocet*dx+5, y+10, text=znak, fill=f)
        percento = '{:5.2f} %'.format(podiel/10)
        canvas.create_text(x+pocet*dx+5, y-podiel*2-30, text=percento, angle=90)    
        pocet += 1
        
histogram(10, 300, 25, 'blue', 'anglicke_texty.txt')
histogram(20, 300, 25, 'red', 'slovenske_texty.txt')

