class Renderer:

    def show(

        self,

        puzzles

    ):

        for index, puzzle in enumerate(

            puzzles,

            start=1

        ):

            print(

                f"\nPuzzle {index}"

            )

            print(

                "-" * 25

            )

            print(

                f"Category: {puzzle.category}"

            )

            print(

                f"Difficulty: {puzzle.difficulty}"

            )

            print()

            print(

                puzzle.text

            )
