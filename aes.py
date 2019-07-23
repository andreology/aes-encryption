
#CBC MODE 
from Crypto.Cipher import AES

key = "Sixteen byte key"
iv = "Initialization V"
plain = "Secret: 16 bytesSecret: 16 bytesSecret: 16 bytes" 
cipher = AES.new(key, AES.MODE_CBC, iv)
print(cipher.encrypt(plain))

#ECB MODE 
#from Crypto.cipher import AES 
#key = "Sixteen Byte Key"
#plain = "Secret: 16 BytesSecret: 16 BytesSecret: 16 Bytes"
#cipher = AES.new(key)
#print(cipher.encrypt(plain))

