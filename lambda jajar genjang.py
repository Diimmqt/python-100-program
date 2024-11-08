def JajarGenjang():
    sisi_a = int (input('masukan sisi a: '))
    sisi_b = int (input('masukan sisi b:'))
    tinggi = int (input('masukan tinggi:'))

    keliling =lambda keliling: sisi_a * tinggi
    luas = lambda luas:2 *(sisi_a + sisi_b)

    print ('keliling\t\t:',keliling(sisi_a),'cm2')
    print('luas\t\t:',luas(sisi_a),'cm2')

JajarGenjang()
JajarGenjang()