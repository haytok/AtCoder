S = input()

alphabet_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    ]

for s in S:
    if s in alphabet_list:
        alphabet_list.remove(s)
if len(alphabet_list) == 0:
    print("None")
else:
    print(alphabet_list[0])

# S = input()
# ans = None
# for letter in "abcdefghijklmnopqrstuvwxyz":
#     if letter not in S:
#         ans = letter
#         break
# print(ans)