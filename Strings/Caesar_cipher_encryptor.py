# Caesar cipher encryptor

def caesarCipherEncryptor(string, key):
    lst = list(string)
    unicode_plus_key, output = [], []
	
    for i, s in enumerate(string):
        unicode_plus_key.append(ord(s)+key % 26)
        output.append(chr(unicode_plus_key[i]))
    return ''.join(output)	
