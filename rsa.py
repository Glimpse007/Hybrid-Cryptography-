#This is a program to implement RSA algorithm for encryption..
#This program is developed by Glimpse Salwan....
import random
def isprime(num):
    for i in range(2, num):
	    if num % i  == 0:
		    return False
    else:
	    return True
def calc_n_g():
    # initialising primes
    minPrime = 100
    maxPrime = 1000
    cached_primes = [ i for i in range(minPrime,maxPrime) if isprime(i)]
    return cached_primes
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

#Calculating value of e .
def calc_e(fi):
    for i in range(2,fi):
        if gcd(fi,i) == 1:
            return i

#Caclculating value of d.
def calc_d(fi,e):
    if gcd(fi,e) != 1:
        print("e and fi must be coprime.")
        return 0
#Method used is iterative method by trying every possible way for multiplicative inverse.
    for x in range(1, fi):
        if (((e%fi) * (x%fi)) % fi == 1):
            return x
    return -1



# Main Encryption Function....
def encrypt(plaintext):
    lists = calc_n_g()
    p = random.choice(lists)
    q = random.choice(lists)
    n = p*q
    fi = (p-1) * (q-1)
    e = calc_e(fi)
    print("E == ",e)
    ans = [] 
    x=[]
    m=0
    for i in plaintext:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            #spc=400 space value 
            x.append(400)
    for i in x:
    #space is left here on purpose .....
        if i == 400:
            ans.append(" ")
        else:
            ans.append(chr(i+97))
    n = str(n)
    fi = str(fi)
    return n+"~"+fi,x,"".join(ans)
   
# Main Decryption Function..............
def decrypt(ciphertext,key2):
    x = key2.split('~',1)
    n = int(x[0])
    fi = int(x[1])
    e = calc_e(fi)
    d = calc_d(fi,e)
    pl = []
    y = ""
    m = 0
    for i in ciphertext:
        #using space
        if i == " ":
            pl.append(400)
        else:
            pl.append(ord(i)-97)
    for i in pl:
        if(i=='400'):
            y+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            y+=c
    return d,pl,y

# #input stuff..
# p = int(input("Enter the value of p: "))
# q = int(input("Enter the value of q: "))

# #checking if p and q are prime.

# if isprime(p) and isprime(q):
#     choice = int(input("Do you want to encrypt or decrypt the data ? press 1 and 2 accordingly: "))
#     #calculating n and fi
#     n = p*q
#     fi = (p-1) * (q-1)

#     if choice == 1:
#         plaintext = input("Enter the text to be encrypted: ")
#         #calling the encrypted function and printing cipher and stuff.....
#         public_e , cipher_numbers, cipher = encrypt(plaintext,n,fi)
#         public_key = {public_e,n}
#         print("The Public Key used is: {}. ".format(public_key))
#         print("Generated List of numbers is: {} and the Generated cipher text is: {}.".format(cipher_numbers,cipher))
#     elif choice == 2:
#         ciphertext = input("Enter the text to be decrypted: ")
#         #calling the encrypted function and printing cipher and stuff.....
#         private_d , plain_numbers, orignal = decrypt(ciphertext,n,fi)
#         private_key = {private_d,n}
#         print("The Private Key used is: {}. ".format(private_key))
#         print("Generated List of numbers is: {} and the Generated Orignal text is: {}.".format(plain_numbers,orignal))
        
#     else:
#         print("Kindly enter a valid choice.")
#         exit(0)

# else:
#     print("p and q need to be prime.")
#     exit(0)

