'''
List:

* FYI, list dalam python ketika dibuat loop maka hanya bisa bertipe data string. Silahkan buktikan sendiri dengan non-string.
* untuk format list comperhension simplenya gini:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
[expression for item in iterable if condition]
x pada dasarnya adalah elemen dalam list.
x awal(expression) adalah after atau bentuk setelah. Dia bisa diberi/dimodif ke bentu apapun bebas.
x kedua(item) adalah before atau bentuk asli dari elemen yang ada di list awal.
x ketiga adalah tempat atas perubahan dari integrasi expression + item + iterable + condition.
fruits itu adalah list awal.
newlist: list terbaru atau hasil pembentukan.

* pembuktian bahwa x awal bisa diubah,
ex 1:
newlist = [float(x) for x in range(10) if x < 5]
print(newlist)
ex 2:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)





'''
