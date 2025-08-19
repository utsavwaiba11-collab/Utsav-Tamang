# Simple Form


name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in feet: "))
country = input("Enter your country: ")


name_upper = name.upper()
country_upper = country.upper()
height_rounded = round(height, 2)
nickname = (name[:2] + name[-2:]).upper()


print(f"\nHello {name_upper}")
print(f"You are {age} years old.")
print(f"Your height is {height_rounded:.2f} feet.")
print(f"You are from {country_upper}.")
print(f"Your nickname is {nickname}")
