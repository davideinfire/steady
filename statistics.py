from collections import Counter

class Statistics:

    def build(

        self,

        puzzles

    ):

        categories = Counter(

            p.category

            for p in puzzles

        )

        return {

            "generated":

                len(puzzles),

            "categories":

                len(categories)

        }

    def print(

        self,

        stats

    ):

        print()

        print("Statistics")

        print()

        print(

            f"Puzzles: {stats['generated']}"

        )

        print(

            f"Categories: {stats['categories']}"

        )
