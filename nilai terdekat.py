def cari_nilai_terdekat(data, target):
    """Menemukan angka dalam list yang paling dekat dengan nilai target."""
    return min(data, key=lambda x: abs(x - target))

def main():
    print("=== Program Mencari Nilai Terdekat dalam List ===")
    
    try:
        # Input list angka
        data = list(map(float, input("Masukkan daftar angka (pisahkan dengan spasi): ").split()))
        target = float(input("Masukkan angka target: "))

        if not data:
            print("List tidak boleh kosong.")
            return

        # Cari nilai terdekat
        nilai_terdekat = cari_nilai_terdekat(data, target)
        print(f"Angka dalam list yang paling dekat dengan {target} adalah {nilai_terdekat}")

    except ValueError:
        print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()
