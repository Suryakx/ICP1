sentence = "I am a teacher and I love to inspire and teach people"

# Split the sentence into a list of words
words = sentence.split()
print("Words in the sentence:", words)

# Convert the list to a set to get unique words
unique_words = set(words)
print("Unique words:", unique_words)

# Get the count of unique words
num_unique_words = len(unique_words)
print("Number of unique words:", num_unique_words)
