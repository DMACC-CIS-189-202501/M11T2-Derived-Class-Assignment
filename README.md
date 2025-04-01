# M11 T2: Derived Class Assignment

## Instructions for students

- Implement your solutions in `assignment.py`
- The tests in `test_assignment.py` can be inspected but do not modify them

### Directions - Copy/Pasted from Canvas

You are going to make a student class that is a Derived (or think extended) class of Person.

You will expand person by taking in an additional:
* `major` - optional, defaults to 'Computer Science
* `gpa` - optional, defaults to 0.0
* `student_id` required

You will then add a `display` method that should output in the format

~~~python
f"{self.last_name}, {self.first_name}: ({self.student_id}) {self.major} gpa: {self.gpa}"
# eg: Song, River:(900111111) Computer Science gpa: 0.0
~~~