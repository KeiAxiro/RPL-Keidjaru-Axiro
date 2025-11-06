a = ("apel", "jeruk", "ceri", "durian", "apel")

print(len(a))

# range tertentu
print(a[1:4])

# Tuple itu Immutable / Fixed, tidak bisa seperti List yang bisa di ubah, di hapus, dan di tambah
# Untuk mengubah Tuple, kita perlu mengubahnya menjadi List terlebih dahulu

(a,b,c,d,e) = a

print(a)
print(b)
print(c)
print(d)
print(e)