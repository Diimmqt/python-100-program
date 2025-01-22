def tentukan_harga(harga, batas_murah, batas_mahal):
    """Menentukan apakah barang mahal atau murah berdasarkan harga."""
    if harga <= batas_murah:
        return "Murah"
    elif harga >= batas_mahal:
        return "Mahal"
    else:
        return "Harga sedang"

def main():
    print("=== Program Menentukan Barang Mahal atau Murah ===")
    try:
        harga = float(input("Masukkan harga barang (dalam IDR): "))
        batas_murah = float(input("Masukkan batas harga murah (dalam IDR): "))
        batas_mahal = float(input("Masukkan batas harga mahal (dalam IDR): "))

        if harga < 0 or batas_murah < 0 or batas_mahal < 0:
            print("Harga tidak boleh negatif.")
            return

        kategori = tentukan_harga(harga, batas_murah, batas_mahal)
        print(f"Barang dengan harga {harga} IDR dikategorikan sebagai: {kategori}")

    except ValueError:
        print("Masukkan harga yang valid.")

if __name__ == "__main__":
    main()
