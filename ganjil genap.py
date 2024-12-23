def cek_ganjil_genap(angka):
    angka= int(input("masukan angka plat nomer anda:"))
    
    if angka % 2 == 0:
        return "Genap"  # Mengembalikan string "Genap"
    else:
        return "Ganjil"  # Mengembalikan string "Ganjil"

# Memanggil fungsi dan menyimpan hasilnya
hasil = cek_ganjil_genap(0)
print(f"plat nomer anda adalah {hasil}")
