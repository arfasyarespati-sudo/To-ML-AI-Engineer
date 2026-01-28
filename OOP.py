# OOP
class GPU:
    def __init__(self, driver):
        self.driver = driver

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, value):
        if not value:
            raise ValueError("Driver name cannot be empty")
        self._driver = value


gpu1 = GPU("NVIDIA GTX SERIES")
gpu2 = GPU("RADEON RX SERIES")

print(gpu1.driver)
print(gpu2.driver)





