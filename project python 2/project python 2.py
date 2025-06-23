import sqlite3

# Fungsi untuk membuat dan menghubungkan ke database
def connect_db():
    return sqlite3.connect('hospital.db')

# Fungsi untuk membuat tabel pasien
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER,
                        gender TEXT,
                        diagnosis TEXT,
                        admission_date TEXT)''')
    conn.commit()
    conn.close()

# Fungsi untuk menambah data pasien
def add_patient(name, age, gender, diagnosis, admission_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (name, age, gender, diagnosis, admission_date) VALUES (?, ?, ?, ?, ?)",
                   (name, age, gender, diagnosis, admission_date))
    conn.commit()
    conn.close()
    print("Pasien berhasil ditambahkan!")

# Fungsi untuk melihat daftar pasien
def view_patients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    if patients:
        print("Daftar Pasien Rumah Sakit:")
        for patient in patients:
            print(f"ID: {patient[0]} | Nama: {patient[1]} | Umur: {patient[2]} | Gender: {patient[3]} | Diagnosis: {patient[4]} | Tanggal Masuk: {patient[5]}")
    else:
        print("Tidak ada data pasien.")
    conn.close()

# Fungsi untuk mengupdate data pasien
def update_patient(patient_id, new_name, new_age, new_gender, new_diagnosis, new_admission_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE patients SET name=?, age=?, gender=?, diagnosis=?, admission_date=? WHERE id=?",
                   (new_name, new_age, new_gender, new_diagnosis, new_admission_date, patient_id))
    conn.commit()
    conn.close()
    print("Data pasien berhasil diupdate!")

# Fungsi untuk menghapus data pasien
def delete_patient(patient_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    conn.close()
    print("Pasien berhasil dihapus!")

# Menu interaktif
def main():
    create_table()  # Pastikan tabel ada

    while True:
        print("\nMenu:")
        print("1. Tambah Data Pasien")
        print("2. Lihat Daftar Pasien")
        print("3. Update Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        choice = input("Pilih opsi (1/2/3/4/5): ")

        if choice == '1':
            name = input("Masukkan nama pasien: ")
            age = int(input("Masukkan umur pasien: "))
            gender = input("Masukkan gender pasien (L/P): ")
            diagnosis = input("Masukkan diagnosis pasien: ")
            admission_date = input("Masukkan tanggal masuk (YYYY-MM-DD): ")
            add_patient(name, age, gender, diagnosis, admission_date)
        elif choice == '2':
            view_patients()
        elif choice == '3':
            patient_id = int(input("Masukkan ID pasien yang akan diupdate: "))
            new_name = input("Masukkan nama baru: ")
            new_age = int(input("Masukkan umur baru: "))
            new_gender = input("Masukkan gender baru (L/P): ")
            new_diagnosis = input("Masukkan diagnosis baru: ")
            new_admission_date = input("Masukkan tanggal masuk baru (YYYY-MM-DD): ")
            update_patient(patient_id, new_name, new_age, new_gender, new_diagnosis, new_admission_date)
        elif choice == '4':
            patient_id = int(input("Masukkan ID pasien yang akan dihapus: "))
            delete_patient(patient_id)
        elif choice == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
