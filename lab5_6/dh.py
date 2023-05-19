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
    

