import random

class TebakKata:
    def __init__(self):
        # Daftar kata yang dapat dipilih
        self.kata_kumpulan = ["python", "komputer", "programming", "algoritma", "java", "pemrograman", "database"]
        self.kata = random.choice(self.kata_kumpulan)  # Memilih kata secara acak
        self.tertebak = ["_"] * len(self.kata)  # Menyimpan huruf yang sudah ditebak
        self.coba = 0  # Menyimpan jumlah percobaan
        self.max_coba = 7  # Maksimal percobaan sebelum game berakhir

    def tebak_huruf(self, huruf):
        """Mengecek apakah huruf yang ditebak ada dalam kata"""
        if huruf in self.kata:
            # Jika huruf ada, update huruf yang sudah ditebak
            for i in range(len(self.kata)):
                if self.kata[i] == huruf:
                    self.tertebak[i] = huruf
            print(f"Tebakan benar! {''.join(self.tertebak)}")
        else:
            # Jika huruf tidak ada
            self.coba += 1
            print(f"Tebakan salah! Anda memiliki {self.max_coba - self.coba} kesempatan lagi.")
        
    def status(self):
        """Menampilkan status permainan"""
        print(f"Status: {''.join(self.tertebak)}")
        print(f"Percobaan yang tersisa: {self.max_coba - self.coba}")

    def main(self):
        """Logika permainan utama"""
        print("Selamat datang di permainan Tebak Kata!")
        print("Kata yang harus ditebak memiliki", len(self.kata), "huruf.")
        
        # Menjalankan permainan hingga selesai
        while self.coba < self.max_coba:
            self.status()
            tebakan = input("Masukkan huruf atau kata lengkap: ").lower()
            
            # Jika pemain menebak kata lengkap
            if tebakan == self.kata:
                print("Selamat! Anda berhasil menebak kata dengan benar!")
                break
            
            # Jika tebakan adalah huruf
            elif len(tebakan) == 1 and tebakan.isalpha():
                self.tebak_huruf(tebakan)
            else:
                print("Masukkan hanya satu huruf atau kata lengkap.")
            
            if "_" not in self.tertebak:
                print("Selamat! Anda berhasil menebak kata dengan benar!")
                break
        else:
            print(f"Game over! Kata yang benar adalah: {self.kata}")

if __name__ == "__main__":
    game = TebakKata()
    game.main()
