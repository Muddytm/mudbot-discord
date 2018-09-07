"""Joke telling mudule."""
import random


def telljoke(name):
    """Tell a joke!

    Variable 'name' is for jokes that involve the querying user."""
    with open("mudules/jokes/default.txt") as f:
        lines = f.readlines()

    joke_list = []
    for line in lines:
        joke_list.append(line)

    # Bug with Discord is causing me to have to do this. Angery
    joke = str(random.choice(joke_list)).replace("NEWLINE", "\n")

    # We put the joke in a string to ward off the \n monster.
    if "{}" in joke:
        return (joke.format(name))
    else:
        return (joke)
