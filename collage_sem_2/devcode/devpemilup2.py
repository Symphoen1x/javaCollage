
# # using extend
# def pasanganPresiden(namaCalon, noUrut):
#     if noUrut == 1:
#         return namaCalon[0:2]
#     elif noUrut == 2:
#         return namaCalon[2:4]
#     elif noUrut == 3:
#         return namaCalon[4:6]
#     else:
#         return ["kosong"]
# s = ["Ahmad", "Kurla", "Romli", "Karsa", "Ruan", "Nirlo"]
# p = pasanganPresiden(s, 7)
# print(p)


# using extend
def pasanganPresiden(namaCalon, noUrut):
    result = []
    if noUrut == 1:
        result.extend(namaCalon[0:2])
    elif noUrut == 2:
        result.extend(namaCalon[2:4])
    elif noUrut == 3:
        result.extend(namaCalon[4:6])
    else:
        result.extend(["kosong"])
    return result

s = ["Ahmad", "Kurla", "Romli", "Karsa", "Ruan", "Nirlo"]
p = pasanganPresiden(s, 7)
print(p)