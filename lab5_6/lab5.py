def power(a, b, p):
    if b == 1:
        return a % p
    else:
        return pow(a, b, p)

def dh_generatePublicKey(P, G, privateKey):
    publicKey = pow(G, privateKey, P)
    return publicKey

def dh_generateSecretKey(publicKey, privateKey, P):
    secretKey = pow(publicKey, privateKey, P)
    return secretKey

def main():
    P = 0; G = 0; x = 0; a = x
    y = 0; b = 0
    ka = 0; kb = 0

    # Both the users will be agreed upon the public keys G and P
    P = 23; # A prime number P is taken
    print("The value of P:", P)

    G = 9; # A primitive root for P, G is taken
    print("The value of G:", G)

    # Alice will choose the private key a
    a = 4; # a is the chosen private key
    print("The private key a for Alice:", a)

    x = dh_generatePublicKey(P,G,a)

    # Bob will choose the private key b
    b = 3; # b is the chosen private key
    print("The private key b for Bob:", b)

    y = dh_generatePublicKey(P,G,b)

    # Generating the secret key after the exchange of keys
    ka = dh_generateSecretKey(y,a,P)
    kb = dh_generateSecretKey(x,b,P)
    
    print("Secret key for the Alice is:", ka)
    print("Secret Key for the Bob is:", kb)

main()