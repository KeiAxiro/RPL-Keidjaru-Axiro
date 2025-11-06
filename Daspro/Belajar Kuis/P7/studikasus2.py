# 2
umur= 22
gender="pria"
tinggi=177
iq = 144

if(umur >= 18 and umur < 25):
    print("umur masuk ketentuan")
    if(iq >= 130):
        print("iq lolos ketentuan")
        if(gender == "pria" and tinggi >= 175):
            print("Tinggi Badan Lolos")
        elif(gender == "wanita" and tinggi >= 170):
            print("Tinggi Badan Lolos")
        else:
            print("tinggi badan tidak lolos")
    else:
        print("iq kurang")
else:
    print("umur tidak masuk ketentuan")
