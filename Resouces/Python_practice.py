from dataclasses import dataclass


print("Hello World")
print(5+2*3)
print(8//5-3)
print(8+22*2-4)
print(16-3/(2+7)-1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)
print((5+2)*3)
print((8//5)-3)
print(8+(22*(2-4)))
print(16-3/(2+7)-1)
print(3**(3%5))
print(5+(9*3/2-4))
print(5+(9*3/(2-4)))
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict["El Paso"] = 461149
counties_dict
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
counties_dict["Arapahoe"]
counties_dict.get("Jefferson")
voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})
voting_data.append({"county": "El Paso", "registered_voters": 461149})
voting_data
voting_data.remove({"county": "Arapahoe", "registered_voters": 422829})
voting_data
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
  print(counties[1])
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
x = 0
while x <= 5:
    print(x)
    x = x + 1


