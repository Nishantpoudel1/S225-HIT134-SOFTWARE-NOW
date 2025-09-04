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



# Function to decrypt the content
"""
This function is the decryption function. In this function the encrypted text that is stored in the encryption_text.txt is decrypted.
"""
def decrypt(text, shift1, shift2):
    decrypted = ""
    for char in text:
        if char.isupper():
            if 'A' <= char <=  'M':
                decrypted += chr((ord(char) - ord('A') + shift1) %13 + ord('A')) 
            elif 'N' <= char <= 'z':
                shift = shift2 * shift2
                decrypted += chr((ord(char) - ord('N') - shift) %13 + ord('N'))
        elif char.islower():
            if 'a' <= char <= 'm':
                shift = shift1 * shift2
                decrypted += chr((ord(char) - ord('a') - shift) %13 + ord('a'))
            elif 'n' <= char <= 'z':
                shift = shift1 + shift2
                decrypted += chr((ord(char) - ord('n') + shift) %13 + ord('n'))
        else:
            decrypted += char
    return decrypted

# Function to compare the content of the two raw_text.txt and decryption_text.txt 
def compare(raw_file, decrypt_file):
    try:
        with open(raw_file, 'r') as file1, open(decrypt_file, 'r') as file2:
            raw = file1.read()
            decpt = file2.read()

        if len(raw) != len(decpt):
            print(f"There is a diiference in length of the files {raw_file} is {len(raw)} and {decrypt_file} is {len(decpt)}")

        min_len = min(len(raw), len(decpt))
        for i in range(min_len):
            if raw[i] != decpt[i]:
                print(f"There is difference in character {raw[i]} in {raw_file} and {decpt[i]} in {decrypt_file}")
        
        if raw == decpt:
            print(f"Both the files {raw_file} and {decrypt_file} are same.")
        else:
            print("File differs.")
    except FileNotFoundError as e:
        print(f"Error: {e}")



# Operations for the input of the shift value and content of the file.
def main():
    try:
        # Givin the shif value to shift the data 
        shift1 = int(input("Enter the first shift value: "))
        shift2 = int(input("Enter  the second shift value: "))      

        # Writing the content to be encrypted in the file raw_text.txt
        with open("raw_text.txt", 'r') as file:
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

        # Decrypting the content of the file 'encrypt_text.txt'.
        encrypted_line = enc_text.strip()
        decrypt_text = decrypt(encrypted_line, shift1, shift2)

        # writing the decrypted text in the file Decryption_text.txt 
        with open("Decryption_text.txt", 'w+') as file:
            file.write(decrypt_text)
            file.seek(0)
            decrypted_text = file.read()

        print("\n\n" + "The Decrypted text is: " + "\n")
        print(decrypted_text)
        print ("\n\n")
# Comparison of the texts in the file raw_text.txt and Decryption_text.txt
        file1 = "raw_text.txt"
        file2 = "Decryption_text.txt"
        compare(file1, file2)
        
    except FileNotFoundError as e:
        print("Error: {e}")
        

if __name__ == "__main__":
    main()