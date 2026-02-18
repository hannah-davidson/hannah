# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

def counting_vowels_and_consonants(string):
    vowels = 0
    consonants = 0
    for letter in string.lower():
        if letter.isalpha():
            if letter in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return(vowels,consonants)
print(counting_vowels_and_consonants("Flower"))

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

def average_vowels_and_consonants(par):
    sentences = par.replace("\n",".").split('.')
    sentences = [s.strip() for s in sentences if s.strip() != ""]

    num_sentences = len(sentences)
    total_vowels = 0
    total_consonants = 0

    for sentence in sentences:
        vowels, consonants = counting_vowels_and_consonants(sentence)
        total_vowels += vowels
        total_consonants += consonants

    avg_vowels = round((total_vowels / num_sentences),2)
    avg_consonants = total_consonants / num_sentences

    return(num_sentences, avg_vowels, avg_consonants)

num_sentences, avg_vowels, avg_consonants = average_vowels_and_consonants(paragraph)
print(f"In this paragraph, there are {num_sentences} sentences, with an average of {avg_vowels} vowels and {avg_consonants} consonants.")