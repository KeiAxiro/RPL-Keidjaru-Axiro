hari_pertama = {"Andi", "Budi", "Citra", "Dewi", "Eka"}
hari_kedua = {"Budi", "Citra", "Fajar", "Gita", "Andi"}

# 1
print(hari_pertama.intersection(hari_kedua))

# 2
print(hari_pertama.symmetric_difference(hari_kedua))

# 3
print(len(hari_pertama.union(hari_kedua)))