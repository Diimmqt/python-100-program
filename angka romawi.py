def desimal_ke_romawi(angka):
    """Mengonversi angka desimal menjadi angka Romawi."""
    if not (1 <= angka <= 3999):
        return "Angka harus antara 1 dan 3999."
    
    romawi_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    
    hasil = ""
    for nilai, simbol in romawi_map:
        while angka >= nilai:
            hasil += simbol
            angka -= nilai
    return hasil

def main():
    print("=== Program Konversi Angka Desimal ke Romawi ===")
    try:
        angka = int(input("Masukkan angka desimal (1-3999): "))
        romawi = desimal_ke_romawi(angka)
        print(f"Angka {angka} dalam angka Romawi adalah: {romawi}")
    except ValueError:
        print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()
