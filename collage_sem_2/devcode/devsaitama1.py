def klasifikasiHero(kekuatan, penghargaan):
    if kekuatan >= 3000 and penghargaan >= 30:
        return "S"
    elif kekuatan >= 2000 and penghargaan >= 20:
        return "A"
    elif kekuatan >= 1000 and penghargaan >= 10:
        return "B"
    else:
        return "C"


# Contoh penggunaan fungsi
print(klasifikasiHero(3000, 30))
