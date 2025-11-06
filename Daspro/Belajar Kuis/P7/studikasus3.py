# no 3

kendaraan = input("Masukan Kendaraan:")
lama_parkir = int(input("Verapa lama parkirnya:"))
tarif = 0

if (kendaraan == "motor" and lama_parkir >= 1):
    tarif += 3000
    print(tarif)
    if(lama_parkir > 1):
        tarif += lama_parkir * 2000
        print(tarif)
        if(lama_parkir >= 10):
            tarif = 20000
elif(kendaraan == "mobil" and lama_parkir >= 1):
    tarif += 5000
    print(tarif)
    if(lama_parkir > 1):
        tarif += lama_parkir * 3000
        print(tarif)
        if(lama_parkir >= 10):
            tarif == 30000