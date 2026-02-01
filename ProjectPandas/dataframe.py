import pandas as pd

data = {"Name": ["Baby Dragon", "Witch", "Archer", "Barbarians", "Tesla Towers"],
        "Troop": ["Air", "Ground", "Ground", "Ground", "Ground"],
        "Attack" : ["Fire Ball", "Magic spell", "Arrows", "Sword", "Lightning Bolt"]}

df = pd.DataFrame(data)
print(df)