alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
cipher_text = []
alphabet_length = len(alphabet)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    out_of_index = 0
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
            if shift_index < alphabet_length:

                # 1.Index number
                # print(f"letter index: {index_}")
                # print(f"Shift Index: {shift_by}")

                # 2.Find Actual Number
                # print(f"Plain Text: {alphabet[index_]}")
                # print(f"Cipher Text: {alphabet[shift_by]}")
                cipher_text.append(alphabet[shift_index])
            elif shift_index >= alphabet_length:

                print(f"Out of Index reset number")
                print(f"Index Cover: {alphabet[out_of_index]}")
                cipher_text.append(alphabet[out_of_index])
                out_of_index += 1
        else:
            cipher_text.append(letter)

    print(f"Cipher Text: {cipher_text}")
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text=text,shift=shift)
