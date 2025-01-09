def hitung_pengeluaran():
    print("Selamat datang di aplikasi Pengelolaan Pengeluaran Bulanan!")
    
    # Input pengeluaran dari pengguna
    kebutuhan_pokok = float(input("Masukkan pengeluaran untuk kebutuhan pokok (makanan, minuman, dll): "))
    tagihan = float(input("Masukkan pengeluaran untuk tagihan (listrik, air, internet, dll): "))
    transportasi = float(input("Masukkan pengeluaran untuk transportasi (angkot, bensin, dll): "))
    hiburan = float(input("Masukkan pengeluaran untuk hiburan (bioskop, liburan, dll): "))
    tabungan = float(input("Masukkan pengeluaran untuk tabungan atau investasi: "))
    
    # Menjumlahkan semua pengeluaran
    total_pengeluaran = kebutuhan_pokok + tagihan + transportasi + hiburan + tabungan
    
    # Menampilkan hasil
    print("\nRincian Pengeluaran Bulanan Anda:")
    print(f"Kebutuhan Pokok: {kebutuhan_pokok:.2f}")
    print(f"Tagihan: {tagihan:.2f}")
    print(f"Transportasi: {transportasi:.2f}")
    print(f"Hiburan: {hiburan:.2f}")
    print(f"Tabungan/Investasi: {tabungan:.2f}")
    print(f"\nTotal Pengeluaran Bulanan: {total_pengeluaran:.2f}")
    
    return total_pengeluaran

# Menjalankan program
hitung_pengeluaran()
