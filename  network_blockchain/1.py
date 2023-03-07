import random

key = "abcdefghijklmnopqrstuvwxyz"
value=list(key)
random.shuffle(value)
dict_E = dict(zip(key, value))
dict_D=dict(zip(dict_E.values(),dict_E.keys()))

def encryptText(inputText):
    str = ""
    for i in inputText:
        if i==" ":
            str+=i

        if i in dict_E:
            str+=dict_E[i]
    return str

def decryptText(inputText):
    str = ""
    for i in inputText:
        if i==" ":
            str+=i

        if i in dict_D:
            str+=dict_D[i]
    return str

cryptogram = encryptText(input("평문 입력: "))
print("암호문: ", cryptogram)
print("복호문: ", decryptText(cryptogram))