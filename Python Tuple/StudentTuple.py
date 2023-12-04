# Function to create a tuple with student information
def create_student_tuple(name, age, grade):
    student_tuple = (name, age, grade)
    return student_tuple

# Function to display student information from a tuple
def display_student_info(student_tuple):
    name, age, grade = student_tuple
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

# Example usage
student1_info = create_student_tuple("Alice", 18, "A")
student2_info = create_student_tuple("Bob", 20, "B")

# Display student information
print("Student 1:")
display_student_info(student1_info)

print("\nStudent 2:")
display_student_info(student2_info)
