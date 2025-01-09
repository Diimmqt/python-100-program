def angka_ke_kata(angka):
    # Daftar angka dalam kata
    angka_dalam_kata = {
        1: "satu",
        2: "dua",
        3: "tiga",
        4: "empat",
        5: "lima",
        6: "enam",
        7: "tujuh",
        8: "delapan",
        9: "sembilan",
        10: "sepuluh"
    }

    # Mengembalikan kata sesuai angka
    return angka_dalam_kata.get(angka, "Angka di luar jangkauan (1-10)")

# Tes fungsi
for i in range(1, 11):
    print(f"{i} -> {angka_ke_kata(i)}")
