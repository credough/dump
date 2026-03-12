students = ["Alice", "Bob", "Charlie", "Diana"]

subjects = ("Math", "English", "Science")

grades = {
    "Alice": {"Math": 90,"English": 85, "Science": 92},
    "Bob": {"Math": 78,"English": 88, "Science": 88},
    "Charlie": {"Math": 85, "English": 90, "Science": 87},
    "Diana": {"Math": 92,"English": 95, "Science": 89}
}

for student in students:
    print(f"\nGrades for {student}")
    for subject in subjects:
        print(f"{subject}: {grades[student][subject]}")