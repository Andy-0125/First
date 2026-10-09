
weight = float(input("Please enter your weight:"))

unit = float(input("Kilograms or Pounds?: (K/P)"))

if unit =="K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is round({weight},3) {unit}")
elif unit == "P":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is round({weight},3) {unit}")
else:
    print(f"{unit} was not valid")
