subor=open('eu_sk.csv','r')
subor1=open('eu_cz.csv','r')
subor2=open('eu_en.csv','r')
eun=[]
eun1=[]
eun2=[]
for riadok in subor:
    riadok=riadok.strip()
    info=riadok.split(';')
    eu={}
    eu['štát']=info[0]
    eu['rok vstupu']=info[1]
    eu['počet obyvateľov']=info[2]
    eu['rozloha']=info[3]
    eu['HDP']=info[4]
    eu['počet miest']=info[5]
    eun.append(eu)
    
for riadok1 in subor1:
    riadok1=riadok1.strip()
    info1=riadok1.split(';')
    eu1={}
    eu1['štát']=info1[0]
    eu1['rok vstupu']=info1[1]
    eu1['počet obyvateľov']=info1[2]
    eu1['rozloha']=info1[3]
    eu1['HDP']=info1[4]
    eu1['počet miest']=info1[5]
    eun1.append(eu1)
    
for riadok2 in subor2:
    riadok2=riadok2.strip()
    info2=riadok2.split(';')
    eu2={}
    eu2['štát']=info2[0]
    eu['rok vstupu']=info2[2]
    eu2['počet obyvateľov']=info2[3]
    eu2['rozloha']=info2[4]
    eu2['HDP']=info2[5]
    eu2['počet miest']=info2[6]
    eun2.append(eu2)
kluce=list(eun[0].keys())

for i in kluce:
    for poc in range(len(eun)):
        if eun[poc].get(i)!=eun1[poc].get(i):
            print(eun[poc].get(i))
            print(eun1[poc].get(i))
            print('Medzi slovenskym a ceskym ',eun[poc].get('štát')+'m',' je rozdiel v ',i)

for i in kluce:
    for poc in range(len(eun)):
        if eun1[poc].get(i)!=eun2[poc].get(i):
            print(eun1[poc].get(i))
            print(eun2[poc].get(i))
            print('Medzi ceskym a anglickym ',eun[poc].get('štát')+'m',' je rozdiel v ',i)    

for i in kluce:
    for poc in range(len(eun)):
        if eun[poc].get(i)!=eun2[poc].get(i):
            print(eun[poc].get(i))
            print(eun2[poc].get(i))
            print('Medzi slovenskym a anglickym ',eun[poc].get('štát')+'m',' je rozdiel v ',i)
subor3=open('slovnik_krajin.csv','a')
rozloha=0

for i in range(3):
    subor3.write(eun[i].get('štát')+';'+eun1[i].get('štát')+';'+eun2[i].get('štát')+'\n')
