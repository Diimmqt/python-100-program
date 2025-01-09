def deret_aritmatika(suku_pertama, beda, jumlah_suku):
    deret = []
    for i in range(jumlah_suku):
        suku = suku_pertama + i * beda
        deret.append(suku)
    return deret

# Input dari pengguna
suku_pertama = int(input("Masukkan suku pertama: "))
beda = int(input("Masukkan beda (selisih antar suku): "))
jumlah_suku = int(input("Masukkan jumlah suku yang ingin ditampilkan: "))

# Menampilkan deret aritmatika
deret = deret_aritmatika(suku_pertama, beda, jumlah_suku)
print("Deret Aritmatika:", deret)
