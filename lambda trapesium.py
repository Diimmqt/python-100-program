def trapesium():
    a =int (input('masukan sisi a: '))
    b = int (input('masukan sisi b: '))
    c= int (input('masukan sisi c: '))
    d = int (input('masukan sisi d: '))
    tinggi =int (input('masukan sisi tinggi: '))


    luas = lambda luas: a + b + c +d
    keliling = lambda keliling:  (a + b) * tinggi /2

    print ('luas\t\t:',luas(a),'cm2')
    print ('keliling\t\t:',keliling(a),"cm2")

trapesium()
trapesium()