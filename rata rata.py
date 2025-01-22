def hitung_rata_rata(angka_list):
    """Menghitung rata-rata dari list angka."""
    if not angka_list:
        return "List kosong. Tidak dapat menghitung rata-rata."
    return sum(angka_list) / len(angka_list)

def main():
    print("=== Program Mencari Rata-Rata Angka ===")
    try:
        # Meminta input angka dari pengguna
        input_angka = input("Masukkan angka-angka, pisahkan dengan spasi: ")
        angka_list = list(map(float, input_angka.split()))

        if not angka_list:
            print("Tidak ada angka yang dimasukkan.")
            return

        # Menghitung rata-rata
        rata_rata = hitung_rata_rata(angka_list)
        print(f"Rata-rata: {rata_rata:.2f}")
    except ValueError:
        print("Masukkan hanya angka yang valid.")

if __name__ == "__main__":
    main()
