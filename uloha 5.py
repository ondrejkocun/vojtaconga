import tkinter
canvas = tkinter.Canvas(width=700, height=320)
canvas.pack()

def analyzuj(meno_suboru):
    subor = open(meno_suboru, 'r')  
    frekvencia = {}
    for riadok in subor:
        riadok = riadok.lower()
        for znak in riadok:
            if 'a' <= znak <= 'z':
                frekvencia[znak] = frekvencia.get(znak, 0) + 1
    subor.close()
    zoradene = sorted(frekvencia, key=frekvencia.get, reverse=True)
    for kluc in zoradene:
        print(kluc, frekvencia.get(kluc))
    return zoradene

def kresli_stlpec(x, y, dx, dy, znaky):
    fa, fb = 'yellow', 'lightblue'
    for znak in znaky:
        canvas.create_rectangle(x, y, x+dx, y+dy, fill=fa)
        canvas.create_text(x+dx/2, y+dy/2, text=znak)
        y += dy
        fb, fa = fa, fb

def kresli_tabulku(x, y, meno_suboru):
    velkost = 300
    pocet_casti = 2
    dx = 50
    spracovat = analyzuj(meno_suboru)
    while len(spracovat) > 0:
        kresli_stlpec(x,y,dx,velkost/pocet_casti,spracovat[:pocet_casti])
        spracovat = spracovat[pocet_casti:]
        x += dx
        pocet_casti *= 2

kresli_tabulku(10, 10, 'anglicke_texty.txt')
kresli_tabulku(310, 10, 'slovenske_texty.txt')
