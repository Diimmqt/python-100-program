import math

def cek_kuadrat_sempurna():
    angka = int(input("Masukkan angka: "))
    
    # Mencari akar kuadrat dari angka
    akar = math.sqrt(angka)
    
    # Mengecek apakah akar kuadratnya adalah bilangan bulat
    if akar.is_integer():
        print(f"{angka} adalah kuadrat sempurna!")
    else:
        print(f"{angka} bukan kuadrat sempurna!")

# Jalankan program
cek_kuadrat_sempurna()
