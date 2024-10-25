#layang layang

sisipendek= int (input('masukan sisi pendek: '))
sisipanjang= int (input('masukan sisi panjang: '))
d1 = int (input ('masukan diagonal 1:'))
d2 = int (input ('masukan diagonal 2:'))

luas =1 * d1  * d2  / 2
keliling = sisipendek + sisipendek + sisipanjang + sisipanjang

print (f'luas={luas}')
print (f'keliling={keliling}')