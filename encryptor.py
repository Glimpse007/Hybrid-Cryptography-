#This is a key generation proogram using the in-built python library and rsa algorithm .
#reference document for cryptography library: https://cryptography.io/en/latest/fernet/
import random

from cryptography.fernet import Fernet

from rsa import decrypt, encrypt


def isprime(num):
    for i in range(2, num):
	    if num % i  == 0:
		    return False
    else:
	    return True

def encrypt_using_lib(part1):
    key1 = Fernet.generate_key()
    f = Fernet(key1)
    cipher1 = f.encrypt(part1.encode("utf-8"))
    return cipher1,key1

def encrypt_using_rsa(part2):
    key2,nums,cipher2 = encrypt(part2)
    print("Cipher2: ",cipher2,"Nums: ",nums)
    return cipher2,key2

