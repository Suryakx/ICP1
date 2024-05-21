it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("Updated it_companies:", it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Samsung', 'Intel', 'Nvidia'])
print("it_companies after adding multiple companies:", it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print("it_companies after removing IBM:", it_companies)

# What is the difference between remove and discard
# remove() raises a KeyError if the element is not found, while discard() does not raise an error
print("Difference between remove() and discard():")
print("remove() raises an error if the element is not found.")
print("discard() does not raise an error if the element is not found.")

# Join A and B
joined_set = A.union(B)
print("A union B:", joined_set)

# Find A intersection B
intersection_set = A.intersection(B)
print("A intersection B:", intersection_set)

# Is A subset of B
is_subset = A.issubset(B)
print("Is A a subset of B?", is_subset)

# Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", are_disjoint)

# Join A with B and B with A
joined_with_A = A.union(B)
joined_with_B = B.union(A)
print("A union B:", joined_with_A)
print("B union A:", joined_with_B)

# What is the symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_diff)

# Delete the sets completely
del A, B

# Convert the ages to a set and compare the length of the list and the set
ages_set = set(age)
print("Ages List:", age)
print("Ages Set:", ages_set)
print("Length of Ages List:", len(age))
print("Length of Ages Set:", len(ages_set))
