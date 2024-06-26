class User:
    def __init__(self, fname, lname, email, password):
        self.fname = fname
        self.lname = lname
        self.__email = email
        self.__password = password
       
    def user_info(self):#
        print(f"Full name:{self.fname} {self.lname}")
        print(f"Was registered using {self.__email}")
   
    def get_password(self):
        return self.__password
   
    def set_password(self, new_password ):
        if (len(new_password) < 8):
            print("password was not changed")
        else:
            print("password was succesfully changed")
            self.password = new_password
class Course:
    def __init__(self, crn, title, semester, taught_by):
        self.__crn = crn
        self.__title = title
        self.semester = semester
        self.taught_by = taught_by
   
    def get_crn(self):
        return self.__crn
   
    def set_crn(self, crn):
        self.__crn = crn
   
    def get_title(self):
        return self.__title
   
    def set_title(self, title):
        self.__title = title
   
    def course_info(self):
        print(f"CRN: {self.__crn}")
        print(f"Title: {self.__title}")
        print(f"Semester: {self.semester}")
        print(f"Taught by: {self.taught_by}")
       
        
class Student(User):
    def __init__(self, unumber, major, fname, lname, email, password, minor=None):
        super().__init__(fname, lname, email, password)
        self.unumber = unumber
        self.major = major
        self.minor = minor
        self.courses = []
   
    def user_info(self):
        super().user_info()
        print(f"University Number: {self.unumber}")
        print(f"Major: {self.major}")
        if self.minor:
            print(f"Minor: {self.minor}")
        print("User is a Student!")
        if self.courses:
            print("Courses enrolled:")
            for course in self.courses:
                course.course_info()
        else:
            print("No courses enrolled")
    
    def add_course(self, course):
        if isinstance(course, Course):
            self.courses.append(course)
    
akmal = Student("U49639540", "Computer Science", "Akmal", "Kurbanov", "akmal@usf.edu", "Password123", "Entrepreneurship")
course1 = Course("12345", "Data Structures", "Fall 2024", "Dr. Smith")
course2 = Course("67890", "Algorithms", "Spring 2024", "Prof. Johnson")
 
# Add courses to the student
akmal.add_course(course1)
akmal.add_course(course2)
 
# Display student information
print(akmal.get_password())
akmal.user_info()
 