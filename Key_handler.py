#This is the key handler program for  GST encryption...
#from LSBSteg import *
def Key_combiner(key1,key2):
    key1 = key1.decode()
    key2 = str(key2)
    return key1 +"@"+ key2
 

def Key_handler(key1,key2):
    combined_key = Key_combiner(key1,key2)
    print("Combined Key is: ",combined_key)
    return combined_key
    # hide_key(combined_key)
    # show_key()

# def hide_key(combined_key):
#     path = "D:/College/6th SEM/Project/1.jpg"
#     output_path = "D:/College/6th SEM/Project/output.jpg"
#     #Steganography.encode(path, output_path,combined_key)
#     #LSBSteg.encode_text(combined_key)
#     secret = lsb.hide(path,combined_key)
#     secret.save(output_path)
#     print("......Successfully Created Output image.........")

# def show_key():
#     output_path = "D:/College/6th SEM/Project/output.jpg"
#     print("Revealed Key is: ",lsb.reveal(output_path))
#     # print("Revealed key is: ",key_revealed)
#     # secret_text = Steganography.decode(output_path)
#     # print("The revealed key is: ",secret_text)