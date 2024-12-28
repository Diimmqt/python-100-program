print ('='*40)
print ('mencari arus listrik dengan rumus ohm')
print ('='*40)

volt =  int (input('masukan tegangan listrik:'))
ohm = int (input("masukan hambatan listrik (ohm):"))

print ('l = v / R ')

res = volt / ohm

print (f'arus listrik ={res}')