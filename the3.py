def area(Q,T):
    # Tüm Kesişim Noktalarını Bulma------------------------------------------------------------------------------------------------------------------------------------

    def fonksiyon_denklemi(a):  # [(4,2),(1,7)]
        if a[0][0] - a[1][0] == 0:
            return a[0][0]
        else:
            d1_x = (a[0][1] - a[1][1]) / (a[0][0] - a[1][0])  # -5/3
            d1_y = d1_x * -a[0][0] + a[0][1]  # 26/3
            return [d1_x, d1_y]  # y = d1_x.x + d1_y

    dörtgen_denklemleri = []
    üçgen_denklemleri = []
    for i in Q[:3]:
        dörtgen_denklemleri.append(fonksiyon_denklemi([i, Q[Q.index(i) + 1]]))
    dörtgen_denklemleri.append(fonksiyon_denklemi([Q[0], Q[-1]]))
    üçgen_denklemleri.append(fonksiyon_denklemi([T[0], T[1]]))
    üçgen_denklemleri.append(fonksiyon_denklemi([T[1], T[2]]))
    üçgen_denklemleri.append(fonksiyon_denklemi([T[2], T[0]]))
    kesişimler = []

    def kesişim_noktası(x, y):  # [-1.66,8.66],[4,-12]
        if x[0] == y[0]:
            pass
        else:
            kx = (x[1] - y[1]) / (y[0] - x[0])
            ky = kx * x[0] + x[1]
            return kx, ky

    for i in dörtgen_denklemleri:
        for j in üçgen_denklemleri:
            if type(i) == int and type(j) == int:  # İkiside dikey olduğu için kesişmezler.
                kesişimler.append(None)
            elif type(i) == int:  # Dikdörtgeninki dikey
                kesişimler.append((i, j[0] * i + j[1]))

            elif type(j) == int:  # Üçgeninki dikey
                kesişimler.append((j, i[0] * j + i[1]))

            else:
                kesişimler.append(kesişim_noktası(i, j))


    # Doğru Kesişim Noktalarını Bulma-------------------------------------------------------------------------------------------------------------------

    d1x = [Q[0][0], Q[1][0]]
    d1y = [Q[0][1], Q[1][1]]
    d2x = [Q[1][0], Q[2][0]]
    d2y = [Q[1][1], Q[2][1]]
    d3x = [Q[2][0], Q[3][0]]
    d3y = [Q[2][1], Q[3][1]]
    d4x = [Q[0][0], Q[3][0]]
    d4y = [Q[0][1], Q[3][1]]

    ü1x = [T[0][0], T[1][0]]
    ü1y = [T[0][1], T[1][1]]
    ü2x = [T[1][0], T[2][0]]
    ü2y = [T[1][1], T[2][1]]
    ü3x = [T[0][0], T[2][0]]                #or (min() == max() and abs(min() - kesişimler[][]) < 0.000001)
    ü3y = [T[0][1], T[2][1]]

    doğru_kesişimler = []

    if kesişimler[0] == None:
        pass
    else:
        if min(d1x) <= kesişimler[0][0] <= max(d1x) or (min(d1x) == max(d1x) and abs(min(d1x) - kesişimler[0][0]) < 0.000001):
        	if min(ü1x) <= kesişimler[0][0] <= max(ü1x) or (min(ü1x) == max(ü1x) and abs(min(ü1x) - kesişimler[0][0]) < 0.000001):
            		if min(d1y) <= kesişimler[0][1] <= max(d1y) or (min(d1y) == max(d1y) and abs(min(d1y) - kesişimler[0][1]) < 0.000001):
            			if min(ü1y) <= kesişimler[0][1] <= max(ü1y) or (min(ü1y) == max(ü1y) and abs(min(ü1y) - kesişimler[0][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[0])

    if kesişimler[1] == None:
        pass
    else:
        if min(d1x) <= kesişimler[1][0] <= max(d1x) or (min(d1x) == max(d1x) and abs(min(d1x) - kesişimler[1][0]) < 0.000001):
        	if min(ü2x) <= kesişimler[1][0] <= max(ü2x) or (min(ü2x) == max(ü2x) and abs(min(ü2x) - kesişimler[1][0]) < 0.000001):
            		if min(d1y) <= kesişimler[1][1] <= max(d1y) or (min(d1y) == max(d1y) and abs(min(d1y) - kesişimler[1][1]) < 0.000001):
            			if min(ü2y) <= kesişimler[1][1] <= max(ü2y) or (min(ü2y) == max(ü2y) and abs(min(ü2y) - kesişimler[1][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[1])

    if kesişimler[2] == None:
        pass
    else:
        if min(d1x) <= kesişimler[2][0] <= max(d1x) or (min(d1x) == max(d1x) and abs(min(d1x) - kesişimler[2][0]) < 0.000001):
        	if min(ü3x) <= kesişimler[2][0] <= max(ü3x) or (min(ü3x) == max(ü3x) and abs(min(ü3x) - kesişimler[2][0]) < 0.000001): 
            		if min(d1y) <= kesişimler[2][1] <= max(d1y) or (min(d1y) == max(d1y) and abs(min(d1y) - kesişimler[2][1]) < 0.000001):
            			if min(ü3y) <= kesişimler[2][1] <= max(ü3y) or (min(ü3y) == max(ü3y) and abs(min(ü3y) - kesişimler[2][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[2])

    if kesişimler[3] == None:
        pass
    else:
        if min(d2x) <= kesişimler[3][0] <= max(d2x) or (min(d2x) == max(d2x) and abs(min(d2x) - kesişimler[3][0]) < 0.000001):
        	if min(ü1x) <= kesişimler[3][0] <= max(ü1x) or (min(ü1x) == max(ü1x) and abs(min(ü1x) - kesişimler[3][0]) < 0.000001):
            		if min(d2y) <= kesişimler[3][1] <= max(d2y) or (min(d2y) == max(d2y) and abs(min(d2y) - kesişimler[3][1]) < 0.000001):
            			if min(ü1y) <= kesişimler[3][1] <= max(ü1y) or (min(ü1y) == max(ü1y) and abs(min(ü1y) - kesişimler[3][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[3])

    if kesişimler[4] == None:
        pass
    else:
        if min(d2x) <= kesişimler[4][0] <= max(d2x) or (min(d2x) == max(d2x) and abs(min(d2x) - kesişimler[4][0]) < 0.000001):
        	if min(ü2x) <= kesişimler[4][0] <= max(ü2x) or (min(ü2x) == max(ü2x) and abs(min(ü2x) - kesişimler[4][0]) < 0.000001):
            		if min(d2y) <= kesişimler[4][1] <= max(d2y) or (min(d2y) == max(d2y) and abs(min(d2y) - kesişimler[4][1]) < 0.000001):
            			if min(ü2y) <= kesişimler[4][1] <= max(ü2y) or (min(ü2y) == max(ü2y) and abs(min(ü2y) - kesişimler[4][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[4])

    if kesişimler[5] == None:
        pass 
    else:
        if min(d2x) <= kesişimler[5][0] <= max(d2x) or (min(d2x) == max(d2x) and abs(min(d2x) - kesişimler[5][0]) < 0.000001):
        	if min(ü3x) <= kesişimler[5][0] <= max(ü3x) or (min(ü3x) == max(ü3x) and abs(min(ü3x) - kesişimler[5][0]) < 0.000001):
            		if min(d2y) <= kesişimler[5][1] <= max(d2y) or (min(d2y) == max(d2y) and abs(min(d2y) - kesişimler[5][1]) < 0.000001):
            			if min(ü3y) <= kesişimler[5][1] <= max(ü3y) or (min(ü3y) == max(ü3y) and abs(min(ü3y) - kesişimler[5][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[5])

    if kesişimler[6] == None:
        pass
    else:
        if min(d3x) <= kesişimler[6][0] <= max(d3x) or (min(d3x) == max(d3x) and abs(min(d3x) - kesişimler[6][0]) < 0.000001):
        	if min(ü1x) <= kesişimler[6][0] <= max(ü1x) or (min(ü1x) == max(ü1x) and abs(min(ü1x) - kesişimler[6][0]) < 0.000001):
            		if min(d3y) <= kesişimler[6][1] <= max(d3y) or (min(d3y) == max(d3y) and abs(min(d3y) - kesişimler[6][1]) < 0.000001):
            			if min(ü1y) <= kesişimler[6][1] <= max(ü1y) or (min(ü1y) == max(ü1y) and abs(min(ü1y) - kesişimler[6][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[6])
    if kesişimler[7] == None:
        pass
    else:
        if min(d3x) <= kesişimler[7][0] <= max(d3x) or (min(d3x) == max(d3x) and abs(min(d3x) - kesişimler[7][0]) < 0.000001):
        	if min(ü2x) <= kesişimler[7][0] <= max(ü2x) or (min(ü2x) == max(ü2x) and abs(min(ü2x) - kesişimler[7][0]) < 0.000001):
            		if min(d3y) <= kesişimler[7][1] <= max(d3y) or (min(d3y) == max(d3y) and abs(min(d3y) - kesişimler[7][1]) < 0.000001):
            			if min(ü2y) <= kesişimler[7][1] <= max(ü2y) or (min(ü2y) == max(ü2y) and abs(min(ü2y) - kesişimler[7][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[7])

    if kesişimler[8] == None:
        pass
    else:
        if min(d3x) <= kesişimler[8][0] <= max(d3x) or (min(d3x) == max(d3x) and abs(min(d3x) - kesişimler[8][0]) < 0.000001):
        	if min(ü3x) <= kesişimler[8][0] <= max(ü3x) or (min(ü3x) == max(ü3x) and abs(min(ü3x) - kesişimler[8][0]) < 0.000001):
            		if min(d3y) <= kesişimler[8][1] <= max(d3y) or (min(d3y) == max(d3y) and abs(min(d3y) - kesişimler[8][1]) < 0.000001):
            			if min(ü3y) <= kesişimler[8][1] <= max(ü3y) or (min(ü3y) == max(ü3y) and abs(min(ü3y) - kesişimler[8][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[8])

    if kesişimler[9] == None:
        pass
    else:
        if min(d4x) <= kesişimler[9][0] <= max(d4x) or (min(d4x) == max(d4x) and abs(min(d4x) - kesişimler[9][0]) < 0.000001):
        	if min(ü1x) <= kesişimler[9][0] <= max(ü1x) or (min(ü1x) == max(ü1x) and abs(min(ü1x) - kesişimler[9][0]) < 0.000001):
            		if min(d4y) <= kesişimler[9][1] <= max(d4y) or (min(d4y) == max(d4y) and abs(min(d4y) - kesişimler[9][1]) < 0.000001):
            			if min(ü1y) <= kesişimler[9][1] <= max(ü1y) or (min(ü1y) == max(ü1y) and abs(min(ü1y) - kesişimler[9][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[9])

    if kesişimler[10] == None:
        pass
    else:
        if min(d4x) <= kesişimler[10][0] <= max(d4x) or (min(d4x) == max(d4x) and abs(min(d4x) - kesişimler[10][0]) < 0.000001):
        	if min(ü2x) <= kesişimler[10][0] <= max(ü2x) or (min(ü2x) == max(ü2x) and abs(min(ü2x) - kesişimler[10][0]) < 0.000001):
            		if min(d4y) <= kesişimler[10][1] <= max(d4y) or (min(d4y) == max(d4y) and abs(min(d4y) - kesişimler[10][1]) < 0.000001):
            			if min(ü2y) <= kesişimler[10][1] <= max(ü2y) or (min(ü2y) == max(ü2y) and abs(min(ü2y) - kesişimler[10][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[10])

    if kesişimler[11] == None:
        pass
    else:
        if min(d4x) <= kesişimler[11][0] <= max(d4x) or (min(d4x) == max(d4x) and abs(min(d4x) - kesişimler[11][0]) < 0.000001):
        	if min(ü3x) <= kesişimler[11][0] <= max(ü3x) or (min(ü3x) == max(ü3x) and abs(min(ü3x) - kesişimler[11][0]) < 0.000001):
            		if min(d4y) <= kesişimler[11][1] <= max(d4y) or (min(d4y) == max(d4y) and abs(min(d4y) - kesişimler[11][1]) < 0.000001):
            			if min(ü3y) <= kesişimler[11][1] <= max(ü3y) or (min(ü3y) == max(ü3y) and abs(min(ü3y) - kesişimler[11][1]) < 0.000001):
                			doğru_kesişimler.append(kesişimler[11])
                
    
    # Üçgenin içinde kalan köşeleri bulma--------------------------------------------------------------------------------------------------------------------------------

    def üçgen_içinde_mi(x, y, x1, y1, x2, y2, x3, y3):
        def yönelim(a, b, c, d, e, f):
            return (d - b) * (e - c) - (c - a) * (f - d)

        d1 = yönelim(x, y, x1, y1, x2, y2)
        d2 = yönelim(x, y, x2, y2, x3, y3)
        d3 = yönelim(x, y, x3, y3, x1, y1)
        if d1 < 0 and d2 < 0 and d3 < 0:
            return True
        elif d1 > 0 and d2 > 0 and d3 > 0:
            return True
        else:
            return False
    
    üçgenin_içinde_kalan_köşeler = []
    
    for i in Q:
        if üçgen_içinde_mi(i[0], i[1], T[0][0], T[0][1], T[1][0], T[1][1], T[2][0], T[2][1]):
            üçgenin_içinde_kalan_köşeler.append(i)

    # Dörtgenin içinde kalan köşeleri bulma-----------------------------------------------------------------------------------------------------------------------------------

    def dörtgen_içinde_mi(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
        def yönelim(a, b, c, d, e, f):
            return (d - b) * (e - c) - (c - a) * (f - d)

        d1 = yönelim(x, y, x1, y1, x2, y2)
        d2 = yönelim(x, y, x2, y2, x3, y3)
        d3 = yönelim(x, y, x3, y3, x4, y4)
        d4 = yönelim(x, y, x4, y4, x1, y1)
        if d1 < 0 and d2 < 0 and d3 < 0 and d4 < 0:
            return True
        elif d1 > 0 and d2 > 0 and d3 > 0 and d4 > 0:
            return True
        else:
            return False

    dörtgenin_içinde_kalan_köşeler = []

    for i in T:
        if dörtgen_içinde_mi(i[0], i[1], Q[0][0], Q[0][1], Q[1][0], Q[1][1], Q[2][0], Q[2][1], Q[3][0],
                             Q[3][1]):
            dörtgenin_içinde_kalan_köşeler.append(i)

    köşeler = doğru_kesişimler + üçgenin_içinde_kalan_köşeler + dörtgenin_içinde_kalan_köşeler
    
    if len(köşeler) == 0:
        return 0

    #Noktaları sıralama-----------------------------------------------------------------------------------------------------------------------------------------------------

    def merkez_noktası (a): #a burada köşeler listemiz
        toplam_x = []
        toplam_y = []
        for i in a:
            toplam_x.append(i[0])
        for i in a:
            toplam_y.append(i[1])
        merkez_x = sum(toplam_x) / len(köşeler)
        merkez_y = sum(toplam_y) / len(köşeler)
        return merkez_x,merkez_y

    import math

    def sıralama (a):
        açılar = []
        merkez = merkez_noktası(a)
        for i in a:
            açılar.append((math.atan2(i[1] - merkez[1], i[0] - merkez[0]) ,i))
        köşeler_sıralı = []
        sıralı = sorted(açılar)
        for i in sıralı:
            köşeler_sıralı.append(i[1])
        return köşeler_sıralı

    köşeler_sıralı = sıralama(köşeler)
    
    #Alan Hesaplama-----------------------------------------------------------------------------------------------------------------------------------------------------------
    köşeler_x = []
    köşeler_y = []
    for i in köşeler_sıralı:
        köşeler_x.append(i[0])
        köşeler_y.append(i[1])

    toplam_1 = []
    toplam_2 = []
    for n in range(len(köşeler_x)):
        toplam_1.append(köşeler_x[n] * (köşeler_y[1:] + [köşeler_y[0]])[n])

    for n in range(len(köşeler_x)):
        toplam_2.append(köşeler_y[n] * (köşeler_x[1:] + [köşeler_x[0]])[n])
        
    return abs(sum(toplam_1) - sum(toplam_2)) / 2
    

    


