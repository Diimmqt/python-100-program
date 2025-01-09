def tampilkan_tabel_pembagian(angka):
    print(f"Tabel Pembagian {angka}:")
    for i in range(1, 11):  # Tabel pembagian dari 1 sampai 10
        if i != 0:
            hasil = angka / i
            print(f"{angka} ÷ {i} = {hasil:.2f}")  # Menampilkan hasil dengan 2 angka di belakang koma

# Input dari pengguna
angka = int(input("Masukkan angka untuk menampilkan tabel pembagian: "))

# Tampilkan tabel pembagian
tampilkan_tabel_pembagian(angka)
