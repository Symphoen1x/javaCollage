# print("{2}, {1}, {0}".format(*"abo") )
# penggunaan syntax format untuk mengubah urutan index.
# penggunaan (*) untuk menjangkau keseluruhan string dalam format(*"XXXX")
# JUMLAH STRING ITU MENYESUAIAKAN PARAMETER STRING AWAL YANG MENDEFINE INDEX URUTAN.

# code tersebut sama dengan cara seperti ini, tapi kalo index mau di edit harus dirubah sedikit.
def my(*unlimitedArgumen):
    print(unlimitedArgumen)
my(*"abc")

