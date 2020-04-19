STUDENTS = (
    'Alice', 'Bob', 'Charlie', 'David',
    'Eve', 'Fred', 'Ginny', 'Harriet',
    'Ileana', 'Joseph', 'Kincaid', 'Larry',
)

PLANTS = {
    'C': 'Clover', 'G': 'Grass', 
    'R': 'Radishes', 'V': 'Violets',
}


class Garden:
    """Class to represent a kindergarten garden."""
    def __init__(self, diagram, students=STUDENTS):
        self.rows = diagram.split()
        kids = sorted(students)
        sets = zip(*([iter(self.rows[0])]*2
                   + [iter(self.rows[1])]*2))
        self.cups = {s:p for s,p in zip(kids, sets)}

    def plants(self, student):
        """Returns the plants a student is responsible for."""
        return [PLANTS[plant] for plant in self.cups[student]]

    def plants_all_students(self):
        """Returns all student plant responsibilities."""
        return {s:[PLANTS[p] for p in self.cups[s]]
                for s in self.cups}

    def plants_in_row(self, row=1):
        """Returns all the plants present in a row."""
        return [PLANTS[plant] for plant in self.rows[row-1]]

    def count_plant(self, plant='C'):
        """Returns how many times a plant has been planted."""
        return (PLANTS[plant],
                sum(row.count(plant) for row in self.rows))
