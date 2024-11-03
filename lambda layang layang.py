#lambda layang layang

def layanglayang():
    sisipendek= int (input('masukan sisi pendek: '))
    sisipanjang= int (input('masukan sisi panjang: '))
    d1 = int (input ('masukan diagonal 1:'))    
    d2 = int (input ('masukan diagonal 2:'))

    luas = lambda luas : 1 * d1  * d2  / 2
    keliling = lambda luas :sisipendek + sisipendek + sisipanjang + sisipanjang

    print ('luas \t\t :', luas (sisipendek),'cm2')
    print ('keliling\t\t :',keliling(sisipendek),'cm2')

layanglayang()
layanglayang()