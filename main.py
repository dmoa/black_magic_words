# Stan O 2020
# If you are reading this, I want you to do know I made this instead of studying

import random as r

consonants = list("qwrtyplkjhgfdszxcvbnm")
vowels = list("aeiou")

generatedWord = ""

for i in range( r.randint(3,15) ):
    if r.randint(1,2) == 1:
        generatedWord += r.choice(consonants)
    else:
        generatedWord += r.choice(vowels)

print(generatedWord)

# to self https://www.thoughtco.com/sounds-in-english-language-3111166