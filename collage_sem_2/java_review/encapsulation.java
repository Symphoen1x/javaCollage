/*
 * * Apa itu void?
 * : intinya si void ini digunakan untuk indikasi
 * bahwa sebuah method/function tidak mengembalikan nilai apapun(return)
 * *Keyword baru di encapsulation: set and get.
 * 1. set: ini dan anu itu berpasangan. Tujuan ini adalah untuk membuat objek memiliki sebuah value.
 * 2. get: ini adalah cara agar value yang di define dengan set itu bisa keluar menjadi output.
 * : Getter (Metode Pembaca)
Getter adalah metode yang digunakan untuk mengambil atau membaca nilai dari atribut privat sebuah kelas.
Setter (Metode Penulis)
Setter adalah metode yang digunakan untuk menetapkan atau mengubah nilai dari atribut privat sebuah kelas.

 */

/*
 * QNA:
 * 1. penggunaan nama class yang tidak diawali public itu termasuk acces modifer default?
 * jika iya, bedanya apa dengan yang disertai public?



// pembuktian kenapa Atribut nama adalah read-only karena hanya memiliki metode getter (getNama()), yang memungkinkan hanya pembacaan nilai.
Atribut umur adalah write-only karena hanya memiliki metode setter (setUmur(int)), yang memungkinkan hanya penulisan nilai tanpa kemampuan membaca nilai tersebut kembali.
// 1. kondisi ketika write-only dan read-only
 */
class DataPribadi {
    // Atribut private sehingga tidak bisa diakses langsung dari luar kelas
    private String nama;
    private int umur;

    // Constructor: kayak __init__ function in pyton
    public DataPribadi(String nama, int umur) {
        this.nama = nama;
        this.umur = umur;
    }

    // Metode getter untuk nama - membuat atribut nama sebagai read-only
    public String getNama() {
        return nama;
    }

    // public void setNama(String nama) {
    // this.nama = nama;
    // }

    // Metode setter untuk umur - membuat atribut umur sebagai write-only
    public void setUmur(int umur) {
        this.umur = umur;
    }

    // Metode getter untuk umur - membuat atribut umur dapat dibaca
    // public int getUmur() {
    // return umur;
    // }
}

public class encapsulation {
    public static void main(String[] args) {
        DataPribadi orang = new DataPribadi("Budi", 25);
        // orang.setNama("surtaman");
        // Mencoba membaca nama
        System.out.println("Nama: " + orang.getNama());

        // Mencoba menulis umur
        orang.setUmur(30);
        // Sekarang kita bisa membaca umur juga
        // System.out.println("Umur: " + orang.getUmur());
    }
}
// Cek output code tersebut, pasti : getNama() hanya mengeluarkan output dengan
// catatan dia tidak bisa diganti/ubah nilai karena tidak ada fasilitas set()
// sebagai penulisan value objek secara bebas.
// itu dinamakan read-only.
// Lalu si setUmur() hanya bisa menulis value secara bebas, tetapi tidak bisa
// terlihat outputna. Ini dinamakan write-only.

// contoh kode yang benar
// class DataPribadi {
// // Atribut private sehingga tidak bisa diakses langsung dari luar kelas
// private String nama;
// private int umur;

// // Constructor: kayak __init__ function in pyton
// public DataPribadi(String nama, int umur) {
// this.nama = nama;
// this.umur = umur;
// }

// // Metode getter untuk nama - membuat atribut nama sebagai read-only
// public String getNama() {
// return nama;
// }

// public void setNama(String nama) {
// this.nama = nama;
// }

// // Metode setter untuk umur - membuat atribut umur sebagai write-only
// public void setUmur(int umur) {
// this.umur = umur;
// }

// // Metode getter untuk umur - membuat atribut umur dapat dibaca
// public int getUmur() {
// return umur;
// }
// }

// public class encapsulation {
// public static void main(String[] args) {
// DataPribadi orang = new DataPribadi("Budi", 25);
// orang.setNama("surtaman");
// // Mencoba membaca nama
// System.out.println("Nama: " + orang.getNama());
// // Mencoba menulis umur
// orang.setUmur(30);
// // Sekarang kita bisa membaca umur juga
// System.out.println("Umur: " + orang.getUmur());
// }
// }
