# OOP

class GPU:
    def __init__(self):

        self.driver = "NVIDIA GTX SERIES"

GraphicsCard1 = GPU()
GraphicsCard2 = GPU()

GraphicsCard2.driver = "RADEON RX Series"

print(GraphicsCard1.driver)
print(GraphicsCard2.driver)
print()
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
mobil_1 = Mobil("Merah", "Toyota", 120)
print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

