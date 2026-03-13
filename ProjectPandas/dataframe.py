import pandas as pd

data = {"Name": ["Baby Dragon", "Witch", "Archer", "Barbarians", "Tesla Towers"],
        "Troop": ["Air", "Ground", "Ground", "Ground", "Ground"],
        "Attack" : ["Fire Ball", "Magic spell", "Arrows", "Sword", "Lightning Bolt"]}

df = pd.DataFrame(data, index=["Troop 1", "Troop 2", "Troop 3", "Troop 4", "Tower"])
row = pd.DataFrame([{"Name": "Archer Queen", "Troop" : "Ground", "Attack" : "Volley Arrows"}, 
                    {"Name" : "Hero Giant", "Troop" : "Ground", "Attack" : "Fist"}], 
                   index=["Champion", "Hero"])

df = pd.concat([df, row])
df["Rarity"] = ["Epic", "Epic", "Common", "Common", "Common", "Champion", "Hero"]
print(df)