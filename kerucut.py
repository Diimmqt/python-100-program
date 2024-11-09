r = int (input('masukan jari jari: '))
t = int (input('masukan tinggi:'))
s = int (input('masukan sisi pelukis'))


volume = 1/3 * 3.14 * r * r * t
luas =  3.14 * r**2 + 3.14 * r * s
keliling = 2 * 3.14 * r

print (f'volume = {volume}')
print (f' luas = {luas}')
print (f'keliling = {keliling}')