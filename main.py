import json, requests

data = requests.get("https://www.habbo.com/api/public/groups/g-hhus-8b52498479f0703ea41ad95d6128e09c/members").json()

names = []
for item in data:
    if "name" in item:
        names.append(item["name"])

try:
    with open("names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name + "\n")
    print("names wre written to ./names.txt")
except IOError as e:
    print(f"Error writing to file: {e}")
