def kalkulator_diskon(harga_awal, persentase_diskon):
    """Menghitung harga setelah diskon"""
    diskon = (persentase_diskon / 100) * harga_awal  # Menghitung diskon
    harga_setelah_diskon = harga_awal - diskon  # Mengurangi harga awal dengan diskon
    return diskon, harga_setelah_diskon

# Input dari pengguna
harga_awal = float(input("Masukkan harga awal barang: "))
persentase_diskon = float(input("Masukkan persentase diskon (%): "))

# Hitung diskon dan harga setelah diskon
diskon, harga_setelah_diskon = kalkulator_diskon(harga_awal, persentase_diskon)

# Tampilkan hasil
print(f"Diskon yang diberikan: Rp {diskon:,.2f}")
print(f"Harga setelah diskon: Rp {harga_setelah_diskon:,.2f}")
