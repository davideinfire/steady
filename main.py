from config import PUZZLE_COUNT
from config import OUTPUT_FILE

from repository import Repository
from puzzle_generator import PuzzleGenerator
from renderer import Renderer
from exporter import Exporter
from statistics import Statistics

repository = Repository()

data = repository.load()

generator = PuzzleGenerator()

puzzles = [

    generator.create(data)

    for _ in range(PUZZLE_COUNT)

]

Renderer().show(

    puzzles

)

stats = Statistics().build(

    puzzles

)

Statistics().print(

    stats

)

Exporter().save(

    puzzles,

    OUTPUT_FILE

)
