hari = input("Masukan hari: ")
kat_penonton = input("Masukan Kategori Penonton: ")
harga = 0

# if(kat_penonton == "dewasa"):
#     if(hari == "sabtu" or hari == "minggu"):
#         harga = 70000
#     elif not(hari == "sabtu" or hari == "minggu"):
#         harga = 50000
#     else:
#         print("hari tidak terdeteksi")
# elif(kat_penonton == "mahasiswa"):
#     if(hari == "sabtu" or hari == "minggu"):
#         harga = 60000
#     elif not(hari == "sabtu" or hari == "minggu"):
#         harga = 40000
#     else:
#         print("hari tidak terdeteksi")
# elif(kat_penonton == "anak-anak"):
#     if(hari == "sabtu" or hari == "minggu"):
#         harga = 40000
#     elif not(hari == "sabtu" or hari == "minggu"):
#         harga = 30000
#     else:
#         print("hari tidak terdeteksi")
# else:
#     print("kategori penonton tidak ada")


weekdays = ["senin", "selasa", "rabu", "kamis", "jumat"]
weekends = ["sabtu", "minggu"]

if hari in weekdays:
    if kat_penonton == "dewasa":
        harga = 50000
    elif kat_penonton == "mahasiswa":
        harga = 40000
    elif kat_penonton == "anak-anak":
        harga = 30000
    else:
        print("Kategori Penonton:", kat_penonton, "tidak ada")
elif hari in weekends:
    if kat_penonton == "dewasa":
        harga = 70000
    elif kat_penonton == "mahasiswa":
        harga = 60000
    elif kat_penonton == "anak-anak":
        harga = 40000
    else:
        print("Kategori Penonton:", kat_penonton, "tidak ada")
else:
    print("Hari",hari,"tidak ada dalam kalender")

if harga != 0:
    print("Hari:", hari)
    print("Harga Tiket untuk kategori:", kat_penonton, "adalah sebesar:",harga)