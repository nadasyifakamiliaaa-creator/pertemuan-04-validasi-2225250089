try:
    # Mengambil input dari pengguna dan mengubahnya menjadi integer
    x = int(input("Masukkan bilangan bulat: "))

    # Mengecek kondisi nilai x
    if x < 0:
        print("Bilangan negatif")
    elif x == 0:
        print("Nol")
    elif x % 2 == 0:
        print("Bilangan positif genap")
    else:
        print("Bilangan positif ganjil")

except ValueError:
    print("Input tidak valid! Harap masukkan angka bulat.")
    