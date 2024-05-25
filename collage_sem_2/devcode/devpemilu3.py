# no 5 berhasil tapi 4 dan 6 tidak

def cekSuaraSah(lembarSuara):
    # Memeriksa apakah ada tanda "x" di dalam kurung "()"
    if "xx" in lembarSuara:
        return "sah"
    elif "(x)" in lembarSuara:
        return "sah"
    # Memeriksa apakah ada tanda "x" di luar kurung atau dalam pola yang salah
    elif "x" in lembarSuara or ")x(" in lembarSuara:
        return "tidak sah"
    # Memeriksa jika tidak ada tanda "x" sama sekali
    else:
        return "tidak sah"

# no 4 dan 6 berhasil tapi no 5 tidak 
def cekSuaraSah(lembarSuara):
    if "xx" in lembarSuara:
        return "tidak sah"
    elif "(x)" in lembarSuara:
        return "sah"
    elif "x" in lembarSuara or ")x(" in lembarSuara:
        return "tidak sah"
    else:
        return "tidak sah"

lembarSuara = "(" + "x" + ")" + "(" + ")" + "(" + ")"
p = cekSuaraSah(lembarSuara)
print(p)
