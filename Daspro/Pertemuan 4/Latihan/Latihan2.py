students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}

# membuat dictionary untuk menghitung jumlah siswa per prodi
prodi_count = {}

for nama, prodi in students.items():
    if prodi in prodi_count:
        prodi_count[prodi] += 1
    else:
        prodi_count[prodi] = 1

# print hasil
for prodi, jumlah in prodi_count.items():
    print(f"prodi {prodi} sebanyak {jumlah}")