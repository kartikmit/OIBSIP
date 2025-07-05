def bmi(w, h):
    return w / (h ** 2)

while True:
    try:
        weight = float(input("Enter your weight in Kg: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Please enter numeric values for weight and height.\n")
        continue

    if weight <= 0 or height <= 0:
        print("Weight and height must both be positive numbers.\n")
        continue

    break

result = bmi(weight, height)

if result < 18.5:
    category = "underweight"
elif result < 25:
    category = "healthy"
elif result < 30:
    category = "overweight"
else:
    category = "obese"

print(f"Your BMI is {result:.3f} and you are in the {category} category")
