def cari_huruf_vokal(teks):
    """Mengembalikan huruf vokal dalam teks."""
    vokal = "aiueoAIUEO"
    hasil = [huruf for huruf in teks if huruf in vokal]
    return hasil

def main():
    print("=== Program Menampilkan Huruf Vokal ===")
    teks = input("Masukkan sebuah teks: ")
    
    # Mencari huruf vokal
    huruf_vokal = cari_huruf_vokal(teks)
    
    if huruf_vokal:
        print(f"Huruf vokal dalam teks: {' '.join(huruf_vokal)}")
    else:
        print("Tidak ada huruf vokal dalam teks.")

if __name__ == "__main__":
    main()
