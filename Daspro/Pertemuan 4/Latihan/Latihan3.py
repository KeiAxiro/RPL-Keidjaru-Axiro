student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}

nama = input("nama siswa: ")

if nama in student_info:
    umur = student_info[nama]["age"]
    prodi = student_info[nama]["major"]
    print(f"umur {nama} adalah {umur} dan prodinya adalah {prodi}")
else:
    print(f"data untuk {nama} tidak ada.")