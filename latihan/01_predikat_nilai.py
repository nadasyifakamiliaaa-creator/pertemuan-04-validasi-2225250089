nilai = float(input("Nilai akhir (0-100): "))

if 0 <= nilai <= 100:
    if nilai >= 85:
        predikat = "A"
    elif nilai >= 70:
        predikat = "B"
    elif nilai >= 60:
        predikat = "C"
    elif nilai >= 50:
        predikat = "D"
    else:
        predikat = "E"
    print(f"Nilai {nilai:.2f} memperoleh predikat {predikat}.")
else:
    print("Nilai harus antara 0 dan 100.")
