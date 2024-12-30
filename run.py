from AES import encrypt, decrypt

key = '1HundredwireKey.1HundredwireKey.'
text = '1HundredwireWiFi'

cipher_text = encrypt(key,text)
print(cipher_text)
output = decrypt(cipher_text,key)
print(output)
