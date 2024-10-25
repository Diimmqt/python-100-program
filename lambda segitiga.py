def segitiga():
    a = int (input('masukan alas:'))
    t = int (input('masukan tinggi :'))
    sisi = int (input('masukan sisi'))

    l = lambda a : a * t  / 2
    k = lambda a : sisi + sisi + sisi

    print ('luas\t\t:',l (a),'cm2')
    print ('keliling\t\t:',k(sisi),'cm')