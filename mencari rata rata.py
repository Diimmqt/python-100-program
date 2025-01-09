def hitung_rata_rata():
    try:
        # Meminta pengguna untuk memasukkan angka-angka
        angka_input = input("Masukkan angka-angka yang ingin dihitung rata-ratanya, pisahkan dengan spasi: ")
        
        # Mengubah input string menjadi list angka
        angka_list = [float(angka) for angka in angka_input.split()]
        
        if len(angka_list) == 0:
            print("Tidak ada angka yang dimasukkan!")
            return
        
        # Menghitung jumlah dan banyaknya angka
        jumlah_angka = sum(angka_list)
        banyak_angka = len(angka_list)
        
        # Menghitung rata-rata
        rata_rata = jumlah_angka / banyak_angka
        
        # Menampilkan hasil
        print(f"Rata-rata dari angka-angka yang dimasukkan adalah: {rata_rata:.2f}")
    
    except ValueError:
        print("Masukkan angka yang valid!")

# Menjalankan fungsi
hitung_rata_rata()
