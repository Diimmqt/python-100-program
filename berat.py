def masukkan_barang():
    """Memasukkan barang dan beratnya."""
    daftar_barang = []
    print("Masukkan data barang (nama dan berat). Ketik 'selesai' untuk berhenti.")
    while True:
        nama = input("Nama barang: ")
        if nama.lower() == "selesai":
            break
        try:
            berat = float(input(f"Berat {nama} (dalam kg): "))
            daftar_barang.append((nama, berat))
        except ValueError:
            print("Berat harus berupa angka. Silakan coba lagi.")
    return daftar_barang

def sortir_barang_berdasarkan_berat(daftar_barang):
    """Mensortir daftar barang berdasarkan beratnya."""
    return sorted(daftar_barang, key=lambda x: x[1])

def tampilkan_barang(daftar_barang):
    """Menampilkan daftar barang yang telah diurutkan."""
    print("\nDaftar Barang Setelah Disortir (berat dari teringan ke terberat):")
    for nama, berat in daftar_barang:
        print(f"- {nama}: {berat} kg")

def main():
    print("=== Program Mensortir Barang Berdasarkan Berat ===")
    daftar_barang = masukkan_barang()
    if not daftar_barang:
        print("Tidak ada barang yang dimasukkan.")
        return
    daftar_barang_terurut = sortir_barang_berdasarkan_berat(daftar_barang)
    tampilkan_barang(daftar_barang_terurut)

if __name__ == "__main__":
    main()
