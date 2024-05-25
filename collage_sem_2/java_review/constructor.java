/*
 * * TUjuan: intinya si konstruktor ini beda dengan method.
 * karena dia lebih untuk insialisasi method/objek suatu class.
 * Dia tidak bertipe return kayak method, tapi bentuknya mirip
 * dan bisa naruh argument di dalam situ kayak method.
 * Selain itu, kosntruktor ini memiliki nama yang sama dengan nama class.
 * Pemanggilan dia itu otomatis saat variabel baru dibuat dari suatu kelas.
 * Tenang aja, java nyediain otomatis ni konstruktor sebagai constructor default
 * tanpa harus dibuat.
 * * Maksud dari constructor default itu tidak memiliki parameter dan tidak
 * melakukan apa-apa.
 * jadi, dia hanya memanggil kosntruktor supperclass biasanya sih ototmatis ada.
 * * Kelebihan ketika mendefinisikan konstruktor manual/sendiri:
 * 1. bisa inisialisasi secara kustom dan melakukan operasi lain lebih banyak
 * sehingga kita dapat mengambil parameter dan menggunakan parameter untuk atur
 * nilai variabel class.
 * 2. punya kontrol value si variabel tanpa harus ngedefine value variabel
 * class.
 * * Overloading constructor = terjadi banyak  constructor/lebih dari 1.
 * Jika suatu class punya lebih dari 1 konstruktor syaratnya itu
 * parameter/argumen-> (a, b) dalam setiap construktor tdiak boleh sama.
 */

//  contoh overloading constructor dalam satu
// public class constructor {
//     private int nim;
//     private String nama;

//     // constructor 1
//     public constructor() {
//         nim = 0;
//         nama = "";
//     }

//     // constructor 2
//     public constructor(int n) {
//         nim = n;
//         nama = "";
//     }

//     // constructor 3
//     public constructor(int n, String s) {
//         nim = n;
//         nama = s;
//     }

//     public int getNim() {
//         return nim;
//     }

//     // Method untuk menampilkan informasi siswa alias method format output
//     public void displayInfo() {
//         System.out.println("NIM: " + nim + ", Nama: " + nama);
//     }

//     // Main method versi dalam class
//     // public static void main(String[] args) {
//     // define object based beserta value
//      
//     // constructor siswa1 = new constructor(12345, "Budi")
//     // pemanggilan method format output
//     // siswa1.displayInfo();
//     // }
// }

public class constructor {
    private int nim;
    private String nama;

    // pembeda/unik pertama: ketika usertidak memberikan nilai inisialisasi nim dan
    // nama maka nim akan diset dengan nilai 0 dan nama diset dengan "".
    public constructor() { // tanpa argumen
        nim = 0;
        nama = "";
    }

    // unik kedua: jika user ingin menginisialisasi nim sesuai dengan nilai yang
    // diinginkan, maka nim akan diisi sesuai nilai yang diinginkan oleh user dan
    // nama diset dengan "".
    public constructor(int n) {// satu argumen
        nim = n;
        nama = "";
    }

    // unik ketiga: jika user ingin menginisialisasi nim dan nama sesuai dengan
    // nilai yang diinginkan, maka nim dan nama akan diisi sesuai nilai yang
    // diinginkan oleh user.
    public constructor(int n, String s) {// doble
        nim = n;
        nama = s;
    }

    // Getter untuk nim
    public int getNim() {
        return nim;
    }

    // Setter untuk nim
    public void setNim(int nim) {
        this.nim = nim;
    }

    // Getter untuk nama
    public String getNama() {
        return nama;
    }

    // Setter untuk nama
    public void setNama(String nama) {
        this.nama = nama;
    }

    public void displayInfo() {
        System.out.println("NIM: " + nim + ", Nama: " + nama);
    }
}
// running di file p.java

// QNA:
// 1. Bagaimana cara pemanggilan diluar class dengan file yang sama?