print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

x = int(input("Pilih proses aritmatika: ")) 
i = float(input("Masukkan angka pertama: "))
j = float(input("Masukkan angka pertama: "))

if x == 1:
    print(i + j)
elif x == 2:
    print(i - j)
elif x == 3:
    print(i * j)
elif x == 4:
    print(i / j)
else:
    print("Illegal Number")

