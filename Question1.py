# Function to encrypt the content
def encrypt(text, shift1, shift2):
    encrypted = ""
    for char in text:
        ''' 
        Checking the condition that the text is Captial aplhabet or not. 
        If the aplhabet lies between (A-M) then the character is shifted backward by the shift1 value.
        Encryption is done between (A-M) only, and the alphabets don't exceed than M.
        If the alphabet is captila and lies between (N-Z) then the character is shifted forward by the addition of the shift1 and shift2 value
        '''
        if char.isupper():
            if 'A' <= char <=  'M':
                encrypted += chr((ord(char) - ord('A') - shift1) %13 + ord('A')) 
            elif 'N' <= char <= 'z':
                shift = shift2 * shift2
                encrypted += chr((ord(char) - ord('N') + shift) %13 + ord('N'))
        elif char.islower():
            if 'a' <= char <= 'm':
                shift = shift1 * shift2
                encrypted += chr((ord(char) - ord('a') + shift) %13 + ord('a'))
            elif 'n' <= char <= 'z':
                shift = shift1 + shift2
                encrypted += chr((ord(char) - ord('n') - shift) %13 + ord('n'))
        else:
            encrypted += char
    return encrypted



# Operations for the input of the shift value and content of the file.
try:
    # Givin the shif value to shift the data 
    shift1 = int(input("Enter the first shift value: "))
    shift2 = int(input("Enter  the second shift value: "))


    # creating the  file and inserting the text in the file 
    raw_text = input("Write the file content: ")

    # Writing the content to be encrypted in the file raw_text.txt
    with open("raw_text.txt", 'w+') as file:
        file.write(raw_text)
        file.seek(0)
        raw_text = file.read()
    print("\n\n"+"Sentences have been saved to 'raw_text.txt'")

    # Encrypting the content of the file using Encrypt function
    encrypt_text = encrypt(raw_text, shift1, shift2)

    # Writing the encrypted text in the file encrypt_text.txt
    with open("encrypt_text.txt", 'w+') as file:
        file.write(encrypt_text)
        print("\n\n" + "Encrypted has been sucessfull.")
        file.seek(0)
        enc_text = file.read()

    print("\n\n"+ "The raw text are: " + "\n")
    print(raw_text)
    print("\n\n"+ "The Encrypted text are: " + "\n")
    print(enc_text)

except FileNotFoundError as e:
    print("Error: {e}")
