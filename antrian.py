from collections import deque

def simulasi_antrian():
    antrian = deque()  # Menggunakan deque untuk struktur antrian
    while True:
        print("\n--- Simulasi Antrian ---")
        print("1. Tambah antrian")
        print("2. Hapus antrian (proses antrian)")
        print("3. Lihat antrian saat ini")
        print("4. Keluar")

        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == "1":
            nama = input("Masukkan nama yang akan ditambahkan ke antrian: ")
            antrian.append(nama)
            print(f"{nama} telah ditambahkan ke antrian.")
        
        elif pilihan == "2":
            if antrian:
                yang_diproses = antrian.popleft()  # Menghapus dari depan antrian
                print(f"{yang_diproses} telah diproses dan keluar dari antrian.")
            else:
                print("Antrian kosong! Tidak ada yang bisa diproses.")
        
        elif pilihan == "3":
            if antrian:
                print("Antrian saat ini:", antrian)
            else:
                print("Antrian kosong!")
        
        elif pilihan == "4":
            print("Terima kasih telah menggunakan simulasi antrian. Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1, 2, 3, atau 4.")

# Jalankan program
simulasi_antrian()
