def cek_ganjil_genap(angka):
    angka= int(input("masukan angka:"))
    
    if angka % 2 == 0:
        return "Genap"  # Mengembalikan string "Genap"
    else:
        return "Ganjil"  # Mengembalikan string "Ganjil"

# Memanggil fungsi dan menyimpan hasilnya
hasil = cek_ganjil_genap(7)
print(f"hasil: {hasil}")
