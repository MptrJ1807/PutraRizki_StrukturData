class SepedaMotor:
    def __init__(self, pabrik, merk, cc, harga):
        self.pabrik = pabrik
        self.merk = merk
        self.cc = cc
        self.harga = harga

def tampilkan_data(data_motor):
    print("\nDaftar Sepeda Motor:")
    for motor in data_motor:
        print(f"{motor.pabrik} >> {motor.merk} >> {motor.cc}CC >> {motor.harga}")

def urutkan_berdasarkan_harga(data_motor, ascending=True):
    return sorted(data_motor, key=lambda x: x.harga, reverse=not ascending)

def urutkan_berdasarkan_cc(data_motor, ascending=True):
    return sorted(data_motor, key=lambda x: x.cc, reverse=not ascending)

def main():
    data_motor = []

    # Input data motor
    jumlah_motor = int(input("Masukkan jumlah sepeda motor: "))
    for _ in range(jumlah_motor):
        pabrik = input("Masukkan pabrik: ")
        merk = input("Masukkan merk: ")
        cc = input("Masukkan CC: ")
        harga = int(input("Masukkan harga: "))
        
        motor = SepedaMotor(pabrik, merk, cc, harga)
        data_motor.append(motor)

    # Tampilkan data sepeda motor sebelum diurutkan
    tampilkan_data(data_motor)

    # Urutkan berdasarkan harga secara ascending
    data_motor_harga_asc = urutkan_berdasarkan_harga(data_motor, True)
    print("\nHasil Sorting berdasarkan Harga (Ascending):")
    tampilkan_data(data_motor_harga_asc)

    # Urutkan berdasarkan harga secara descending
    data_motor_harga_desc = urutkan_berdasarkan_harga(data_motor, False)
    print("\nHasil Sorting berdasarkan Harga (Descending):")
    tampilkan_data(data_motor_harga_desc)

    # Urutkan berdasarkan CC secara ascending
    data_motor_cc_asc = urutkan_berdasarkan_cc(data_motor, True)
    print("\nHasil Sorting berdasarkan CC (Ascending):")
    tampilkan_data(data_motor_cc_asc)

    # Urutkan berdasarkan CC secara descending
    data_motor_cc_desc = urutkan_berdasarkan_cc(data_motor, False)
    print("\nHasil Sorting berdasarkan CC (Descending):")
    tampilkan_data(data_motor_cc_desc)

if __name__ == "__main__":
    main()
