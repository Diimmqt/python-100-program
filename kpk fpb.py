import math

def hitung_fpb(a, b):
    """Menghitung FPB menggunakan fungsi bawaan math.gcd"""
    return math.gcd(a, b)

def hitung_kpk(a, b):
    """Menghitung KPK menggunakan rumus KPK = (a * b) // FPB"""
    fpb = hitung_fpb(a, b)
    return (a * b) // fpb

# Input dari pengguna
print("=== Program Menghitung KPK dan FPB ===")
angka1 = int(input("Masukkan bilangan pertama: "))
angka2 = int(input("Masukkan bilangan kedua: "))

# Hitung FPB dan KPK
fpb = hitung_fpb(angka1, angka2)
kpk = hitung_kpk(angka1, angka2)

# Tampilkan hasil
print(f"FPB dari {angka1} dan {angka2} adalah: {fpb}")
print(f"KPK dari {angka1} dan {angka2} adalah: {kpk}")
