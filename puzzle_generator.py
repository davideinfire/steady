import random

from models import Puzzle
from difficulty import random_level
from category_service import CategoryService

class PuzzleGenerator:

    def create(

        self,

        data

    ):

        person1, person2 = random.sample(

            data["people"],

            2

        )

        color1, color2 = random.sample(

            data["colors"],

            2

        )

        obj = random.choice(

            data["objects"]

        )

        text = (
            f"{person1} and {person2} each have a "
            f"{obj}. One is {color1}, the other is {color2}. "
            f"{person1} does not own the {color1} one. "
            f"Who owns each {obj}?"
        )

        return Puzzle(

            title="Generated Puzzle",

            category=CategoryService().pick(),

            difficulty=random_level(),

            text=text

        )
