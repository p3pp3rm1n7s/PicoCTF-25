import base64
import hashlib

def xor_bytes(a, b):
    # Make sure b is long enough by repeating it
    b_extended = b * (len(a) // len(b) + 1)
    b_extended = b_extended[:len(a)]
    return bytes(x ^ y for x, y in zip(a, b_extended))

def unpad(padded_data):
    try:
        padding_length = padded_data[-1]
        if padding_length > 0 and padding_length <= 16:
            return padded_data[:-padding_length]
    except IndexError:
        pass
    return padded_data

# Use the ACTUAL KEY from the file
key = b'\x8e\xdc\x08\xb8S\xee6\x0c\xf5\xfd\xceP\x15\xbf\xf6\xe2\x90\xf3\xd7F?,!\x1c\xb0D\x0cO\xcc\x04q\xb8'

# Use direct byte representation instead of reading from file
encrypted_data = b"\xb4\xc8\xbd\xec@A\xbd-\x1d\xfd\x16\xe1\xe3sW\x18\xb1\x99\xea\xb8\x15\x10\xe8{\x19\xacE\xb3\xb4w\nH\xe7\x9d\xea\xe9EC\xb9(N\xa8\x14\xe1\xb7t]\x1c\xb7\xc8\xb9\xbaAF\xea}L\xadF\xb4\xb1&\n\x19\xac\xcc\xbc\xedGI\xef~\x16\xab\x10\xb6\xb7'\x0cN\xe0\xca\xee\xba\x15D\xbcz\x17\xfa\x17\xe3\xe0sY\x14\xe5\xca\xb5\xecAB\xea{\x1e\xffD\xe4\xb0%\x0cO\xb0\xc9\xee\xefC\x12\xeb|N\xff\x16\xe8\xb4'[\x15\xe0\xd1\xbc\xec\x10F\xe8q\x17\xa8\x10\xe1\xedu\\N\xb6\xc5\xef\xba\x10@\xe8y\x1a\xadC\xe3\xb0p\nO\xb0\xce\xfc\xb5\x15\x1e\xcd\x1di\xb5B\xbc\xba \x05s\xb2\xaf\xde\xb4 \x18\xdc+{\xffQ\xb3\x8d\x1c6y\xeb\xb1\xbc\xaeBH\xed\x01p\xbfc\xaa\xb8\t4V\xc3\xb7\xd3\xe8G\x12\xbfy\x1c\xfd\x11\xad\xe4r\\\x1f\xb5\xc8\xbf\xeeCC\xefy\x18\xadC\xb1\xe3uXM\xe7\xc4\xe9\xeb\x17\x12\xeb{\x1b\xf7\x15\xb6\xf8s^\x1c\xe7\xca\xba\xe5\x10A\xb8-\x18\xffA\xe4\xe7u]J\xb1\xcf\xb9\xef\x12C\xbd+L\xfd\x19\xe6\xed'XN\xe0\xcf\xe9\xef\x17@\xbczI\xa8\x18\xb1\xe1vV\x1d\xe5\xcb\xbf\xec\x12\x15\xec|L\xabD\xb4\xb0n^\x1c\xb8\x98\xea\xea\x10A\xec/\x1c\xfa\x17\xb6\xecp\x08J\xb9\xc4\xed\xeb\x10\x17\xb6+\x1c\xf6\x11\xe5\xe0s\x0bI\xe3\xca\xb9\xbaGH\xb6}\x18\xf7A\xe0\xe5{X\x1f\xb4\x99\xe9\xbe@H\xbf*I\xfd\x14\xb6\xe7 l."

print("Key length:", len(key))
print("Encrypted data length:", len(encrypted_data))

# Try different hash functions
for hash_func in [hashlib.sha256, hashlib.sha1, hashlib.md5]:
    print(f"\nTrying {hash_func.__name__} hash function...")
    key_hash = hash_func(key).digest()
    
    # Try both padded and unpadded decryption
    for do_unpad in [True, False]:
        try:
            decrypted_data = xor_bytes(encrypted_data, key_hash)
            
            if do_unpad:
                decrypted_data = unpad(decrypted_data)
            
            # Try both UTF-8 and ASCII decoding
            for encoding in ['latin-1', 'utf-8', 'ascii']:
                try:
                    decrypted_str = decrypted_data.decode(encoding, errors='ignore')
                    
                    if 'picoCTF{' in decrypted_str:
                        print(f"Successfully decoded with {encoding} encoding!")
                        start_idx = decrypted_str.find('picoCTF{')
                        end_idx = decrypted_str.find('}', start_idx)
                        if end_idx > start_idx:
                            flag = decrypted_str[start_idx:end_idx+1]
                            print(f"FOUND FLAG: {flag}")
                        else:
                            # Print the whole chunk around picoCTF{
                            print(f"PARTIAL FLAG: {decrypted_str[start_idx:start_idx+50]}")
                            
                            # Print raw ASCII values of characters after picoCTF{block_
                            if "block_" in decrypted_str[start_idx:start_idx+50]:
                                block_pos = decrypted_str.find("block_", start_idx) + 6
                                print("Characters after 'block_':")
                                for i in range(20):
                                    if block_pos + i < len(decrypted_str):
                                        char = decrypted_str[block_pos + i]
                                        print(f"{i}: '{char}' (ASCII: {ord(char)})")
                        
                except UnicodeDecodeError:
                    continue
        except Exception as e:
            print(f"Error: {e}")