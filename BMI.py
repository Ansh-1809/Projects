# Ask the user for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Show the result
print(f"Your BMI is:{bmi:.2f}")

# Interpret the BMI
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25.4:
  print("You have a normal weight.")
elif bmi < 30:
  print("You are overweight.")
else:
  print("You are obese.")
