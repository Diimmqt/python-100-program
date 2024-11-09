def suhu():
    celcius = int (input('masukan suhu di sekitar anda:'))

    farenheit= lambda farenheit: celcius * (9/5) + 32
    kelvin = lambda kelvin:celcius + 273

    print ('farenheit\t\t:',farenheit(celcius))
    print ('kelvin\t\t:',kelvin(celcius))

suhu()
suhu()