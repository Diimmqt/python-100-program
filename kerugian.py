def hitung_kerugian():
    harga_beli = float(input("Masukkan harga beli per barang: "))
    harga_jual = float(input("Masukkan harga jual per barang: "))
    jumlah_terjual = int(input("Masukkan jumlah barang yang terjual: "))

    total_beli = harga_beli * jumlah_terjual
    total_jual = harga_jual * jumlah_terjual
    kerugian = total_beli - total_jual

    if kerugian > 0:
        persen = (kerugian / total_beli) * 100
        print(f"Anda mengalami kerugian sebesar Rp{kerugian:,.2f} ({persen:.2f}%)")
    else:
        print("Tidak ada kerugian.")

# Jalankan program
hitung_kerugian()
