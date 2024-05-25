
# skip dulu terlalu susah

def hitungKorban(gambaran, kekuatan):
    bangunan_hancur = kekuatan // 10  # Menghitung jumlah bangunan yang hancur
    total_korban = 0
    i = 0
    buildings_destroyed = 0  # Menghitung jumlah bangunan yang telah dihancurkan

    while i < len(gambaran) and buildings_destroyed < bangunan_hancur:
        if gambaran[i] == 'b':
            i += 1
            jumlah_bangunan = 0
            while i < len(gambaran) and gambaran[i].isdigit():
                jumlah_bangunan = jumlah_bangunan * 10 + int(gambaran[i])
                i += 1

            if i < len(gambaran) and gambaran[i] == 'm':
                i += 1
                jumlah_manusia = 0
                while i < len(gambaran) and gambaran[i].isdigit():
                    jumlah_manusia = jumlah_manusia * 10 + int(gambaran[i])
                    i += 1

                total_korban += jumlah_bangunan * jumlah_manusia
                buildings_destroyed += 1
            else:
                continue
        else:
            i += 1

    return total_korban


# Pengujian Fungsi
print(hitungKorban("b2m3b3m2", 50))  # Output: 12
print(hitungKorban("b2m2b3m1", 30))  # Output: 5
print(hitungKorban("b1m2", 30))      # Output: 2
