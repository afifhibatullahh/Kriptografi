def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modulo invers tidak ada
    else:
        return x % m


# mengembalikan cipher teks
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26)
                        + ord('A')) for t in text.upper().replace(' ', '')])


# mengembalikan plainteks
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1]))
                         % 26) + ord('A')) for c in cipher])


def main():
    text = ''
    with open('plainteks.txt', 'r') as file:
        for sentence in file:
            text += sentence

    m = int(input('Masukan nilai m : '))
    n = int(input('Masukan nilai n : '))
    key = [m, n]

    # memanggil encryption function
    affine_encrypted_text = affine_encrypt(text, key)
    with open('cipherteks.txt', 'w') as file:
        file.write(affine_encrypted_text)

    print('Encrypted Text: {}'.format(affine_encrypted_text))


    # memanggil decryption function
    cipherteks = ""
    with open('cipherteks.txt', 'r') as file:
        for sentence in file:
            cipherteks += sentence

    affine_decrypted_text = affine_decrypt(cipherteks, key)
    print('Decrypted Text: {}'.format(affine_decrypted_text))

    with open('dekripteks.txt', 'w') as file:
        file.write(affine_decrypted_text)


if __name__ == '__main__':
    main()