import random

# Fungsi utama permainan slot
def main():
    print("🎰 Selamat datang di Permainan Slot ")
    balance = int (input('masukan saldo anda:'))

    while True:
        print(f"\nSaldo Anda saat ini: {balance}")
        bet = int(input("Masukkan jumlah taruhan (atau ketik 0 untuk keluar): "))

        if bet == 0:
            print("Terima kasih telah bermain. Sampai jumpa!")
            break
        elif bet > balance:
            print("❌ Taruhan Anda melebihi saldo. Coba lagi.")
            continue
        elif bet <= 0:
            print("❌ Masukkan jumlah taruhan yang valid.")
            continue

        # Mesin slot (3 simbol acak)
        symbols = ["🍒", "🍋", "🍉", "⭐", "💎", "7️⃣"]
        result = [random.choice(symbols) for _ in range(3)]
        print("🎲 Hasil slot:", " | ".join(result))

        # Aturan kemenangan
        if result[0] == result[1] == result[2]:  # Tiga simbol sama
            print(" JACKPOT! Anda menang 10x taruhan! ")
            balance += bet * 10
        elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:  # Dua simbol sama
            print(" Selamat! Anda menang 2x taruhan!")
            balance += bet * 2
        else:
            print(" Anda kalah. Coba lagi!")
            balance -= bet

        # Periksa saldo pemain
        if balance <= 0:
            print("💸 Saldo Anda habis. Permainan selesai!")
            break

if __name__ == "__main__":
    main()
