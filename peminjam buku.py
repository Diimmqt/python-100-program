import datetime

class Buku:
    def __init__(self, judul, penulis, jumlah):
        self.judul = judul
        self.penulis = penulis
        self.jumlah = jumlah
        self.peminjaman = 0  # Jumlah buku yang sedang dipinjam

    def tersedia(self):
        return self.jumlah - self.peminjaman > 0

    def pinjam(self):
        if self.tersedia():
            self.peminjaman += 1
            return True
        return False

    def kembalikan(self):
        if self.peminjaman > 0:
            self.peminjaman -= 1
            return True
        return False

    def info(self):
        return f"{self.judul} oleh {self.penulis} - Tersedia: {self.jumlah - self.peminjaman}"

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []  # Menyimpan daftar buku
        self.peminjaman_buku = []  # Menyimpan riwayat peminjaman buku

    def tambah_buku(self, judul, penulis, jumlah):
        buku = Buku(judul, penulis, jumlah)
        self.daftar_buku.append(buku)
        print(f"Buku '{judul}' berhasil ditambahkan.")

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("Tidak ada buku di perpustakaan.")
            return
        print("\nDaftar Buku:")
        for buku in self.daftar_buku:
            print(buku.info())

    def pinjam_buku(self):
        judul_buku = input("\nMasukkan judul buku yang ingin dipinjam: ").capitalize()
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul_buku.lower() and buku.pinjam():
                tanggal_pinjam = datetime.date.today()
                tanggal_kembali = tanggal_pinjam + datetime.timedelta(days=7)  # Peminjaman selama 7 hari
                self.peminjaman_buku.append({
                    "judul": buku.judul,
                    "tanggal_pinjam": tanggal_pinjam,
                    "tanggal_kembali": tanggal_kembali
                })
                print(f"Buku '{buku.judul}' berhasil dipinjam! Harap kembalikan pada {tanggal_kembali}")
                return
        print(f"Buku '{judul_buku}' tidak tersedia untuk dipinjam.")

    def kembalikan_buku(self):
        judul_buku = input("\nMasukkan judul buku yang ingin dikembalikan: ").capitalize()
        for peminjaman in self.peminjaman_buku:
            if peminjaman["judul"].lower() == judul_buku.lower():
                for buku in self.daftar_buku:
                    if buku.judul.lower() == peminjaman["judul"].lower():
                        if buku.kembalikan():
                            print(f"Buku '{judul_buku}' berhasil dikembalikan.")
                            self.peminjaman_buku.remove(peminjaman)
                            return
        print(f"Buku '{judul_buku}' tidak ditemukan dalam daftar peminjaman.")

    def tampilkan_peminjaman(self):
        if not self.peminjaman_buku:
            print("Belum ada buku yang dipinjam.")
            return
        print("\nRiwayat Peminjaman Buku:")
        for peminjaman in self.peminjaman_buku:
            print(f"{peminjaman['judul']} - Tanggal Pinjam: {peminjaman['tanggal_pinjam']} - Tanggal Kembali: {peminjaman['tanggal_kembali']}")

# Fungsi utama untuk menjalankan program
def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\nMenu Sistem Peminjaman Buku")
        print("1. Tambah Buku")
        print("2. Tampilkan Daftar Buku")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Tampilkan Peminjaman")
        print("6. Keluar")
        
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == "1":
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            jumlah = int(input("Masukkan jumlah buku: "))
            perpustakaan.tambah_buku(judul, penulis, jumlah)
        elif pilihan == "2":
            perpustakaan.tampilkan_buku()
        elif pilihan == "3":
            perpustakaan.pinjam_buku()
        elif pilihan == "4":
            perpustakaan.kembalikan_buku()
        elif pilihan == "5":
            perpustakaan.tampilkan_peminjaman()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan sistem peminjaman buku!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-6.")

if __name__ == "__main__":
    main()
