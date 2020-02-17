# Stan O 2020
# If you are reading this, I want you to do know I made this instead of studying
import random as r

import click


@click.command()
@click.option('--lower-bound', default=3)
@click.option('--upper-bound', default=15)
def generate_word(lower_bound, upper_bound):
    if upper_bound < lower_bound:
        raise AttributeError("The lower bound must be greater than the upper bound.")

    consonants = list("qwrtyplkjhgfdszxcvbnm")
    vowels = list("aeiou")

    generated_word = ""

    for i in range(r.randint(lower_bound, upper_bound)):
        if r.randint(1, 2) == 1:
            generated_word += r.choice(consonants)
        else:
            generated_word += r.choice(vowels)

    print(generated_word)

    # to self https://www.thoughtco.com/sounds-in-english-language-3111166


if __name__ == '__main__':
    generate_word()
