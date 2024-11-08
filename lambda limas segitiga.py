def limasSegitiga():
    la =int (input('masukan luas alas:'))
    ls = int (input('masukan luas sisi:'))
    t = int (input('masukan tinggi:'))

    luas = lambda luas:la + ls
    volume = lambda volume: 1/3 * la * t

    print ('luas\t\t:',luas(la),'cm2')
    print ('volume\t\t:',volume(la),'cm2')

limasSegitiga()
limasSegitiga()