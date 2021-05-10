#This is a Decryptor program using the in-built python library and rsa algorithm .
#reference document for cryptography library: https://cryptography.io/en/latest/fernet/
import random

from cryptography.fernet import Fernet

from rsa import decrypt, encrypt
def calculate_ciphers(combined_cipher):
    x = combined_cipher.split('@',1)
    return x[0],x[1]
def decrypt_using_lib(cipher1,key1):
    key1 = key1.encode()
    f = Fernet(key1)
    part1 = f.decrypt(cipher1.encode())
    return part1.decode()
def decrypt_using_rsa(cipher2,key2):
    p,nums,part2 = decrypt(cipher2,key2)
    print("part2: ",part2,"Nums: ",nums,p)
    return part2
def Decryp(combined_cipher,combined_key):
    cipher1,cipher2 = calculate_ciphers(combined_cipher)
    key1 , key2 = calculate_ciphers(combined_key)
    part1 = decrypt_using_lib(cipher1,key1)
    part2 = decrypt_using_rsa(cipher2,key2)
    return part1,part2
