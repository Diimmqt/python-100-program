def tampilkan_tabel_perkalian(angka):
    print(f"Tabel Perkalian {angka}:")
    for i in range(1, 11):  # Tabel perkalian dari 1 sampai 10
        print(f"{angka} x {i} = {angka * i}")

# Input dari pengguna
angka = int(input("Masukkan angka untuk menampilkan tabel perkalian: "))

# Tampilkan tabel perkalian
tampilkan_tabel_perkalian(angka)
