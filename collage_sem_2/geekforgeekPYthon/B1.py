# Permainan menebak angka dengan Python 
# TUgas:
'''
Buatlah permainan menebak angka, di mana pengguna memilih rentang.
Katakanlah Pengguna memilih rentang, yaitu dari A ke B , di mana A dan B termasuk dalam Integer.
Beberapa bilangan bulat acak akan dipilih oleh sistem dan pengguna harus menebak bilangan bulat tersebut dalam jumlah tebakan minimum
'''
# ANalisis
'''
* JIka input user telalu kecil, maka beri "Input terlalu kecil"
* Jika input user terlalu besar, maka beri "Input terlalu besar"
* JUmlah tebakan bergantung pada rentang. Jadi buat sistem yang menharuskan compiler python menghitung jumlah tebakan minimum
* rumus jum minimum: 2 log(batas atas - batas bawah + 1)
'''

# Algoritma
'''
Pengguna memasukkan batas bawah dan batas atas rentang.
Kompiler menghasilkan bilangan bulat acak antara rentang dan menyimpannya dalam variabel untuk referensi di masa mendatang.
Untuk tebakan berulang, perulangan while akan diinisialisasi.
Jika pengguna menebak angka yang lebih besar dari angka yang dipilih secara acak, pengguna mendapat keluaran “ Coba Lagi! Anda menebak terlalu tinggi “
Lain Jika pengguna menebak angka yang lebih kecil dari angka yang dipilih secara acak, pengguna mendapat keluaran “ Coba Lagi! Kamu menebak terlalu kecil”
Dan jika pengguna menebak dalam jumlah tebakan minimum, pengguna mendapat pesan “ Selamat! ” Keluaran.
Jika tidak, jika pengguna tidak menebak bilangan bulat dalam jumlah minimum tebakan, dia akan mendapatkan “ Semoga Lebih Beruntung Lain Kali! ” keluaran.
'''


import random
import math

low = int(input("Inisiasi batas bawah:\t "))
up = int(input("Inisiasi batas atas:\t"))
# menggenerate target number between range low-up by randint()
p = random.randint(low,up)  #IB
define = round(math.log(up - low + 1, 2))   #IB
print(f"kesempatan yang kamu miliki: {define}")
# chekc poin pertama gw


# inisiasi jumlah tebakan awal
count = 0
# gimana caranya biar si count ini dibuat sistem yang bisa memanage tebakan pengguna sesuai kesempatan yang diberikan
# feel gw diatur di while loopnya
# gimana cara define kesempatan minimal di setiap percobaan
choose = int(input("masukan tebakan angka tersembunyi: \t"))
# gw coba teori kebalikan
while choose not p:
    if choose > p:
        print("Coba Lagi! Anda menebak terlalu tinggi")
        count += 1
        print(f"Kamu telah melakukan percobaan sebanyak {count}")
        s = define - count
            print(f"Kesempatan kamu sisa: {s}")
        
    elif choose < p:
        print("Coba Lagi! Anda menebak terlalu rendah")
        count += 1
        print(f"Kamu telah melakukan percobaan sebanyak {count}")
        s = define - count
        print(f"Kesempatan kamu sisa: {s}")
    else:
        print("Selamat")
        count += 1
        print(f"Kamu telah melakukan percobaan sebanyak {count}")
        s = define - count
        print(f"Selamat kamu berhasil menebak dengan jumlah: {s} tebakan")
        break

'''