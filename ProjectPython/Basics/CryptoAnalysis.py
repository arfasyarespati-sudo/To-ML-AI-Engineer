periode = int(input("Masukkan periode hari: "))

kumpulHari = []
total = rata = naik = turun = lonjakan = 0


for i in range(periode):
    hari = float(input(f"Harga penutupan hari {i+1}: "))
    kumpulHari.append(hari)

print(f"Riwayat harga: {kumpulHari}")

for i in kumpulHari:
    total += i

rata += total / len(kumpulHari)

print(f"Harga Rata-rata: {rata}")

awal = kumpulHari[0]
for i in kumpulHari: #ex: 100 200 50
    if awal > i:
        naik += 1
    elif awal < i:
        turun += 1
    else:
        naik += 0


print(f"Hari mengalami kenaikan: {naik}")
print(f"Hari mengalami penurunan: {turun}")

for i in range (1, len(kumpulHari)):
    selisih = kumpulHari[i] - kumpulHari[i-1]
    if selisih > 0:
        lonjakan += selisih


print(f"Lonjakan harian tertinggi: +{lonjakan}")

