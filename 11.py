import random
subor = open('slovne_hodnotenia.txt', 'r',encoding='utf-8')
celytext = subor.read()
celytext = celytext.split()
subor.close()
slova=[]
for slovo in celytext:
    if not slovo in slova:
        slova.append(slovo)
slova_zamiesane=slova[:]
random.shuffle(slova_zamiesane)
substitucia={}
for i in range(len(slova)):
    substitucia[slova[i]]=slova_zamiesane[i]
celytext_sifrovany=''
for slovo in celytext:
    celytext_sifrovany+=slova_zamiesane[i]
celytext_sifrovany=''
for slov in celytext:
    celytext_sifrovany+=substitucia[slovo]
subor_sifrovany = open('slovne_hodnotenia_sifrovane.txt', 'w')
subor_sifrovany.write(celytext_sifrovany)
subor_sifrovany.close()
subor_tabulka = open('slovne_hodnotenia_kluc.txt', 'w')
for kluc, hodnota in substitucia.items():
    subor_tabulka.write(kluc+';'+hodnota+';')
subor_tabulka.close()
