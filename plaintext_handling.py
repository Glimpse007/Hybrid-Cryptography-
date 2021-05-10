#This the datta handling program which handles the given input written in python...
from encryptor import encrypt_using_lib , encrypt_using_rsa
from Key_handler import Key_handler
from Decryptor import Decryp
def divide(l,plaintext):
    if l % 2 == 0:
        return int(l/2) , int(l/2)
    else:
        return divide(l + 1, plaintext + "1")
def handle_data(lp1,lp2,plaintext):
    part1 = plaintext[:lp1]
    part2 = plaintext[lp1:]
    return part1 , part2
def  get_cipher(part1,part2):
    cipher1 , key1 = encrypt_using_lib(part1)
    cipher1 = cipher1.decode()
    print("Cipher1: ",cipher1,"Key1: ",key1)
    cipher2 , key2 = encrypt_using_rsa(part2)
    print("Key2: ",key2)
    
    return (cipher1 +"@"+ cipher2), key1 ,key2

def get_plain_text(combined_cipher,combined_key):
    part1 , part2 = Decryp(combined_cipher,combined_key)
    orignal = part1 + part2.lower()
    return orignal

def __main__():
    plaintext = input("Enter the secret message you want to send: ")
    l = len(plaintext)
    lp1 , lp2 = divide(l,plaintext)
    part1 , part2 = handle_data(lp1,lp2,plaintext)
    print("Part1 is :",part1)
    print("Part2 is :",part2)
    combined_cipher ,key1 ,key2 = get_cipher(part1,part2)
    print("The Combined Cipher is : ",combined_cipher)
    combined_key = Key_handler(key1,key2)
    print("after decryption......")
    orignal = get_plain_text(combined_cipher,combined_key)
    print("Orignal text obtained is: ",orignal)

__main__()