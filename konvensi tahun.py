def konversi_tahun_ke_bulan_dan_hari(tahun):
    bulan = tahun * 12  # Setiap tahun memiliki 12 bulan
    hari = tahun * 365  # Menghitung hari dengan menganggap setiap tahun 365 hari (tanpa tahun kabisat)
    
    return bulan, hari

# Input dari pengguna
tahun = float(input("Masukkan jumlah tahun: "))

# Konversi dan tampilkan hasil
bulan, hari = konversi_tahun_ke_bulan_dan_hari(tahun)
print(f"{tahun} tahun setara dengan {bulan} bulan atau {hari} hari.")
