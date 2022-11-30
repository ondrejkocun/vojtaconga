def analyzuj(meno_suboru):
    subor = open(meno_suboru, 'r')
    SK_znaky = 'áäčďéíľĺňóôšťúýž'
    frekvencia = {}
    pocet = 0
    for riadok in subor:
        riadok = riadok.lower()
        for znak in riadok:
            if 'a' <= znak <= 'z' or znak in SK_znaky:
                frekvencia[znak] = frekvencia.get(znak, 0) + 1
                pocet += 1
    subor.close()
    zoradene = sorted(frekvencia, key=frekvencia.get, reverse=True)
    for kluc in zoradene:
        percento = frekvencia.get(kluc) / pocet * 100
        print(kluc, frekvencia.get(kluc), '{:5.2f} %'.format(percento))
        
analyzuj('slovenske_texty.txt')
