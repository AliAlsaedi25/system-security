def hill_cipher_encrypt(plain_text, key):

    #checking if the key is a string and 4 letters 
    check = isinstance(key,str)
    if check != True:
        print('please enter a string as the key')
        return
    if len(key) != 4:
        print('the key has to be 4 letters')
        return

    #convert the key into a matrix 
    key = key.upper()
    key = list(key)
    matrix = []
    for i in key:
        x = ord(i)
        x = (x - 65)%26
        matrix.append(x)

    top_matrix = matrix[:2]
    bottom_matrix = matrix[2:]
    key_matrix = []
    key_matrix.append(top_matrix)
    key_matrix.append(bottom_matrix)

    # Convert plaintext to uppercase and remove spaces
    plain_text = plain_text.replace(" ", "").upper()

    # If plaintext length is odd, append an 'X' to the end
    if len(plain_text) % 2 != 0:
        plain_text += 'X'

    # Initialize ciphertext
    cipher_text = ""

    # Create 2x2 matrix of plaintext pairs
    pairs = []
    for i in range(0, len(plain_text), 2):
        pair = [ord(plain_text[i]) - 65, ord(plain_text[i+1]) - 65]
        pairs.append(pair)

    # Multiply pairs by key matrix and convert to mod 26
    for pair in pairs:
        result = [0, 0]
        for i in range(2):
            for j in range(2):
                result[i] += pair[j] * key_matrix[i][j]
            result[i] = result[i] % 26

        # Convert back to letters and add to ciphertext
        cipher_text += chr(result[0] + 65) + chr(result[1] + 65)

    return cipher_text



def hill_cipher_decrypt(cipher_text, key):
    
    #checking if the key is a string and 4 letters 
    check = isinstance(key,str)
    if check != True:
        print('please enter a string as the key')
        return
    if len(key) != 4:
        print('the key has to be 4 letters')
        return

    #convert the key into a matrix 
    key = key.upper()
    key = list(key)
    matrix = []
    for i in key:
        x = ord(i)
        x = (x - 65)%26
        matrix.append(x)

    top_matrix = matrix[:2]
    bottom_matrix = matrix[2:]
    key_matrix = []
    key_matrix.append(top_matrix)
    key_matrix.append(bottom_matrix)

    # Convert ciphertext to uppercase and remove spaces
    cipher_text = cipher_text.replace(" ", "").upper()

    # Calculate inverse of key matrix modulo 26
    det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26
    det_inv = -1
    for i in range(26):
        if (i * det) % 26 == 1:
            det_inv = i
            break
    if det_inv == -1:
        raise ValueError("key_matrix is not invertible")

    key_matrix_inv = [[0, 0], [0, 0]]
    key_matrix_inv[0][0] = (key_matrix[1][1] * det_inv) % 26
    key_matrix_inv[0][1] = (-key_matrix[0][1] * det_inv) % 26
    key_matrix_inv[1][0] = (-key_matrix[1][0] * det_inv) % 26
    key_matrix_inv[1][1] = (key_matrix[0][0] * det_inv) % 26

    # Create 2x2 matrix of ciphertext pairs
    pairs = []
    for i in range(0, len(cipher_text), 2):
        pair = [ord(cipher_text[i]) - 65, ord(cipher_text[i+1]) - 65]
        pairs.append(pair)

    # Multiply pairs by key matrix inverse and convert to mod 26
    plain_text = ''
    for pair in pairs:
        result = [0, 0]
        for i in range(2):
            for j in range(2):
                result[i] += pair[j] * key_matrix_inv[i][j]
            result[i] = result[i] % 26

        # Convert back to letters and add to plaintext
        plain_text += chr(result[0] + 65) + chr(result[1] + 65)

    return plain_text


# Define the plaintext and key
plain_text = "hello everyone"
key = 'hill'

# Call the function
cipher_text = hill_cipher_encrypt(plain_text, key)

# Call the function
plain_text = hill_cipher_decrypt(cipher_text, key)

# Print the decrypted plaintext
print(plain_text) 
print(cipher_text)

