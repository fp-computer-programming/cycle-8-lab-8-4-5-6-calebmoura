# Author: Caleb Moura

# Function to count the number of 'a' and 'A' in a given word
def count_a(word):
    # Amount of times 'a' and 'A' is counted in the word and return the count.
    count = word.count('a') + word.count('A')
    return count

# Sample word and result of count then printed.
sample_word = "Alakazam"
result = count_a(sample_word)
print(f"The number of 'a' in '{sample_word}' is: {result}")