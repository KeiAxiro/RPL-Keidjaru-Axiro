# orang = {"yanto", "yanti", "otnay", "agung"}
# #  Set bersifat random, atau berubah ubah (unordered), dan immutable tidak bisa di manipulasi datanya
# print(orang)
# print(len(orang))

# a = {"apel", 20, True, "durian", 12.2}

# # Set tidak ada indexnya jadinya harus di looping
# print("\n")
# for x in a:
#     print(x)

# print("\n")

# print("apel" in a)
# print("yahaha" in a)

# # tapi bisa ditambah dan dihapus

# # tambah item

# a.add("semangka")
# print(a)

# print("\n")# tambah item di set dari set lainya

# b = {"apel", "wiw"}

# a.update(b)

# print(a)

# print("\n")# mengabungkan dua Set dan memasukanya ke variabel baru

# c = a.union(b)

# print(a)
# print(b)
# print(c)

# interception = cari item yang sama dari set

# a = {"apel", "jeruk", "ceri", "durian"}
# b = {"strawberry", "blueberry", "apel", "jeruk"}

# a.intersection_update(b)

# print(a) # {'jeruk', 'apel'}

# print(a.intersection(b)) # {'jeruk', 'apel'}


# Symmetric_diffrenet = cari item yang beda dari set

# a = {"apel", "jeruk", "ceri", "durian"}
# b = {"strawberry", "blueberry", "apel", "jeruk"}

# a.symmetric_difference_update(b) 

# print(a) # {'ceri', 'blueberry', 'durian', 'strawberry'}

# a = {"apel", "jeruk", "ceri", "durian"}
# b = {"strawberry", "blueberry", "apel", "jeruk"}

# c = a.symmetric_difference(b)


# bisa tambah List dan Tuple ke dalam Set:

a = {"apel", "jeruk", "ceri", "durian"} # Set
b = ["strawberry", "blueberry"] # List
c = ("pisang", "mangga") # Tuple

a.update(b)
a.update(c)
print(a) # {'apel', 'mangga', 'strawberry', 'pisang', 'durian', 'blueberry', 'jeruk', 'ceri'}

