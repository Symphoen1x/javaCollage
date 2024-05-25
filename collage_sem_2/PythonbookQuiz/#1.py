try:
    for i in range(3):
        try:
            1/0
        except ZeroDivisionError:
            raise ZeroDivisionError(    #bentuk penambahan/pengajuan pengeceualian based on kesalahan, dia bisa berdiiri tanpa except/try
                "The code has Eror becasue You divided by zero!")
        finally:
            print("Finnaly executed")
            # break #jika ini tidak ada maka yang akan keluar ada ini ada output.
# except ZeroDivisionError:
#     print("Outer ZeroDivisionError exception caught")
