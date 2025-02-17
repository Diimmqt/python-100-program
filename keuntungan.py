def hitung_keuntungan():
    harga_beli = float(input("Masukkan harga beli per barang: "))
    harga_jual = float(input("Masukkan harga jual per barang: "))
    jumlah_terjual = int(input("Masukkan jumlah barang yang terjual: "))

    total_beli = harga_beli * jumlah_terjual
    total_jual = harga_jual * jumlah_terjual
    keuntungan = total_jual - total_beli

    if keuntungan > 0:
        persen = (keuntungan / total_beli) * 100
        print(f"Anda mendapatkan keuntungan sebesar Rp{keuntungan:,.2f} ({persen:.2f}%)")
    else:
        print("Tidak ada keuntungan.")

# Jalankan program
hitung_keuntungan()
