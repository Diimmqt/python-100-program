penumpang= int (input("masukan jumlah penumpang:"))

if penumpang >= 50:
    print("anda perlu menyewa large bus")
elif penumpang >= 30:
    print("anda perlu menyewa medium bus")
elif penumpang >= 20:
    print("anda perlu menyewa minibus")
else:
    print("Gunakan kendaraan kecil atau tidak perlu kendaraan besar")
