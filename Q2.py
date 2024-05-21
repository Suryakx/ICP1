# Question 2.1 - Create an empty dictionary called dog
dog = {}

# Question 2.2 - Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

print("Dog Dictionary:", dog)

# Question 2.3 - Create a student dictionary and add first_name, last_name, gender,
# age, marital_status, skills, country, city and address as keys for the dictionary

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'Java', 'SQL'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

print("\nStudent Dictionary:", student)

# Question 2.4 - Get the length of the student dictionary
print("\nLength of Student Dictionary:", len(student))

# Question 2.5 - Get the value of skills and check the data type, it should be a list
skills = student['skills']
print("\nStudent Skills:", skills)
print("Data Type of Skills:", type(skills))

# Question 2.6 - Modify the skills values by adding one or two skills
student['skills'].append('React')
student['skills'].append('Angular')
print("\nUpdated Student Skills:", student['skills'])

# Question 2.7 - Get the dictionary keys as a list
keys = list(student.keys())
print("\nStudent Dictionary Keys:", keys)

# Question 2.8 - Get the dictionary values as a list
values = list(student.values())
print("\nStudent Dictionary Values:", values)
