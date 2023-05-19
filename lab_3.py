def encrypt_text(inputText, N, D):
    # Define valid characters
    valid_chars = set(chr(i) for i in range(34, 127)) - set([" ", "!"])

    # Reverse input text
    inputText = inputText[::-1]

    # Shift characters by N positions
    encrypted_text = ""
    for char in inputText:
        if char in valid_chars:
            char_code = ord(char)
            char_code -= 34
            char_code += N * D
            char_code %= len(valid_chars)
            char_code += 34
            encrypted_text += chr(char_code)
        else:
            encrypted_text += char

    return encrypted_text

def testCustomEncrypt():
    #getting the user id 
    user_id = input('Input a UserID (that does not include "space" or "!" they will not be encrypted): ')

    #getting theuser password
    user_password = input('Input a password (that does not include "space" or "!" they will not be encrypted): ')

    #seting n value (must be greater than 1)
    N_value = input('Please enter an N value (N must be >=1): ')
    N_value = int(N_value)
    while N_value < 1:
        N_value = input('Please enter an N value (N must be >=1): ')
        N_value = int(N_value)

    #setting d value (must be 1 or -1)
    D_value = input('Please enter an D value (D must be +1 or -1): ')
    D_value = int(D_value)
    while D_value not in [1,-1]:
       D_value = input('Please enter an D value (D must be +1 or -1): ')
       D_value = int(D_value)
    
    # encrypt username
    encrypted_user_id = encrypt_text(user_id,N_value,D_value)

    # encrypt password
    encrypted_password = encrypt_text(user_password,N_value,D_value)

    #displaying the encrypted and original username and password 
    print('encrypted UserID: ' + encrypted_user_id)
    print('encrypted Password: ' + encrypted_password)
    print('original UserID: ' + user_id)
    print('original Password: ' + user_password)


testCustomEncrypt()
