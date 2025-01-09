def konversi_detik_ke_jam(detik):
    jam = detik // 3600  # Hitung jumlah jam
    sisa_detik = detik % 3600  # Sisa detik setelah jam
    menit = sisa_detik // 60  # Hitung jumlah menit
    detik_akhir = sisa_detik % 60  # Sisa detik setelah menit
    
    return jam, menit, detik_akhir
  
# Input dari pengguna
total_detik = int(input("Masukkan jumlah detik: "))

# Konversi dan tampilkan hasil
jam, menit, detik = konversi_detik_ke_jam(total_detik)
print(f"{total_detik} detik setara dengan {jam} jam, {menit} menit, dan {detik} detik.")
