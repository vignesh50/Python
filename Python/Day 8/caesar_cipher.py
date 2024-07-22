alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art

print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26

alphabet_length = len(alphabet)


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_field, shift_number):
    cipher_text = ""
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    # print(f"Plain Text: {text}")
    #cipher_text = "mjqqt"
    for letter in text:
        if letter in alphabet:
            index_ = alphabet.index(letter)
            shift_index = index_ + shift
            cipher_text += alphabet[shift_index]
        else:
            cipher_text += letter

    print(f"Cipher Text: {cipher_text}")
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text_field, shift_number):
    cipher_text = ""
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    # print(f"Plain Text: {text}")
    #cipher_text = "mjqqt"
    for letter in text:
        if letter in alphabet:
            index_ = alphabet.index(letter)
            shift_index = index_ - shift
            cipher_text += alphabet[shift_index]
        else:
            cipher_text += letter

    print(f"Cipher Text: {cipher_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


if direction == "encode":
    encrypt(text_field=text, shift_number=shift)
else:
    decrypt(text_field=text, shift_number=shift)

