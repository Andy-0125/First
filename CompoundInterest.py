principle = 0
rate = 0
time = 0
while True:
    principle = input("Enter the principle amount:")
    if int(principle) <= 0:
        print("Principle amount should not be less than 0.")
    else:
        break