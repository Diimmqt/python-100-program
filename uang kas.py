class UangKas:
    def __init__(self):
        self.saldo = 0  # Saldo awal kas
        self.history = []  # Riwayat transaksi

    def tampilkan_saldo(self):
        print(f"\nSaldo Uang Kas Saat Ini: Rp {self.saldo}")

    def tambah_pemasukan(self):
        try:
            pemasukan = float(input("Masukkan jumlah pemasukan: Rp "))
            if pemasukan <= 0:
                print("Jumlah pemasukan harus lebih dari 0.")
                return
            self.saldo += pemasukan
            self.history.append(f"Pemasukan: Rp {pemasukan}")
            print(f"Pemasukan sebesar Rp {pemasukan} berhasil ditambahkan.")
        except ValueError:
            print("Masukkan jumlah yang valid.")

    def tambah_pengeluaran(self):
        try:
            pengeluaran = float(input("Masukkan jumlah pengeluaran: Rp "))
            if pengeluaran <= 0:
                print("Jumlah pengeluaran harus lebih dari 0.")
                return
            if pengeluaran > self.saldo:
                print("Pengeluaran melebihi saldo kas.")
                return
            self.saldo -= pengeluaran
            self.history.append(f"Pengeluaran: Rp {pengeluaran}")
            print(f"Pengeluaran sebesar Rp {pengeluaran} berhasil dikurangkan.")
        except ValueError:
            print("Masukkan jumlah yang valid.")

    def tampilkan_riwayat(self):
        if not self.history:
            print("Belum ada transaksi.")
            return
        print("\nRiwayat Transaksi:")
        for transaksi in self.history:
            print(f"- {transaksi}")

# Fungsi utama untuk menjalankan program
def main():
    kas = UangKas()

    while True:
        print("\nMenu Pengelolaan Uang Kas")
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Tampilkan Saldo Kas")
        print("4. Tampilkan Riwayat Transaksi")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            kas.tambah_pemasukan()
        elif pilihan == "2":
            kas.tambah_pengeluaran()
        elif pilihan == "3":
            kas.tampilkan_saldo()
        elif pilihan == "4":
            kas.tampilkan_riwayat()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem pengelolaan uang kas!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")

if __name__ == "__main__":
    main()
