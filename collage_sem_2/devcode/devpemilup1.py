def persentaseSuara(populasiHela, populasiSakaar, populasiXandar):
    totalPopulasi = populasiHela + populasiSakaar + populasiXandar
    populasiKonoha = 1000000
    persentase = (totalPopulasi/populasiKonoha) * 100
    return f"{persentase:.2f}%"


p = persentaseSuara(300000, 210000, 110000)
print(p)
