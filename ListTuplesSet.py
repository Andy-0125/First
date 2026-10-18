# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER
fruits = ["apple", "coconut", "orange", "banana"]
fruits = {"apple", "coconut", "orange", "banana"}
fruits = ("apple", "coconut", "orange", "banana")
fruits.pop()
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple"in fruits)
# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
print(fruits.count("banana"))

for fruit in fruits:
    print(fruit)

