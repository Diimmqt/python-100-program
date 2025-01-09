class PemesananTiket:
    def __init__(self):
        # Data destinasi dan harga tiket
        self.destinasi = {
            "Jakarta": 100000,  # Harga tiket dalam Rupiah
            "Bali": 150000,
            "Yogyakarta": 120000,
            "Surabaya": 130000
        }
        self.pemesanan = []  # Menyimpan daftar pemesanan pengguna

    def tampilkan_destinasi(self):
        print("Destinasi yang tersedia:")
        for destinasi, harga in self.destinasi.items():
            print(f"- {destinasi}: Rp {harga}")

    def pesan_tiket(self):
        print("\nSistem Pemesanan Tiket")
        self.tampilkan_destinasi()

        # Memilih destinasi
        destinasi_pilihan = input("\nMasukkan nama destinasi yang ingin Anda pilih: ").capitalize()

        if destinasi_pilihan not in self.destinasi:
            print("Destinasi tidak ditemukan. Silakan pilih destinasi yang valid.")
            return

        # Memilih jumlah tiket
        try:
            jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
            if jumlah_tiket <= 0:
                print("Jumlah tiket harus lebih dari 0.")
                return
        except ValueError:
            print("Masukkan jumlah tiket yang valid.")
            return

        # Menghitung total harga
        harga_tiket = self.destinasi[destinasi_pilihan]
        total_harga = harga_tiket * jumlah_tiket

        # Menyimpan pemesanan
        self.pemesanan.append({
            "destinasi": destinasi_pilihan,
            "jumlah_tiket": jumlah_tiket,
            "total_harga": total_harga
        })

        print(f"\nPemesanan berhasil!\nTotal harga untuk {jumlah_tiket} tiket ke {destinasi_pilihan} adalah: Rp {total_harga}")

    def tampilkan_pemesanan(self):
        if not self.pemesanan:
            print("Belum ada pemesanan.")
            return

        print("\nDaftar Pemesanan Tiket:")
        for i, pemesanan in enumerate(self.pemesanan, 1):
            print(f"{i}. {pemesanan['jumlah_tiket']} tiket ke {pemesanan['destinasi']} - Rp {pemesanan['total_harga']}")

# Fungsi utama untuk menjalankan program
def main():
    sistem = PemesananTiket()

    while True:
        print("\nMenu Pemesanan Tiket")
        print("1. Pesan Tiket")
        print("2. Lihat Pemesanan")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1-3): ")

        if pilihan == "1":
            sistem.pesan_tiket()
        elif pilihan == "2":
            sistem.tampilkan_pemesanan()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem pemesanan tiket!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-3.")

if __name__ == "__main__":
    main()
