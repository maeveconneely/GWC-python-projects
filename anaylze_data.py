"""
Survey Project
7/9/19
"""
import json
with open('survey_data.txt', 'r') as open_file:
    contents = open_file.read()

data = json.loads(contents) # loads, s means string, so writing it to a string

age = 0
water_drinkers = 0
for i in data:
    age += int(i["age"])
    if i["water"] == "n":
        water_drinkers += 1
print("Average age of repsondents:", age/len(data))
print("Number of repsonses:", len(data))
print(water_drinkers , "person(s) didn't drink enough water.")
