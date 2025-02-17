def cari_angka_terbesar():
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    if angka1 > angka2:
        print(f"Angka terbesar adalah {angka1}")
    elif angka1 < angka2:
        print(f"Angka terbesar adalah {angka2}")
    else:
        print("Kedua angka tersebut sama.")

# Jalankan program
cari_angka_terbesar()
