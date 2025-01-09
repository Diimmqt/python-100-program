import datetime
import time

class Tugas:
    def __init__(self, nama_tugas, tenggat_waktu):
        self.nama_tugas = nama_tugas
        self.tenggat_waktu = tenggat_waktu
        self.diperiksa = False  # Menandakan apakah tugas sudah diproses

    def __str__(self):
        return f"{self.nama_tugas} - Tenggat Waktu: {self.tenggat_waktu}"

class PengingatTugas:
    def __init__(self):
        self.tugas_list = []  # Menyimpan semua tugas

    def tambah_tugas(self):
        nama_tugas = input("\nMasukkan nama tugas: ")
        tanggal_input = input("Masukkan tenggat waktu tugas (format: YYYY-MM-DD HH:MM): ")
        try:
            tenggat_waktu = datetime.datetime.strptime(tanggal_input, "%Y-%m-%d %H:%M")
            tugas = Tugas(nama_tugas, tenggat_waktu)
            self.tugas_list.append(tugas)
            print(f"Tugas '{nama_tugas}' berhasil ditambahkan dengan tenggat waktu {tenggat_waktu}.")
        except ValueError:
            print("Format tanggal tidak valid. Harap masukkan dengan format yang benar (YYYY-MM-DD HH:MM).")

    def tampilkan_tugas(self):
        if not self.tugas_list:
            print("\nTidak ada tugas yang ditambahkan.")
            return
        print("\nDaftar Tugas:")
        for tugas in self.tugas_list:
            print(tugas)

    def cek_tugas(self):
        saat_ini = datetime.datetime.now()
        for tugas in self.tugas_list:
            if not tugas.diperiksa and tugas.tenggat_waktu <= saat_ini:
                print(f"\nTugas yang sudah waktunya: {tugas}")
                tugas.diperiksa = True  # Tandai tugas sudah diperiksa

    def hapus_tugas(self):
        nama_tugas = input("\nMasukkan nama tugas yang ingin dihapus: ")
        for tugas in self.tugas_list:
            if tugas.nama_tugas.lower() == nama_tugas.lower():
                self.tugas_list.remove(tugas)
                print(f"Tugas '{nama_tugas}' berhasil dihapus.")
                return
        print(f"Tugas '{nama_tugas}' tidak ditemukan.")

# Fungsi utama untuk menjalankan aplikasi
def main():
    pengingat = PengingatTugas()

    while True:
        print("\nMenu Aplikasi Pengingat Tugas")
        print("1. Tambah Tugas")
        print("2. Tampilkan Daftar Tugas")
        print("3. Cek Tugas yang Mendekati Tenggat Waktu")
        print("4. Hapus Tugas")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            pengingat.tambah_tugas()
        elif pilihan == "2":
            pengingat.tampilkan_tugas()
        elif pilihan == "3":
            pengingat.cek_tugas()
        elif pilihan == "4":
            pengingat.hapus_tugas()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan Aplikasi Pengingat Tugas!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")

if __name__ == "__main__":
    main()
