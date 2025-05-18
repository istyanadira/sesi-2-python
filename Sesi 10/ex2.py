import numpy as np

students = np.array([2.0, 10, False], dtype=int)
print(students)

students2 = ['Denis', 'Adit', 'Adel', 'Jarwo', 10, False]
students3 = students2
students3.append(True)
students2.append(100)
print(students3)