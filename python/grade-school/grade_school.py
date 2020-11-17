class School:
    """Class to represent a school roster."""
    def __init__(self):
        self._students = []
        
    def add_student(self, name, grade):
        """Adds a student's grade and name to the school roster."""
        if grade not in range(1, 8):
            raise ValueError("Grade can't be below 1 or above 7.")
        self._students.append((grade, name))
        self._students.sort()

    def roster(self):
        """Returns the full roster for the school."""
        return [name for grade, name in self._students]

    def grade(self, grade_number):
        """Returns the roster for a single grade."""
        return [name for grade, name in self._students if grade == grade_number]
