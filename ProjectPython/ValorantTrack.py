kills = []
pertandingan = int(input("Masukkan Jumlah Pertandingan: "))
for i in range(pertandingan):
    kill = int(input(f"Masukkan Jumlah kill match ke-{i+1}: "))
    kills.append(kill)

print(f"Riwayat Kill: {kills}")

total = 0
rata = 0
best = kills[0]
mvp = 0

for i in kills:
    total += i

print(f"Total Kill           : {total}")

for i in kills:
    rata += i / len(kills)

print(f"Rata-rata Kill       : {rata}")

for i in kills:  #ex: 10,20,30
    if i > best: #jika 10 > 10.  jika 20 > 10.  jika 30 > 20.
       best = i  #best = 1.      best = 20.     best = 30.(max)

print(f"Kill Tertinggi       : {best}")

for i in kills:
    if i >= 20:
        mvp += 1

print(f"MVP (20 kills keatas): {mvp}")