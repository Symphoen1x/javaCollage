'''
* ilmu baru:
1. Perbedaan Penggunaan super() dan namaClass():
* Intinya penggunaan super() dalam Python adalah cara khusus untuk memanggil metode/objek dari kelas induk, terutama dalam konteks inheritance.
* sementara namaClass()merujuk pada referensi class yang menjadi anak.
* super()fungsi yang akan membuat kelas anak mewarisi semua metode dan properti dari induknya.
* super() itu pemanggilan sebuah class saja tidak bisa mewakili banyak kelas jika dalam kelas yang diwakili masing-masing tidak didefine si super()  
* jika namaClass() itu bisa di define untuk mewakili sebuah kelas, tapi dalam kelas yang diwakili/child class tidak perlu define className() masing-masing. 
2. Sebuah child class bisa di define dengan hanya:
class Student(Person):
  pass
Namun, Lebih baik menggunakan function  __init__() karena function tersebut lebih baik dipakai dari pada keyword pass.
Selain itu,  __init__() mengotomatiskan setiap kali class digunakan untuk membuat objke baru di child class.
 __init__() membuat  si class child tidak lagi mewarisi induknya karena dia mengambil alih warisan  __init__() fuction class induk.
3. Bedakan single inheritance dan multiple inherintance:
ex single inherin:
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
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# pemanggilan keseluruhan class single inheritance
x = Student("Mike", "Olsen", 2019)
x.printname() 
x.welcome()


ex: multiple inherin
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

class Output(Car, Boat, Plane):
  def __init__(self, brand, model):
    Car.__init__(self, brand, model)
    Boat.__init__(self, brand, model)
    Plane.__init__(self, brand, model)

  def move_all(self):
    Car.move(self)
    Boat.move(self)
    Plane.move(self)

#Pemanggilan keseluruhan output class yang dicakup oleh class output sebagai mutiple warisan
vehicle = Output("Tesla", "Model S")
vehicle.move_all()  # Ini akan mencetak "Drive!", "Sail!", dan "Fly!"


Jadi, prinsip si warisan/inheritance ini sama baik single maupun multiple. Setiap child class harus serasi struktunya dengan parent class.
Intinya setiap function dari parent itu seperti di duplicate di child dengan perbedaan penambahan objek dan perbedaan nama method.
Konsep paling bagus dalam oop itu pada bagian pemanggilan
'''


# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius


# # Creating an object of the Circle class
# circle1 = Circle(5)
# print("Circle Area:", circle1.area())

'''
* Abce adalah module yang disediakan oleh python.
* Kelas abstrak adalah kelas yang tidak dapat diinstansiasi sendiri dan biasanya berfungsi sebagai kerangka dasar untuk kelas lain.
anggap aja kayak template buat digunain/ditambahin input.
* @abstractmethod adalah indikasi bahwa dia adalah class abstract
* Agar tidak menjadi abstract maka class circle harus memiliki objek dan return objeknya sendiri.
'''


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     @property
#     def info(self):
#         return f"{self.brand} {self.model}"

#     @staticmethod
#     def production_year():
#         return 2022


# # Creating an object of the Car class
# car1 = Car("Toyota", "Camry")
# print(car1.info)
# print("Production Year:", Car.production_year())

'''
* @property digunakan untuk membuat metode dalam kelas berperilaku seperti atribut.
*  Ini memungkinkan kita untuk mengakses metode sebagai atribut tanpa perlu memanggilnya sebagai fungsi (tanpa tanda kurung).
* buktinya tidak ada kan di pemanggilan memanggil fungsi info()
* ibarat dia tu membuat kelogisan pemanggilan format argument kelas 
* @staticmethod digunakan untuk mendefinisikan metode yang tidak mengoperasikan instance kelas atau kelas itu sendiri. 
* Jadi dia hanya untuk di return outputnya dan boleh berupa variabel bervalue. intinya dia harus ada value.
* pemanggilan membuat dia tidak bergantung dengan objek class manapun

'''


'''
TO-do:
2. mencari tahu penjelasan __str__() dan __add__()
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


# Creating an object of the Point class
point1 = Point(1, 2)
print(point1)
point2 = Point(3, 4)
print(point2)

# Using the + operator
point3 = point1 + point2
print(point3)
