# Author: Caleb Moura

# Function to check if input word is a palindrome.
def is_palindrome(word):
    # Converts word to lowercase to make comparison not ruined by case (suggested from my friend).
    word = word.lower()
    
    # Compare  word with its reverse to check if it is a palindrome.
    return word == word[::-1]

# Prompt user for word input and determine result.
word_to_check = (input("Enter word you believe is a palindrome: "))
result = is_palindrome

# Print if word is palindrome or not.
if result:
    print(f"{word_to_check} is a palindrome.")
else:
    print(f"{word_to_check} is not a palindrome.")