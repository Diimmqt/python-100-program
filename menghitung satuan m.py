print ('='*30)
print ('menghitung satuan meter ke km')
print ('='*30)
operator = str (input('pilih satuan:mm,cm,dm,m,dam,hm:'))
angka= int (input("masukan angka satuan:"))

if operator == 'mm':
    res = angka / 1000000
elif operator == 'cm':
    res = angka / 100000
elif operator == 'dm':
    res = angka / 10000
elif operator == 'm':
    res = angka / 1000
elif operator == 'dam':
    res = angka /100
elif operator == 'hm':
    res = angka / 10

print (f'konvensi dari {operator} ke km adalah {res}')