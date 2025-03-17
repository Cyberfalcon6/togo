"""version one of the counter"""
print("please give us your text: ", end="")
txt = input()
print(len(txt))

"""version two of the counter"""
# print("please give us your text: ", end="")
# txt = input()
# txt1=txt.replace(" ", "")
# print(len(txt))
# print(len(txt1))

"""doing it in one line"""
print("please give us your text: ", end="")
txt = input()
print(len(txt.replace(" ", "")))