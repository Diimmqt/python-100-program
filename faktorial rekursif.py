def faktorial(n):
    if n == 0 or n == 1:  # Basis: faktorial 0 atau 1 adalah 1
        return 1
    return n * faktorial(n - 1)  # Rekursif

# Input dari pengguna
angka = int(input("Masukkan bilangan: "))
if angka < 0:
    print("Faktorial tidak terdefinisi untuk bilangan negatif.")
else:
    print(f"Faktorial dari {angka} adalah {faktorial(angka)}")
