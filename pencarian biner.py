def pencarian_biner(arr, target):
    """Mencari elemen dalam list yang terurut dengan pencarian biner"""
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Menentukan tengah array
        if arr[mid] == target:
            return mid  # Jika ditemukan, kembalikan indeks tengah
        elif arr[mid] < target:
            low = mid + 1  # Cari di sisi kanan
        else:
            high = mid - 1  # Cari di sisi kiri
    return -1  # Jika elemen tidak ditemukan

# Input pengguna
arr = [1, 2, 3, 4, 5, 7, 8]  # List harus terurut
target = int(input("Masukkan elemen yang ingin dicari: "))

# Mencari elemen dengan pencarian biner
indeks = pencarian_biner(arr, target)

# Menampilkan hasil
if indeks != -1:
    print(f"Elemen {target} ditemukan pada indeks {indeks}.")
else:
    print(f"Elemen {target} tidak ditemukan dalam list.")
