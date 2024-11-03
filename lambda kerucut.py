#kerucut

def kerucut():
    r = int (input('masukan jari jari:'))
    s = int (input('masukan sisi:'))
    t = int (input('masukan tinggi:'))

    volume = lambda volume: 1/3 * 3.14 * r**2 * t
    luas = lambda luas:  3.14 * r**2 + 3.14 * r * s

    print ('volume \t\t:',volume(r),'cm2')
    print ('luas \t\t:', luas (r),'cm2')

kerucut()
kerucut()