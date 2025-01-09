import os

# Nama file tempat menyimpan data pengguna
FILENAME = "users.txt"

# Fungsi untuk registrasi pengguna baru
def registrasi():
    print("Registrasi Pengguna Baru")
    username = input("Masukkan nama pengguna: ")
    password = input("Masukkan kata sandi: ")
    
    # Cek apakah username sudah terdaftar
    if cek_username(username):
        print("Username sudah terdaftar, coba username lain.")
        return
    
    # Menyimpan data pengguna baru ke file
    with open(FILENAME, "a") as file:
        file.write(f"{username} {password}\n")
    
    print(f"Registrasi berhasil! Pengguna {username} telah terdaftar.")

# Fungsi untuk mengecek apakah username sudah terdaftar
def cek_username(username):
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            users = file.readlines()
            for user in users:
                if username == user.split()[0]:  # Cek username
                    return True
    return False

# Fungsi untuk login pengguna
def login():
    print("Login Pengguna")
    username = input("Masukkan nama pengguna: ")
    password = input("Masukkan kata sandi: ")
    
    # Memeriksa apakah username dan password cocok
    if cek_login(username, password):
        print(f"Selamat datang, {username}!")
    else:
        print("Username atau kata sandi salah.")

# Fungsi untuk mengecek apakah username dan password cocok
def cek_login(username, password):
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            users = file.readlines()
            for user in users:
                stored_username, stored_password = user.split()
                if username == stored_username and password == stored_password:
                    return True
    return False

# Menu utama
def menu():
    while True:
        print("\nMenu")
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")
        
        pilihan = input("Pilih opsi (1-3): ")
        
        if pilihan == "1":
            registrasi()
        elif pilihan == "2":
            login()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-3.")

if __name__ == "__main__":
    menu()
