def tentukan_zodiak(hari, bulan):
    """Menentukan zodiak berdasarkan hari dan bulan."""
    if (bulan == 1 and hari >= 20) or (bulan == 2 and hari <= 18):
        return "Aquarius"
    elif (bulan == 2 and hari >= 19) or (bulan == 3 and hari <= 20):
        return "Pisces"
    elif (bulan == 3 and hari >= 21) or (bulan == 4 and hari <= 19):
        return "Aries"
    elif (bulan == 4 and hari >= 20) or (bulan == 5 and hari <= 20):
        return "Taurus"
    elif (bulan == 5 and hari >= 21) or (bulan == 6 and hari <= 20):
        return "Gemini"
    elif (bulan == 6 and hari >= 21) or (bulan == 7 and hari <= 22):
        return "Cancer"
    elif (bulan == 7 and hari >= 23) or (bulan == 8 and hari <= 22):
        return "Leo"
    elif (bulan == 8 and hari >= 23) or (bulan == 9 and hari <= 22):
        return "Virgo"
    elif (bulan == 9 and hari >= 23) or (bulan == 10 and hari <= 22):
        return "Libra"
    elif (bulan == 10 and hari >= 23) or (bulan == 11 and hari <= 21):
        return "Scorpio"
    elif (bulan == 11 and hari >= 22) or (bulan == 12 and hari <= 21):
        return "Sagittarius"
    elif (bulan == 12 and hari >= 22) or (bulan == 1 and hari <= 19):
        return "Capricorn"
    else:
        return "Tanggal tidak valid."

def main():
    print("=== Program Menentukan Zodiak ===")
    try:
        hari = int(input("Masukkan hari lahir (1-31): "))
        bulan = int(input("Masukkan bulan lahir (1-12): "))

        if 1 <= bulan <= 12 and 1 <= hari <= 31:
            zodiak = tentukan_zodiak(hari, bulan)
            print(f"Zodiak Anda adalah: {zodiak}")
        else:
            print("Hari atau bulan yang dimasukkan tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()

print("notes:jangan percaya sama zodiac,its just program hehe")