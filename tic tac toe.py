def tampilkan_papan(papan):
    """Menampilkan papan permainan Tic-Tac-Toe"""
    for baris in papan:
        print(" | ".join(baris))
        print("-" * 5)

def cek_kemenangan(papan, pemain):
    """Mengecek apakah pemain tertentu menang"""
    # Mengecek baris, kolom, dan diagonal
    for i in range(3):
        if all([kotak == pemain for kotak in papan[i]]):  # Baris
            return True
        if all([papan[j][i] == pemain for j in range(3)]):  # Kolom
            return True

    # Mengecek diagonal
    if papan[0][0] == pemain and papan[1][1] == pemain and papan[2][2] == pemain:
        return True
    if papan[0][2] == pemain and papan[1][1] == pemain and papan[2][0] == pemain:
        return True

    return False

def cek_seri(papan):
    """Mengecek apakah permainan berakhir seri"""
    for baris in papan:
        if "_" in baris:  # Jika masih ada kotak kosong
            return False
    return True

def permainan_tic_tac_toe():
    """Logika utama permainan Tic-Tac-Toe"""
    papan = [["_" for _ in range(3)] for _ in range(3)]  # Inisialisasi papan kosong
    pemain = "X"  # Pemain pertama adalah X
    giliran = 0  # Melacak giliran pemain (0 untuk X, 1 untuk O)

    print("Permainan Tic-Tac-Toe")
    tampilkan_papan(papan)

    while True:
        # Meminta input dari pemain untuk memilih posisi
        baris = int(input(f"Pemain {pemain}, masukkan nomor baris (0, 1, 2): "))
        kolom = int(input(f"Pemain {pemain}, masukkan nomor kolom (0, 1, 2): "))

        # Memeriksa apakah posisi valid (belum diisi)
        if papan[baris][kolom] != "_":
            print("Posisi sudah diisi, coba lagi!")
            continue

        # Menempatkan tanda pemain di posisi yang dipilih
        papan[baris][kolom] = pemain

        # Menampilkan papan setelah langkah pemain
        tampilkan_papan(papan)

        # Mengecek apakah pemain saat ini menang
        if cek_kemenangan(papan, pemain):
            print(f"Pemain {pemain} menang!")
            break

        # Mengecek apakah permainan berakhir seri
        if cek_seri(papan):
            print("Permainan berakhir seri!")
            break

        # Bergiliran pemain
        pemain = "O" if pemain == "X" else "X"

# Menjalankan permainan
permainan_tic_tac_toe()
