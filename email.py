import re

def validasi_email(email):
    """Fungsi untuk memvalidasi alamat email"""
    # Pola regex untuk alamat email yang valid
    pola = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Cek apakah email sesuai dengan pola
    if re.match(pola, email):
        return True
    else:
        return False

# Input dari pengguna
email = input("Masukkan alamat email: ")

# Validasi email
if validasi_email(email):
    print(f"'{email}' adalah alamat email yang valid.")
else:
    print(f"'{email}' bukan alamat email yang valid.")
