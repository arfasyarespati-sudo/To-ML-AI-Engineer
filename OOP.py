# OOP

class GPU:
    def __init__(self):

        self.driver = "NVIDIA GTX SERIES"

GraphicsCard1 = GPU()
GraphicsCard2 = GPU()

GraphicsCard2.driver = "RADEON RX SERIES"

print(GraphicsCard1.driver)
print(GraphicsCard2.driver)
print()




