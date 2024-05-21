# Create a tuple containing names of your sisters
sisters = ('Rachel', 'Emily', 'Sophia')

# Create a tuple containing names of your brothers
brothers = ('Michael', 'David', 'Alex')

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print("Siblings Tuple:", siblings)

# How many siblings do you have?
num_siblings = len(siblings)
print("Number of Siblings:", num_siblings)

# Modify the siblings tuple and add the name of your father and mother
# and assign it to family_members
father = 'John'
mother = 'Jane'
family_members = siblings + (father, mother)
print("Family Members Tuple:", family_members)
