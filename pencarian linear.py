def pencarian_linier(arr, target):
    """Mencari elemen dalam list dengan pencarian linier"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Kembalikan indeks elemen yang ditemukan
    return -1  # Jika elemen tidak ditemukan

# Input pengguna
arr = [5, 3, 7, 2, 8, 1, 4]
target = int(input("Masukkan elemen yang ingin dicari: "))

# Mencari elemen dengan pencarian linier
indeks = pencarian_linier(arr, target)

# Menampilkan hasil
if indeks != -1:
    print(f"Elemen {target} ditemukan pada indeks {indeks}.")
else:
    print(f"Elemen {target} tidak ditemukan dalam list.")
