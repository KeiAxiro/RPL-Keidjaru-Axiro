# Kasus 1
nilai = [78,85,62,90,70,88,95,60,72]

jumlah_mhs = len(nilai)
avg = sum(nilai)/jumlah_mhs
nilai_max = max(nilai)
nilai_low = min(nilai)

print("ada",jumlah_mhs, "mahasiswa")
print("Rata-Rata Nilai Mahasiswa Adalah", avg)
print("Nilai Tertinggi:", nilai_max)
print("Nilai Terendah:", nilai_low)

nilai_lulus = [78,85,90,70,88,95,72]
####
print("\n")
# Kasus 2

belanja = ["beras","minyak", "kopi", "gula", "susu"]

belanja.append("teh")
belanja.remove("kopi")

print(belanja[1],"dan",belanja[len(belanja)-1])

belanja.sort()
print(belanja)

####
print("\n")

# Kasus 3
kehadiran = [1,1,0,1,1,0,1]
# hadir = []
# tidak_hadir = []

# for x in kehadiran:
#     if x == 1:
#         hadir.append(x)
#     else:
#         tidak_hadir.append(x)

# print("jumlah hadir", len(hadir))
# print("jumlah hadir", len(tidak_hadir))

# persentase_kehadiran = (len(hadir) / len(kehadiran)) * 100

# print("persentase:", persentase_kehadiran)
# if persentase_kehadiran >= 75:
#     print("Lulus")
# else:
#     print("Tidak Lulus")

print("Hadir:",kehadiran.count(1))
print("Tidak Hadir:",kehadiran.count(0))

kehadiran.pop(2)

print(kehadiran)

####
print("\n")

# Kasus 4

mahasiswa = ["Andi", "Budi", "Citra", "Dewi", "Eka"]

print(mahasiswa[2])
mahasiswa.append("Yanto")
mahasiswa.append("Yanti")

mahasiswa.remove("Budi")

mahasiswa_baru = ["Andi", "Citra", "Dewi"]

print(mahasiswa)
print(mahasiswa_baru)

#####
print("\n")

# Kasus 5

transaksi = [50000, -20000, -15000, 3000, -10000]
print("Total Saldo Akhir: ", sum(transaksi))

transaksi.append(-25000)
transaksi.sort()
print(transaksi)

