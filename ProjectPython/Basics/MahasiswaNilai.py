jumlah = int(input("Masukkan Jumlah Mahasiswa: "))
lists = []
for i in range(jumlah):
    list = float(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
    lists.append(list)

print(f"Daftar Nilai: {lists}")

total = 0
nilaimax = lists[0]
lulus = 0

for i in lists:
    total += i
    if i > nilaimax:
        nilaimax = i
    if i >= 75:
        lulus += 1


print("====================================")
print(f"Rata-rata Nilai        : {total / jumlah}")
print(f"Nilai Tertinggi        : {nilaimax}")
print(f"Jumlah mahasiswa lulus : {lulus}")
print(f"Presentase kelulusan   : {(lulus/jumlah)*100}%")
print("=====================================")