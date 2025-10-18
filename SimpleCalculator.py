print("Selamat datang di Kalkulator!!")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("Pilih sesuai angka 1 - 4")

pilihan = int(input("Masukkan pilihan: "))
if pilihan < 1 or pilihan > 4:
    print("Angka tidak valid")
    exit()
    
angka_1 = int(input("Angka pertama: "))
angka_2 = int(input("Angka kedua: "))

if pilihan == 1:
    hasil = angka_1 + angka_2
    
elif pilihan == 2:
    hasil = angka_1 - angka_2
    
elif pilihan == 3:
    hasil = angka_1 * angka_2
    
elif pilihan == 4:
    hasil = angka_1 / angka_2
    
print(hasil)

