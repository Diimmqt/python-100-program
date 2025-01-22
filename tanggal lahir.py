from datetime import datetime

def hitung_umur(tanggal_lahir):
    """Menghitung umur berdasarkan tanggal lahir."""
    hari_ini = datetime.today()
    selisih_tahun = hari_ini.year - tanggal_lahir.year
    sudah_ulang_tahun = (hari_ini.month, hari_ini.day) >= (tanggal_lahir.month, tanggal_lahir.day)
    umur = selisih_tahun if sudah_ulang_tahun else selisih_tahun - 1
    return umur

def main():
    print("=== Program Penghitung Umur ===")
    try:
        # Input tanggal lahir
        input_tanggal = input("Masukkan tanggal lahir Anda (format: YYYY-MM-DD): ")
        tanggal_lahir = datetime.strptime(input_tanggal, "%Y-%m-%d")
        
        # Menghitung umur
        umur = hitung_umur(tanggal_lahir)
        print(f"Umur Anda saat ini: {umur} tahun")
    except ValueError:
        print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")

if __name__ == "__main__":
    main()
