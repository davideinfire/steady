class Exporter:

    def save(

        self,

        puzzles,

        filename

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            for puzzle in puzzles:

                file.write(

                    f"{puzzle.category}\n"

                )

                file.write(

                    f"{puzzle.difficulty}\n"

                )

                file.write(

                    puzzle.text

                )

                file.write(

                    "\n\n"

                )
