# TODO 1: Delete this and put your Doc String Here


from person import Person


# Note that Student is a derived class of person
class Student(Person):

    # TODO 2: Expand __init__ to include a major, gpa, and student_id that is required
    # Hint: major and gpa should be on the right most side (except for address) and default to 'Computer Science' and '0.0'
    # student_id should be on the left most side (except for self)
    # eg: self, studentid, lname, fname, major, gpa, addy
    def __init__(self, lname, fname, addy=''):
        #This initializes the person class attributes; then we add our additional stuff below
        super.__init__(lname, fname, addy)

        # TODO 3: Don't forget to add your class attributes here

    
    # TODO 4: Override the display method by creating one here# it should output:
    # f"{self.last_name}, {self.first_name}: ({self.student_id}) {self.major} gpa: {self.gpa}"
    # eg: Song, River:(900111111) Computer Science gpa: 0.0



#Driver
if __name__ == "__main__":
    # Testing with major/gpa/address as default
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student