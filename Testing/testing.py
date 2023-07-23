import json

with open("Data\\user_setting.json", 'r') as reso:
    resolutionString = json.load(reso)["Resolution"][1]

print(resolutionString)