# Mencoba implementasi inheritance oop terkait parent class top dengan sebuah child class menggunakan  super() function
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)


class On(Person):
    def __init__(self, fname, lname, status):
        super().__init__(fname, lname)
        self.kelulusan = status

    def student(self):
        print("Student who's name:", self.firstname,
              self.lastname, "has", self.kelulusan)


# Membuat instance dari kelas Student dan On
x = Student("Mike", "Olsen", 2019)
x.welcome()
p = On("Uni", "tun", "lulus")
p.student()

# percobaan jika saya ingin menjadikan child class dari parent awal menjadi parent class untuk sebuah class child


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)


class Postgraduate(Student):
    def __init__(self, fname, lname, year, thesis_title):
        super().__init__(fname, lname, year)
        self.thesis_title = thesis_title

    def print_thesis_title(self):
        print("Thesis Title:", self.thesis_title)


# Membuat instance dari kelas Postgraduate
pg_student = Postgraduate("Sarah", "Connor", 2021, "AI and Society")
pg_student.welcome()
pg_student.print_thesis_title()


# Versi kedua dengan perbedaan syntax pemanggilan kelas : percobaan jika saya ingin menjadikan child class dari parent awal menjadi parent class untuk sebuah class child
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)


class Postgraduate(Student):
    def __init__(self, fname, lname, year, thesis_title):
        super().__init__(fname, lname, year)
        self.thesis_title = thesis_title

    def print_thesis_title(self):
        # jadi saya akan membuat code lebih efisien dengan cara menggabungkan format output ke satu fungsi.
        print("Welcome", self.firstname, self.lastname, "to the class of",
              self.graduationyear, "\nThesis Title:", self.thesis_title)


# Membuat instance dari kelas Postgraduate
pg_student = Postgraduate("Sarah", "Connor", 2021, "AI and Society")
pg_student.print_thesis_title()
