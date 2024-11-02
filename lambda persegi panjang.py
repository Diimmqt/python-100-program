#lambda persegi panjang

def persegiPanjang():
    p = int (input('masukan panjang\t\t:'))
    l = int (input('masukan lebar\t\t:'))

    keliling = lambda keliling : 2 * (p * l) 
    luas = lambda luas: p * l

    print ('keliling\t\t:',keliling (p),'cm2')
    print ('luas \t\t:',luas (p),'cm2')

persegiPanjang()
persegiPanjang()
persegiPanjang()