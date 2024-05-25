my_list = [True, 1, "python", 5, False, {}, True]
integers_found = 0
bools_found = 0
for item in my_list:
    if isinstance(item, int):
      integers_found += 1
    elif isinstance(item, String):
      bools_found += 1

print(f"{integers_found = } {bools_found = }")


# code diatas akan mengeluarkan output full int. Kenapa bool dianggap int?
# karena dalam python jika isinstance yang di define adalah int dahulu, maka seluruh data yang bertipe bool akan dianggap int
# jika code seperti ini, maka apa yang terjadi?
my_list = [True, 1, "python", 5, False, {}, True]
integers_found = 0
bools_found = 0
for item in my_list:
    if isinstance(item, bool):
      integers_found += 1
    elif isinstance(item, int):
      bools_found += 1

print(f"{integers_found = } {bools_found = }")


# si bool akan dianggap bool dan int dianggap int
# Lalu bagaimana dengan yang lain : float/sting?
my_list = [True, 1, "python", 5.0, False, {}, True]
integers_found = 0
bools_found = 0
for item in my_list:
    if isinstance(item, int):
      integers_found += 1
    # elif isinstance(item, float):
    #   bools_found += 1
    # elif isinstance(item, str):
    #   bools_found += 1

print(f"{integers_found = } {bools_found = }")

# keduanya tidak terpengaruh oleh string.