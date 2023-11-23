# Fungsi untuk membandingkan dua mahasiswa berdasarkan NIM
def compare_nim(mahasiswa):
    return mahasiswa['nim']

# Input jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Membuat list untuk menyimpan informasi mahasiswa
mahasiswas = []

# Input informasi mahasiswa
for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i + 1}:")
    
    # Input NIM (empat digit terakhir)
    nim = input("NIM (empat digit terakhir): ")
    
    # Input nama
    nama = input("Nama: ")
    
    # Input fakultas
    fakultas = input("Fakultas: ")

    # Menambahkan informasi mahasiswa ke dalam list
    mahasiswa = {'nim': nim, 'nama': nama, 'fakultas': fakultas}
    mahasiswas.append(mahasiswa)

# Melakukan sorting berdasarkan NIM
mahasiswas.sort(key=compare_nim)

# Menampilkan hasil sorting
print("\nHasil Sorting berdasarkan NIM:")
for mahasiswa in mahasiswas:
    print(f"NIM: {mahasiswa['nim']}\nNama: {mahasiswa['nama']}\nFakultas: {mahasiswa['fakultas']}\n================================================================")
