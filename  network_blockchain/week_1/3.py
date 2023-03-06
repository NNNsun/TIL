from cryptography.fernet import Fernet

key = Fernet.generate_key()
fr = Fernet(key)

with open('data.txt','rb') as txt:
    myData = txt.read()

cryptogram = fr.encrypt(myData)

with open('encrypted.txt','wb') as txt:
    txt.write(cryptogram)

with open('encrypted.txt','rb') as txt:
    cryptogram = txt.read()

decryptText = fr.decrypt(cryptogram)

print("< 복호화가 진행 된 data > \n"+ decryptText.decode())