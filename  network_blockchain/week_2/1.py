import base64
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA

with open('private_key.pem', 'rb') as privateKeyFile:
    privateKey = RSA.importKey(privateKeyFile.read())
with open('public_key.pem', 'rb') as publicKeyFile:
    publicKey = RSA.importKey(publicKeyFile.read())

usertext = input("사용자(평문) 입력= ")
aesKey = get_random_bytes(32)

msgEncryption = AES.new(aesKey, AES.MODE_EAX)
cryptogramText,hmacTag  = msgEncryption.encrypt_and_digest(usertext.encode())

rsa = PKCS1_OAEP.new(publicKey)
encodeAesKey = rsa.encrypt(aesKey)

encodeMsg = base64.b64encode(cryptogramText).decode()
encodedAeskey = base64.b64encode(encodeAesKey).decode()

receiverAesKey = PKCS1_OAEP.new(privateKey).decrypt(base64.b64decode(encodedAeskey))

msgEncryption = AES.new(receiverAesKey, AES.MODE_EAX, msgEncryption.nonce)
decrypted_plaintext = msgEncryption.decrypt_and_verify(base64.b64decode(encodeMsg), hmacTag)

print("입력문을 암호화: ", encodeMsg)
print("입력문을 복호화: ", decrypted_plaintext.decode())