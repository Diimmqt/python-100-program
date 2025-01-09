import random

print("Permainan Tebak Angka")
angka_rahasia = random.randint(1, 10)

for i in range(3):  # Kamu punya 3 kesempatan
    tebakan = int(input("Tebak angka antara 1 dan 10: "))
    if tebakan == angka_rahasia:
        print("Selamat! Tebakanmu benar.")
        break
    elif tebakan < angka_rahasia:
        print("Terlalu rendah!")
    else:
        print("Terlalu tinggi!")

if tebakan != angka_rahasia:
    print(f"Maaf, kamu kalah. Angka rahasianya adalah {angka_rahasia}.")