# dictionary =  a collection of {key:value} pairs
#                        ordered and changeable. No duplicates
capitals = {"China":"Beijing",
            "USA": "Washington D.C.",
            "India": "New Delhi",
            "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("China"))
# if capitals.get("Russia"):
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")
# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA": "Detroit"})
# print(capitals)
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
keys = capitals.keys()
for key in capitals.keys():
    print(key)
values = capitals.values()
for value in capitals.values():
    print(value)
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}:{value}")