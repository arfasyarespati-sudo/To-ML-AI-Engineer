class Mobil:
    def __init__(self,warna,merk,kecepatan):
        self.warna = warna
        self.merk = merk
        self.kecepatan = kecepatan

mobil1 = Mobil("merah", "daihatsu",20)
print(mobil1.warna)
print(mobil1.merk)
print(mobil1.kecepatan)