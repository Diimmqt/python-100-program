def hitung_kata():
    # Meminta input teks dari pengguna
    teks = input("Masukkan teks yang ingin dihitung jumlah katanya: ")
    
    # Memisahkan teks menjadi kata-kata menggunakan spasi sebagai pemisah
    kata_list = teks.split()
    
    # Menghitung jumlah kata
    jumlah_kata = len(kata_list)
    
    # Menampilkan hasil
    print(f"Jumlah kata dalam teks tersebut adalah: {jumlah_kata}")

# Menjalankan program
hitung_kata()
