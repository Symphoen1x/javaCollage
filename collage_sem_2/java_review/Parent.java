public class Parent {
    String parentName;

    public Parent(String parentName) {
        this.parentName = parentName;// jadi parent class juga dapat diberi this karena this berfungsi sebagai
                                     // pembeda. Argumen si cosnstructor itu sama namanya kayak variabel.
    }
}
/*
 * 
 * - `String parentName` adalah variabel instan dari kelas `Parent`.
 * - `public Parent(String parentName)` adalah konstruktor yang memiliki
 * parameter `parentName`.
 * - `this.parentName = parentName;` menyatakan bahwa nilai dari parameter
 * `parentName` harus diinisialisasi ke variabel instan `parentName` dari objek
 * tersebut.
 * - Penggunaan `this` membantu dalam menghindari kebingungan antara variabel
 * instan dan parameter karena mereka memiliki nama yang sama. Ini adalah
 * praktik yang sangat umum dan disarankan untuk kejelasan kode.
 * 
 * 
 */