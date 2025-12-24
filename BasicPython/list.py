#LIST PY
print("---- LIST ----")
mylist1 = ["Apel", "Mangga", "Jeruk", "Markisa", "Nangka"]
mylist2 = ["Mobil", 12, True]
print(mylist1)
print(mylist1[0])
print(len(mylist1))
print(type(mylist2))
print("----")
print(mylist1[-3:-1])
#Tambahkan item urutan berikutnya
mylist1.append("Jambu")
print(mylist1)
#Masukkan item di index
mylist1.insert(1, "Durian")
print(mylist1)
#Loopers
print("--- Loopers ---")

for x in range (len(mylist1) - 3):
    print(mylist1[x])
print("----")

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


