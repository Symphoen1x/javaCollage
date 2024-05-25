/**
 * Secara garis besar ada dua tipe, yaitu subclass(child) dan
 * supperclass(parent)
 * Keyword yang digunakan adalah expand(kelas parent)
 * Protected modifer digunakan untuk membuat sebuah objek yang didefine agar
 * privat sehingga tidak dapat diakses oleh kelas lain kecuali inheritance.
 * final modifer juga ada. gunanya agar suatu class dalam oop itu tidak
 * menggunakan/menyertakan suatu class. Kayak diskip aja tu class.
 */

/**
 * Penggunaan this dan apa itu.
 * 1. referensi variabel yang milik class parent.
 * 3. referensi variabel anatar constructor method.
 */

/*
 * // To-do: tambah ilmu dari ppt collage
 * class parent {//kenapa code class parent ini bisa satu file dengan main
 * classnya? karena dia bukan public class melainkan default sehingga bisa.
 * public int x = 5; //constructor parent
 * }
 * 
 * class Child extends parent {
 * public int x = 10; //constructor child yang mana harus di define ulang
 * variabelnya karena dia bersifat tidak mewarisi induknya. Kalo lupa tenang aja
 * otomatis dibantu compiler java.
 * 
 * public void Info(int x) {
 * System.out.println("Nilai x sebagai parameter = " + x);// merujuk pada
 * variabel x terdekat, yaitu parameter info() karena logikanya argumen x pada
 * info(x) yang dilakukan pemanggilan di kelas main ya merujuk ke dia.
 * 
 * System.out.println("Data member x di class Child = " + this.x);//merujuk pada
 * variabel class child karena this menargetkan variabel yang hanya ada di kelas
 * itu sendiri. sehingga ketika
 * //terjadi situasi di mana variabel dengan nama yang sama ada di kelas induk
 * dan kelas anak, itu dapat membantu membedakan rujukan variabel lokal dan
 * variabel yang diwarisi(dengan cara super())
 * 
 * System.out.println("Data member x di class Parent = " + super.x);//merujuk
 * pada variabel class parent karena sebagai sifat pewarisan oleh induk ke anak.
 * Ini melanjutkan kejadian sebelumnya agar dapat membedakan variabel yang sama
 * namanya di kelas parent dna child.
 * }
 * }
 * 
 * public class inheritance {// main class dan harus sama namanya dengan file.
 * public static void main(String args[]) {
 * Child tes = new Child();
 * tes.Info(20);
 * }
 * }
 */
// Terapan kedua

// INFO: ini menggunakan Parent class public sehingga file terpisah. karena
// aturan dari java.

class Baby extends Parent {
    public Baby(String parentName) {
        // super(parentName); // code cara Memanggil konstruktor Parent karena
        // constructor itu kayak class.
    }

    public void Cry() {
        System.out.println("Owek owek");
    }
}

public class inheritance {
    public static void main(String[] args) {
        Baby bayi = new Baby("NamaParent"); // Sekarang ini valid
        bayi.Cry();
    }
}