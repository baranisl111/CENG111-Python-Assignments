numaralı = {}
kusaklar = {}

def anafonk (L):
    global numaralı, kusaklar
    numaralı = {}
    kusaklar = {}


    numaralı[L[0]] = "1" 

    listem= []

    def numaraver (liste):
        sayı_1 = numaralı[liste[0]]
        sayı_2 = 1
        for i in liste[1:]:
            if type(i) == list:
                numaralı[i[0]] = f"{sayı_1}.{sayı_2}"
                listem.append(i)
            else:
                numaralı[i] = f"{sayı_1}.{sayı_2}"
            sayı_2 += 1
        
    numaraver(L)

    while not listem == []:
        for i in listem:
            numaraver(i)
            listem.remove(i)
    
    for isim, deger in numaralı.items():
        uzunluk = len(deger)//2 + 1

        if uzunluk not in kusaklar:
            kusaklar[uzunluk] = []

        kusaklar[uzunluk].append(isim)
    

def siblings(a,pname):
    anafonk(a)
    kardesleri = []
    nesili = len(numaralı[pname]) //2 + 1
    for i in kusaklar[nesili]:
        if numaralı[pname][:-1] == numaralı[i][:-1]:
            kardesleri.append(i)
    kardesleri.remove(pname)
    return kardesleri

def brothers(a,pname):
    anafonk(a)
    erkek_kardesleri = []
    nesili = len(numaralı[pname]) //2 + 1
    for i in kusaklar[nesili]:
        if numaralı[pname][:-1] == numaralı[i][:-1] and not i.istitle():
            erkek_kardesleri.append(i)
    if pname in erkek_kardesleri:
        erkek_kardesleri.remove(pname)
    return erkek_kardesleri

def sisters(a,pname):
    anafonk(a)
    kız_kardesleri = []
    nesili = len(numaralı[pname]) //2 + 1
    for i in kusaklar[nesili]:
        if numaralı[pname][:-1] == numaralı[i][:-1] and i.istitle():
            kız_kardesleri.append(i)
    if pname in kız_kardesleri:
        kız_kardesleri.remove(pname)
    return kız_kardesleri

def cousins(a,pname):
    anafonk(a)
    kuzenleri = []
    nesili = len(numaralı[pname]) //2 + 1
    for i in kusaklar[nesili]:
        if not numaralı[pname][:-1] == numaralı[i][:-1] and numaralı[pname][:-3] == numaralı[i][:-3]:
            kuzenleri.append(i)
    if pname in kuzenleri:    
        kuzenleri.remove(pname)
    return kuzenleri


def uncles(a,pname):
    anafonk(a)
    if numaralı[pname] == "1":
        return []
    amcaları = []
    nesili = len(numaralı[pname]) //2 + 1
    üst_kusagı = nesili - 1
    for i in kusaklar[üst_kusagı]:
        if numaralı[pname][:-4] == numaralı[i][:-2] and not numaralı[pname][:-2] == numaralı[i] and not i.istitle():
            amcaları.append(i)
    return amcaları

def aunts(a,pname):
    anafonk(a)
    if numaralı[pname] == "1":
        return []
    halaları = []
    nesili = len(numaralı[pname]) //2 + 1
    üst_kusagı = nesili - 1
    for i in kusaklar[üst_kusagı]:
        if numaralı[pname][:-4] == numaralı[i][:-2] and not numaralı[pname][:-2] == numaralı[i] and i.istitle():
            halaları.append(i)
    return halaları



    



    









