buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]

buah[2] = "cherry"

print(buah)

index_buah_baru = int(input("masukan index:"))
buah_baru = input("masukan nama buah:")

buah.insert(index_buah_baru, buah_baru)

print(buah)

buah.sort()

print("sorted: ", buah)