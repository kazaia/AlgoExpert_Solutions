# Caesar cipher encryptor

def caesarCipherEncryptor(string, key):
	key = key % 26
    lst = list(string)
    unicode_plus_key, output = [], []
	
    for i, s in enumerate(string):
		new_code = ord(s)+key
		if new_code < 123:
			unicode_plus_key.append(new_code)
		else:
			unicode_plus_key.append(96 + new_code % 122)
        output.append(chr(unicode_plus_key[i]))
    return ''.join(output)	
	
	
