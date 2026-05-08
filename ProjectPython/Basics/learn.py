#Data Types
a = "super"
print(type(a))
#Multiple Variables & Prints
x, y, z = "Orange", "Apple", "Mango"
print(x,y,z)
print()
print('Hello', 'World')
#Index String Array & Length
p = "Di Sebuah Kota"
print(p[0])
print(len(p))
#Slicing
print(p[3:9])
print(p[:9])
print(p[3:])
#UpperLowerCases
print(p.upper())
print(p.lower())
#Strips
x = "  fein fein fein  "
print("Before")
print("-" + x + "-")
print("After")
print("-" + x.strip() + "-")

num1 = int(input("Masukkan angka pertama: "))
num2 = int(input("Masukkan angka kedua: "))

calc1 = num1 ** num2 #ex : 12^5
calc2 = num1 // num2 #ex : 12/5 = 2 (sisa dibulatkan)
print(calc1)
print(calc2)





