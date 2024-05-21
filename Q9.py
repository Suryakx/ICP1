# Read the number of students from the user
N = int(input("Enter the number of students: "))

# Create an empty list to store the weights in lbs
weights_lbs = []

# Read the weights in lbs from the user
print("Enter the weights in pounds (lbs):")
for i in range(N):
    weight_lb = float(input(f"Weight of student {i+1}: "))
    weights_lbs.append(weight_lb)

# Convert the weights from lbs to kg
weights_kg = []
for weight_lb in weights_lbs:
    weight_kg = weight_lb * 0.453592  # 1 lb = 0.453592 kg
    weights_kg.append(weight_kg)

# Print the original weights in lbs and the converted weights in kg
print("\nOriginal weights in pounds (lbs):", weights_lbs)
print("Converted weights in kilograms (kg):", weights_kg)
