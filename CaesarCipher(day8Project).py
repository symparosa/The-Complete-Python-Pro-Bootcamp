import string

alphabet = list(string.ascii_lowercase)
    
def caesar(original_text, shift_amount, encode_or_decode):
    
    output_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    
    print(f"Here's the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
    
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")

    message = input("Type your message: \n").lower()

    shift_number = int(input("Type the shift number: \n"))

    caesar(message, shift_number, action)
    
    option = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    
    if option == "no":
        should_continue = False
        print("Goodbye!")


