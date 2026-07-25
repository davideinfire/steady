import random

LEVELS = [

    "Easy",

    "Medium",

    "Hard"

]

def random_level():

    return random.choice(

        LEVELS

    )
