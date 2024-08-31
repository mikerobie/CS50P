# Demonstrates iterating over and index into a dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# Iterate over the dictionary 'students'.
# For each key (student name) in the dictionary, print the key (student name) 
# and the associated value (house) separated by a comma.

for student in students:
    print(student, students[student], sep=", ")