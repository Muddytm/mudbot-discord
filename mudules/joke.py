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

    joke = random.choice(joke_list)

    if "{}" in joke:
        return (joke.format(name))
    else:
        return (joke)
