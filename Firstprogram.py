num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))

num1 = int(num1)
num2 = int(num2)

print("\n--- Simple Calculation Results \n")
print("sum", num1 + num2)
print("multiplication", num1 * num2)
print("division", num1 / num2)
print("modulo", num1 % num2)
print("power",num1 ** num2)

print("---\n Simple Form")



      
name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in feet: "))
country = input("Enter your country: ")

# Processing
name_upper = name.upper()
country_upper = country.upper()
nickname = (name[:2] + name[-2:]).upper()
height_rounded = round(height, 2)