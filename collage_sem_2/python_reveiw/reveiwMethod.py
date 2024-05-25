'''
Berikut adalah beberapa cara umum untuk memanggil metode dalam Python:
1. Pemanggilan Metode Instan:
ex:
   class Dog:
       def bark(self):
           print("Woof!")

   my_dog = Dog()
   my_dog.bark()  # Output: Woof!

2. Pemanggilan Metode Kelas (Class Method):
Metode kelas adalah metode yang terikat pada kelas dan bukan pada instance. Metode kelas mengambil cls sebagai argumen pertama yang menunjuk ke kelas dan bukan instance.
ex:
   class Dog:
       @classmethod
       def bark(cls):
           print("Woof from all dogs!")

   Dog.bark() #konsep pemanggilanya mudah saja, yaitu class.method()
3. Pemanggilan Metode Statis (Static Method): Metode statis tidak mengambil argumen self atau cls dan bisa dipanggil pada level kelas atau instance. Metode ini tidak bergantung pada state dari instance atau kelas.
   class Dog:
       @staticmethod
       def bark():
           print("Woof!")

   Dog.bark()  # Bisa pemanggilan versi @classmethod
   my_dog = Dog() # Bisa juga pemanggilan versi instant
   my_dog.bark()  #lanjutan instant

4. Pemanggilan Metode dari Superclass:Ini digunakan dDalam inheritance, metode dari superclass bisa dipanggil menggunakan fungsi super().
lebih lanjut cek bagian file ingheritence.py terkait superclass method.
ex:
   class Animal:
       def speak(self):
           print("Animal speaks!")

   class Dog(Animal):
       def speak(self):
           super().speak()  # Memanggil metode speak dari Animal
           print("Dog barks!")

   my_dog = Dog() #jadi kenapa class ada tambahan () karena python membuat program internal class.method(instance)
   my_dog.speak()
   # Output:
   # Animal speaks!
   # Dog barks!
'''
