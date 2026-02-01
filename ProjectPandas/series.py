import pandas as pd

print("-- Pandas --")
data = [100, 101, 102, 103, 104, 105]
series = pd.Series(data,index=["a","b","c","d","e","f"])
print(series[series <= 104])

print()

calories = {"Day 1" : 1750, "Day 2" : 2100, "Day 3" : 1700}
series2 = pd.Series(calories)
print(series2)