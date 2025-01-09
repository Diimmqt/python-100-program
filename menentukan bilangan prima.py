def cek_bilangan_prima(angka):
    # Bilangan kurang dari 2 bukan bilangan prima
    if angka < 2:
        return False

    # Cek pembagi dari 2 sampai √angka
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return False

    return True

# Tes fungsi
angka = int(input("Masukkan bilangan: "))
if cek_bilangan_prima(angka):
    print(f"{angka} adalah bilangan prima.")
else:
    print(f"{angka} bukan bilangan prima.")
