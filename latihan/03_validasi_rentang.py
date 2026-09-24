try:
    # Mengambil input angka (desimal/bulat) dari pengguna
    sudut = float(input("Besar sudut dalam derajat: "))

    # Validasi dan penentuan jenis sudut
    if sudut <= 0 or sudut >= 180:
        print("Masukan ditolak: sudut harus lebih dari 0 dan kurang dari 180.")
    elif sudut < 90:
        print("Sudut lancip")
    elif sudut == 90:
        print("Sudut siku-siku")
    else:
        print("Sudut tumpul")

except ValueError:
    print("Input tidak valid! Harap masukkan angka yang sesuai.")
    