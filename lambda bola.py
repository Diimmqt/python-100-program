#lambda bola

def bola():
    r = int (input('masukan jari jari:'))

    luas = lambda luas: 4 * 3.14 * r**2
    volume = lambda volume :4/3 * 3.14 * r**3

    print ('luas\t\t :',luas(r),'cm2')
    print('volume\t\t :',volume(r),'cm2')

bola()
bola()