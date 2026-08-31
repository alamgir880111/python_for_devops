info = {
    "Name" : "Alamgir",
    "Address" : "Kazipara",
    "Age" : 42,
    "Favourit" : ["movies", "play"]
}

info.update({"company" : "al-khaleej"})

# print("I live in", info["Address"])

print("I live in", info.get("address", "Not found"))

print(info)

for key,value in info.items():
    print(key,value)