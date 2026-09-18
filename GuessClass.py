Class = ['Chinese', 'Math', 'English', 'Physics', 'Chemistry','Biology', 'ESS', 'Computer Science', 'Music','Psychology','Geography']
Guess = input("I'm gonna guess what class did you choose. Please tell me the capital letter of it:")
x = 0
chosen_class = [c for c in Class if c[0].upper() == Guess]
while len(chosen_class)>1:
    print(f'Is it {chosen_class[x]}?[Y/N]')
    Class_1 = str(input())
    if Class_1 == ("Y"):
        break
    elif Class_1 ==("N"):
        x +=1
        continue
print(f"I guess it's {chosen_class[x]}")

