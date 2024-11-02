#lambda tabung

def tabung():
    r= int (input('masukan jari jari\t\t:'))
    t= int (input ('masukan tinggi\t\t:'))

    volume = lambda volume : 3.14 * r**2 * t
    keliling = lambda keliling: 2 * 3.14 * r
    luas = lambda luas :2 * 3.14 * r**2

    print ('volume \t\t:',volume(r),'cm2')
    print ('keliling\t\t:',keliling(r),'cm2')
    print ('luas\t\t:',luas (r),'cm2')

tabung ()
tabung ()