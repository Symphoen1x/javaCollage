'''
Keyword penting:
1. self : sebuah keyword yang menjadi referensi objek dan method sebuah class.
* Jadi, jika ingin menggunakan method dalam class tersebut harus ada parameter self sebagai rujukan objek suatu kelas.
* Seperti this dalam bahasa lain.
* parameter pertama dalam method sebuah class.
* digunakan untuk sistem oop (parent-child) dimana setiap class child dan methodnya harus punya argumen self.
* selain itu dalam code output misal print(), didalam itu harus mengandung self.objek jika output memanggil objek.
2. method __init__:
* untuk membuat instance baru suatu kelas.
* nanti pemanggilan setiap objek class harus didefine dalam  argumen yang ditampung dimethod __init__
* method khusus untuk menampung argumen berupa objek dan self.
* python membuat method khusus ini agar menyimpan sebuah nilai yang nanti di define dipemanggilan dengan cara yang beragam.
* digunakan dalam oop (parent-child). dimana di parent dia didefine awal dan child class dia juga didefine awal.

'''
