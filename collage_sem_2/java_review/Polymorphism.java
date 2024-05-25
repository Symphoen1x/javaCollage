// Intinya ada banyak kelas yang berhubungan antar variabelnya.
// juga bisa sama nama methodnya, tapi outputnya beda.
/**
 * Overriding adalah suatu keadaan pada saat terjadinya polimorfisme pada suatu
 * parent class dan subclass-nya, yang mempunyai ciri-ciri sebagai berikut :
 * 1. Nama method harus sama
 * 2. Daftar parameter harus sama
 * 3. Return type harus sama
 */
class Parent {
    public void info() {
        System.out.println("Ini class Parent");// return value bentuk stirng
    }
}

class Child extends Parent {// jika tidak dinyalakan maka dia yang akan keluar saat di panggil adalah return
                            // string si parent.
    // jika dinyalakan return dibawah maka yang keluar adalah output kelas child
    // karena dia overidden terhadap method class parent.
    public void info() {
        System.out.println("Ini class Child");// return value bentuk stirng
    }
}

class Polymorphism {
    public static void main(String args[]) {
        Parent anak = new Child();
        anak.info();
    }
}

// Overloading
/*
 * Bedanya, dia dengan overridding adalah fungsionalitas/penggunaan yang
 * berbeda.
 * Dengan demikian walaupun nama method uga harus di samakan, tapi daftar
 * parameter di setiapnya harus beda agar bisa berfungsi variatif.
 * Bedanya ga cuma dari segi jumlah, tapi urutan, tipe data, dll. pengecualian
 * hanya pada nama variabel yang bertipe data sama, itu dianggap tidak ada beda/
 * malah sama.
 * Untuk return type boleh sama atau beda. misal ada yang pakai void, ada juga
 * tidak.
 * 
 */