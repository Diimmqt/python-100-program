def balok():
    pl = int (input('masukan sisi pl:'))
    lt = int (input('masukan sisi lt:'))
    pt = int (input('masukan sisi pt:'))
    p = int (input('masukan panjang:'))
    l= int (input('masukan lebar:'))
    t = int (input('masukan tinggi:'))

    luas = lambda luas:2 * (pl + lt + pt)
    volume = lambda luas:p * l * t

    print ('luas\t\t:',luas(pl),'cm2')
    print ('volume\t\t:',volume(pl),'cm2')

balok()
balok()