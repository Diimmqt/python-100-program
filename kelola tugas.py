import datetime

class Tugas:
    def __init__(self, nama_tugas, tenggat_waktu, kategori="Umum"):
        self.nama_tugas = nama_tugas
        self.tenggat_waktu = tenggat_waktu
        self.kategori = kategori
        self.status = "Belum Selesai"  # Status tugas (Belum Selesai/Selesai)

    def __str__(self):
        return f"{self.nama_tugas} - {self.kategori} - Tenggat Waktu: {self.tenggat_waktu} - Status: {self.status}"

    def tandai_selesai(self):
        self.status = "Selesai"

class PengelolaTugas:
    def __init__(self):
        self.tugas_list = []  # Menyimpan daftar tugas

    def tambah_tugas(self):
        nama_tugas = input("\nMasukkan nama tugas: ")
        tanggal_input = input("Masukkan tenggat waktu tugas (format: YYYY-MM-DD HH:MM): ")
        kategori = input("Masukkan kategori tugas (misalnya: Pekerjaan, Kuliah, Pribadi): ")
        try:
            tenggat_waktu = datetime.datetime.strptime(tanggal_input, "%Y-%m-%d %H:%M")
            tugas = Tugas(nama_tugas, tenggat_waktu, kategori)
            self.tugas_list.append(tugas)
            print(f"Tugas '{nama_tugas}' berhasil ditambahkan.")
        except ValueError:
            print("Format tanggal tidak valid. Harap masukkan dengan format yang benar (YYYY-MM-DD HH:MM).")

    def tampilkan_tugas(self):
        if not self.tugas_list:
            print("\nTidak ada tugas yang ditambahkan.")
            return
        print("\nDaftar Tugas:")
        for tugas in self.tugas_list:
            print(tugas)

    def hapus_tugas(self):
        nama_tugas = input("\nMasukkan nama tugas yang ingin dihapus: ")
        for tugas in self.tugas_list:
            if tugas.nama_tugas.lower() == nama_tugas.lower():
                self.tugas_list.remove(tugas)
                print(f"Tugas '{nama_tugas}' berhasil dihapus.")
                return
        print(f"Tugas '{nama_tugas}' tidak ditemukan.")

    def tandai_selesai(self):
        nama_tugas = input("\nMasukkan nama tugas yang sudah selesai: ")
        for tugas in self.tugas_list:
            if tugas.nama_tugas.lower() == nama_tugas.lower():
                tugas.tandai_selesai()
                print(f"Tugas '{nama_tugas}' telah ditandai sebagai selesai.")
                return
        print(f"Tugas '{nama_tugas}' tidak ditemukan.")

    def tampilkan_tugas_berdasarkan_kategori(self):
        kategori = input("\nMasukkan kategori tugas yang ingin ditampilkan: ")
        tugas_ditemukan = False
        for tugas in self.tugas_list:
            if tugas.kategori.lower() == kategori.lower():
                print(tugas)
                tugas_ditemukan = True
        if not tugas_ditemukan:
            print(f"Tugas dengan kategori '{kategori}' tidak ditemukan.")

# Fungsi utama untuk menjalankan aplikasi
def main():
    pengelola_tugas = PengelolaTugas()

    while True:
        print("\nMenu Sistem Pengelolaan Tugas")
        print("1. Tambah Tugas")
        print("2. Tampilkan Daftar Tugas")
        print("3. Hapus Tugas")
        print("4. Tandai Tugas Sebagai Selesai")
        print("5. Tampilkan Tugas Berdasarkan Kategori")
        print("6. Keluar")

        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == "1":
            pengelola_tugas.tambah_tugas()
        elif pilihan == "2":
            pengelola_tugas.tampilkan_tugas()
        elif pilihan == "3":
            pengelola_tugas.hapus_tugas()
        elif pilihan == "4":
            pengelola_tugas.tandai_selesai()
        elif pilihan == "5":
            pengelola_tugas.tampilkan_tugas_berdasarkan_kategori()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan Sistem Pengelolaan Tugas!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-6.")

if __name__ == "__main__":
    main()

