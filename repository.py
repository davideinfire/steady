from sample_data import PEOPLE
from sample_data import OBJECTS
from sample_data import COLORS
from sample_data import ANIMALS

class Repository:

    def load(self):

        return {
            "people": PEOPLE,
            "objects": OBJECTS,
            "colors": COLORS,
            "animals": ANIMALS
        }
