def estimasi_perjalanan(jarak, kecepatan):
    """Menghitung estimasi waktu perjalanan dalam jam dan menit."""
    if kecepatan <= 0:
        return "Kecepatan harus lebih besar dari 0."
    waktu_jam = jarak / kecepatan  # Waktu dalam jam
    jam = int(waktu_jam)
    menit = int((waktu_jam - jam) * 60)
    return jam, menit

def main():
    print("=== Program Estimasi Perjalanan ===")
    try:
        jarak = float(input("Masukkan jarak tujuan (dalam kilometer): "))
        kecepatan = float(input("Masukkan kecepatan rata-rata kendaraan (dalam km/jam): "))
        
        if jarak < 0 or kecepatan < 0:
            print("Jarak dan kecepatan tidak boleh negatif.")
            return
        
        jam, menit = estimasi_perjalanan(jarak, kecepatan)
        print(f"Estimasi waktu perjalanan: {jam} jam {menit} menit")
        
    except ValueError:
        print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()
