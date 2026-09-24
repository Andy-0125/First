principle = 0
rate = 0
time = 0
while principle <= 0:
    principle = float(input("Please enter the principle value:"))
    if principle <= 0:
        print("Principle value should be no less than zero.")
    # else: it's not neccessary i do it wrong at the first place
while rate <= 0:
    rate = float(input("Please enter the interest rate: (%)"))
    if rate <=0:
        print("Interest rate(%)should be no less than zero")
            # else:
while time <= 0:
    time = int(input("Please enter the number of periods (yrs)"))
    if time <=0:
        print("Number of Periods should be no less than zero")

final_amount = principle * pow((1+ rate/100),time)
print(f"Balance after {time} years is ${final_amount:.2f}.")