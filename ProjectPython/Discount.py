nama_barang = input("Nama Barang: ")
harga_barang = int(input("Harga Barang: "))
jumlah_barang = int(input("Jumlah Barang: "))
diskon_barang = int(input("Diskon: "))

hkotor = harga_barang * jumlah_barang
hbersih = hkotor * ((100 - diskon_barang)/100)
potongan = hkotor - hbersih

print("Barang       : " + nama_barang)
print(f"Harga Kotor  : Rp {hkotor:,.0f}".replace(",", "."))
print(f"Potongan     : Rp {potongan:,.0f}".replace(",","."))
print(f"Harga Bersih : Rp {hbersih:,.0f}".replace(",","."))
