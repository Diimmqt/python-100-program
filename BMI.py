def hitung_bmi(berat, tinggi):
    """Menghitung BMI berdasarkan berat dan tinggi."""
    return berat / (tinggi ** 2)

def kategori_bmi(bmi):
    """Menentukan kategori BMI berdasarkan nilai BMI."""
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Berlebih"
    else:
        return "Obesitas"

def main():
    print("=== Kalkulator BMI ===")
    try:
        berat = float(input("Masukkan berat badan Anda (kg): "))
        tinggi = float(input("Masukkan tinggi badan Anda (m): "))

        if berat <= 0 or tinggi <= 0:
            print("Berat dan tinggi badan harus lebih dari 0.")
            return

        bmi = hitung_bmi(berat, tinggi)
        kategori = kategori_bmi(bmi)

        print(f"\nBMI Anda: {bmi:.2f}")
        print(f"Kategori: {kategori}")
    except ValueError:
        print("Masukkan nilai numerik yang valid untuk berat dan tinggi badan.")

if __name__ == "__main__":
    main()
