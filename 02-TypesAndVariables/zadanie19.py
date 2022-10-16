# BMI Calculator Enter your height in cm: ...
# Enter your weight in kg: ...
# BMI index: ...

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# BMI = round(weight / height**2, 4)
BMI = weight / height**2

print("BMI index:", BMI)
