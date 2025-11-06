kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "lucu": True,
    "hobi": ["makan","tidur"]
}

# print(kucing)

# print(len(kucing))

# buat dengan method
buah = dict(nama = "Apel", warna = "Merah", manis = True)
print(buah)

print(kucing.keys())
print(kucing.values())

kucing["nama"] = "Takuro"

print(kucing["nama"])