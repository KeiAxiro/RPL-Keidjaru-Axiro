total_belanja = int(input("masukan total belanja:"))
status = input("masukan status member: ")
diskon = 0

if status == "ya":
    diskon += (total_belanja * 5)/100
elif status == "no":
    diskon = 0

if total_belanja >= 500_000:
    diskon += (total_belanja * 10)/100
elif total_belanja >= 200_000:
    diskon += (total_belanja * 5)/100

print("anda mendapatkan diskon sebesar:", diskon)
print("anda dapat potongan harga menjadi: Rp.",total_belanja-diskon)