import os

# Nama file tempat menyimpan kontak
FILENAME = "kontak.txt"

# Fungsi untuk menampilkan daftar kontak
def tampilkan_kontak():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            kontak = file.readlines()
            if kontak:
                print("\nDaftar Kontak:")
                for i, line in enumerate(kontak, start=1):
                    print(f"{i}. {line.strip()}")
            else:
                print("Tidak ada kontak yang tersimpan.")
    else:
        print("Tidak ada data kontak.")

# Fungsi untuk menambahkan kontak baru
def tambah_kontak():
    nama = input("Masukkan nama kontak: ")
    nomor_telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan alamat email: ")
    
    with open(FILENAME, "a") as file:
        file.write(f"{nama} | {nomor_telepon} | {email}\n")
    
    print(f"Kontak {nama} berhasil ditambahkan!")

# Fungsi untuk menghapus kontak berdasarkan nomor urut
def hapus_kontak():
    tampilkan_kontak()
    try:
        nomor_kontak = int(input("Masukkan nomor kontak yang ingin dihapus: "))
        with open(FILENAME, "r") as file:
            kontak = file.readlines()

        if 0 < nomor_kontak <= len(kontak):
            del kontak[nomor_kontak - 1]
            with open(FILENAME, "w") as file:
                file.writelines(kontak)
            print("Kontak berhasil dihapus!")
        else:
            print("Nomor kontak tidak valid.")
    except ValueError:
        print("Masukkan nomor yang valid.")

# Fungsi untuk mencari kontak berdasarkan nama
def cari_kontak():
    nama_cari = input("Masukkan nama kontak yang ingin dicari: ").lower()
    with open(FILENAME, "r") as file:
        kontak = file.readlines()
        ditemukan = False
        for line in kontak:
            if nama_cari in line.lower():
                print(f"Ditemukan: {line.strip()}")
                ditemukan = True
        if not ditemukan:
            print("Kontak tidak ditemukan.")

# Fungsi untuk mengedit kontak berdasarkan nomor urut
def edit_kontak():
    tampilkan_kontak()
    try:
        nomor_kontak = int(input("Masukkan nomor kontak yang ingin diedit: "))
        with open(FILENAME, "r") as file:
            kontak = file.readlines()

        if 0 < nomor_kontak <= len(kontak):
            kontak_data = kontak[nomor_kontak - 1].strip().split(" | ")
            nama_baru = input(f"Masukkan nama baru (current: {kontak_data[0]}): ") or kontak_data[0]
            nomor_baru = input(f"Masukkan nomor baru (current: {kontak_data[1]}): ") or kontak_data[1]
            email_baru = input(f"Masukkan email baru (current: {kontak_data[2]}): ") or kontak_data[2]

            kontak[nomor_kontak - 1] = f"{nama_baru} | {nomor_baru} | {email_baru}\n"
            with open(FILENAME, "w") as file:
                file.writelines(kontak)
            print("Kontak berhasil diedit!")
        else:
            print("Nomor kontak tidak valid.")
    except ValueError:
        print("Masukkan nomor yang valid.")

# Menu Utama
def menu():
    while True:
        print("\nSistem Manajemen Kontak")
        print("1. Tampilkan Kontak")
        print("2. Tambah Kontak")
        print("3. Hapus Kontak")
        print("4. Cari Kontak")
        print("5. Edit Kontak")
        print("6. Keluar")

        pilihan = input("Pilih opsi (1-6): ")
        if pilihan == "1":
            tampilkan_kontak()
        elif pilihan == "2":
            tambah_kontak()
        elif pilihan == "3":
            hapus_kontak()
        elif pilihan == "4":
            cari_kontak()
        elif pilihan == "5":
            edit_kontak()
        elif pilihan == "6":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-6.")

if __name__ == "__main__":
    menu()
