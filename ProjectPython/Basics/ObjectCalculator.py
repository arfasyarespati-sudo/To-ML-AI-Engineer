class Kalkulator:
    def __init__(self):
        """Inisialisasi (Constructor)"""
        pass

    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    def bagi(self, a, b):
        if b == 0:
            return "Error: Tidak bisa membagi dengan nol!"
        return a / b


my_calc = Kalkulator()


angka1 = 10
angka2 = 5

print(f"Hasil Tambah: {my_calc.tambah(angka1, angka2)}")
print(f"Hasil Kurang: {my_calc.kurang(angka1, angka2)}")
print(f"Hasil Kali  : {my_calc.kali(angka1, angka2)}")
print(f"Hasil Bagi  : {my_calc.bagi(angka1, angka2)}")