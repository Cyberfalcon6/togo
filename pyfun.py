# """version one of the counter"""
# print("please give us your text: ", end="")
# txt = input()
# print(len(txt))

# """doing it in one line"""
# print("please give us your text: ", end="")
# txt = input()
# print(len(txt.replace(" ", "")))

words = []
word = input(f"Enter five phrases separated by |: ")
# for i in range(1, 6):
#     word = input(f"Enter five words separated by spaces: ")
#     # words.append(word)
word = word.split("|")
for word in words:
    print(word,":",len(word.replace(" ", "")))