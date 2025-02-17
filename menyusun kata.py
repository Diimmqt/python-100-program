import itertools

def susun_kata():
    huruf = input("Masukkan huruf yang akan disusun: ").strip()
    
    # Menyusun semua kombinasi huruf yang dapat dibentuk
    kombinasi_kata = itertools.permutations(huruf)
    
    # Menampilkan semua kata yang dapat disusun
    print("\nKata-kata yang dapat disusun dari huruf tersebut:")
    for kata in kombinasi_kata:
        print("".join(kata))

# Jalankan program
susun_kata()
