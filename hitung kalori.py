def hitung_kalori():
    print("Selamat datang di aplikasi penghitungan kalori!\n")
    
    # Daftar makanan dan kalori per 100 gram
    makanan_kalori = {
        "Nasi Putih": 130,
        "Ayam Goreng": 250,
        "Telur Rebus": 155,
        "Apel": 52,
        "Pisang": 89,
        "Sayur Bayam": 23,
        "Roti Tawar": 265
    }

    # Menampilkan pilihan makanan
    print("Pilih makanan yang Anda konsumsi (ketik nama makanan):")
    for makanan in makanan_kalori:
        print(f"- {makanan}")
    
    pilihan_makanan = input("\nMasukkan nama makanan: ").strip()
    
    # Mengecek apakah makanan ada dalam daftar
    if pilihan_makanan in makanan_kalori:
        berat = float(input(f"Masukkan berat {pilihan_makanan} dalam gram: "))
        
        # Menghitung kalori
        kalori_per_100g = makanan_kalori[pilihan_makanan]
        total_kalori = (kalori_per_100g * berat) / 100
        
        print(f"Total kalori yang Anda konsumsi dari {berat} gram {pilihan_makanan} adalah {total_kalori:.2f} kalori.")
    else:
        print("Makanan tidak ditemukan dalam daftar.")

# Jalankan program
hitung_kalori()
