try:
    weight = float(input("Please enter your weight:"))
except ValueError:
    print(f"Input is not valid.")
    exit()
unit = input("Kilograms or Pounds?: (K/P)")

if unit =="K":
    weight = weight * 2.205
    print(f"Your weight is round({weight},3) {unit}")
elif unit == "P":
    weight = weight / 2.205
    print(f"Your weight is round({weight},3) {unit}")
else:
    print(f"{unit} was not valid")
