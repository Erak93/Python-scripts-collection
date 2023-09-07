from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




def encrypt(plain_text=text,shift_amount=shift):
    cipher_text=""
    for letter in plain_text:
        if letter.isalpha()==False:
            cipher_letter=letter
            cipher_text+=cipher_letter
        else:
            current_index=alphabet.index(letter)
            
            if current_index+shift_amount < len(alphabet):
                cipher_letter=alphabet[current_index+shift_amount]
                cipher_text+=cipher_letter
            else:
                difference=(current_index+shift_amount)-len(alphabet)
                cipher_letter=alphabet[difference]
                cipher_text+=cipher_letter
    return f'The encoded text is {cipher_text}'



def decrypt(transformed_text=text,shift_amount=shift):
    
    deciphered_text=""
    for letter in transformed_text:
        if letter.isalpha()==False:
            deciphered_letter=letter
            deciphered_text+=deciphered_letter
        else:
            current_index=alphabet.index(letter)
            if current_index-shift_amount <= 0:
                deciphered_letter=alphabet[(current_index-shift_amount)]
                deciphered_text+=deciphered_letter
            #elif current_index-shift_amount==0:
                #deciphered_letter=alphabet[-1]
                #deciphered_text+=deciphered_letter
            else:
                difference=(current_index+shift_amount)-len(alphabet)
                deciphered_letter=alphabet[current_index-shift_amount]
                deciphered_text+=deciphered_letter
    return f'The decoded text is {deciphered_text}'


if direction=="encode":
    print(encrypt())
elif direction=="decode":
    print(decrypt())
else:
    print("Invalid command")




    
