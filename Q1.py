ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(f"Sorted list: {ages}")
min_age = ages[0]
max_age = ages[-1]
print(f"Minimum age: {min_age}")
print(f"Maximum age: {max_age}")

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(f"List with min and max added: {ages}")

# Find the median age (one middle item or two middle items divided by two)
ages.sort()  # Sort again after adding min and max
n = len(ages)
if n % 2 == 0:
    # Even number of elements, take the middle two and divide by 2
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    # Odd number of elements, take the middle element
    median = ages[n // 2]
print(f"Median age: {median}")

# Find the average age (sum of all items divided by their number)
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")

# Find the range of the ages (max minus min)
age_range = max_age - min_age
print(f"Range of ages: {age_range}")
