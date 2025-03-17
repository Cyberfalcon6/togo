# """version one of the counter"""
# print("please give us your text: ", end="")
# txt = input()
# print(len(txt))

# """doing it in one line"""
# print("please give us your text: ", end="")
# txt = input()
# print(len(txt.replace(" ", "")))

words = []
for i in range(1, 6):
    word = input(f"Enter word {i}: ")
    words.append(word)
for word in words:
    print(word,":",len(word))