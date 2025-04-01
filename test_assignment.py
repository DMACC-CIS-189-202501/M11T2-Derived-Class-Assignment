import pytest
import ast
import importlib

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Test to check the display method for default values
def test_display_default_values():
    from assignment import Student

    student = Student(900111111, 'Song', 'River')
    expected_output = "Song, River: (900111111) Computer Science gpa: 0.0"
    assert student.display() == expected_output, "DMACC Student, check that you are properly defaulting GPA to 0.0 and major to 'Computer Science'."

# Test to check the display method with specified major
def test_display_specified_major():
    from assignment import Student

    student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    expected_output = "Song, River: (900111111) Computer Engineering gpa: 0.0"
    assert student.display() == expected_output, "DMACC Student, ensure that the major is correctly set when specified."

# Test to check the display method with specified major and gpa
def test_display_specified_major_and_gpa():
    from assignment import Student

    student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    expected_output = "Song, River: (900111111) Computer Engineering gpa: 4.0"
    assert student.display() == expected_output, "DMACC Student, ensure that both the major and GPA are correctly set when specified."

if __name__ == "__main__":
    pytest.main()