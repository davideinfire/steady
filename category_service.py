import random

CATEGORIES = [

    "Logic",

    "Numbers",

    "Detective",

    "Patterns",

    "Objects"

]

class CategoryService:

    def pick(self):

        return random.choice(

            CATEGORIES

        )
