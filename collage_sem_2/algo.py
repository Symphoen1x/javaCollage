# # row = int(input("Enter the # to count of vertical\t"))
# # columns = int(input("Enter the # to count of horizontal\t"))
# # symbol = input('Enter the symbol 1 to using this program\t')

# # for y in range(row):
# #     for x in range(columns):
# #         print()
# #     print(symbol, end="")


# row = int(input("Enter the # to count of vertical\t"))
# columns = int(input("Enter the # to count of horizontal\t"))
# # symbol = input('Enter the symbol 1 to using this program\t')

# for y in range(1, row+1):
#     for x in range(1, columns+1):
#         print(x, end="")
#     print()


# # rows = int(input("Enter the number of rows"))

n = int(input("masukan inputan\t"))


# for row in range(1, n+1):
#     for column in range(1, n+1):
#         if row == (n/2):
#             print("+", end='')
#         elif column == (n/2):
#             print("+", end='')
#         else:
#             print("-", end='')
#     print()


for row in range(1, n+1):
    for column in range(1, n+1):
        if row == column or (row+column) == (n+1):
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()
