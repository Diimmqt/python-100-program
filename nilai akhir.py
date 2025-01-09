def hitung_nilai_mahasiswa():
    print("Selamat datang di Sistem Perhitungan Nilai Mahasiswa!")

    try:
        # Input nilai dari pengguna untuk setiap komponen penilaian
        nilai_ujian = float(input("Masukkan nilai ujian (0-100): "))
        nilai_tugas = float(input("Masukkan nilai tugas (0-100): "))
        nilai_kuis = float(input("Masukkan nilai kuis (0-100): "))

        # Input bobot untuk masing-masing komponen
        bobot_ujian = float(input("Masukkan bobot nilai ujian (misal: 0.4 untuk 40%): "))
        bobot_tugas = float(input("Masukkan bobot nilai tugas (misal: 0.3 untuk 30%): "))
        bobot_kuis = float(input("Masukkan bobot nilai kuis (misal: 0.3 untuk 30%): "))

        # Memeriksa apakah bobot total sama dengan 1 (100%)
        if bobot_ujian + bobot_tugas + bobot_kuis != 1:
            print("Bobot total harus sama dengan 1 (100%). Silakan coba lagi.")
            return
        
        # Menghitung nilai akhir berdasarkan bobot
        nilai_akhir = (nilai_ujian * bobot_ujian) + (nilai_tugas * bobot_tugas) + (nilai_kuis * bobot_kuis)
        
        # Menampilkan hasil
        print(f"\nNilai Akhir Mahasiswa: {nilai_akhir:.2f}")

        # Menentukan status kelulusan
        if nilai_akhir >= 60:
            print("Status: Lulus")
        else:
            print("Status: Tidak Lulus")

    except ValueError:
        print("Masukkan nilai dan bobot yang valid!")

# Menjalankan program
hitung_nilai_mahasiswa()
