import time
import base64
import hashlib
import sys
import secrets


class Block:
    def __init__(self, index, previous_hash, timestamp, encoded_transactions, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.encoded_transactions = encoded_transactions
        self.nonce = nonce

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.encoded_transactions}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()


def proof_of_work(previous_block, encoded_transactions):
    index = previous_block.index + 1
    timestamp = int(time.time())
    nonce = 0

    block = Block(index, previous_block.calculate_hash(),
                  timestamp, encoded_transactions, nonce)

    while not is_valid_proof(block):
        nonce += 1
        block.nonce = nonce

    return block


def is_valid_proof(block):
    guess_hash = block.calculate_hash()
    return guess_hash[:2] == "00"


def decode_transactions(encoded_transactions):
    return base64.b64decode(encoded_transactions).decode('utf-8')


def get_all_blocks(blockchain):
    return blockchain


def blockchain_to_string(blockchain):
    block_strings = [f"{block.calculate_hash()}" for block in blockchain]
    return '-'.join(block_strings)


def encrypt(plaintext, inner_txt, key):
    midpoint = len(plaintext) // 2

    first_part = plaintext[:midpoint]
    second_part = plaintext[midpoint:]
    modified_plaintext = first_part + inner_txt + second_part
    block_size = 16
    plaintext = pad(modified_plaintext, block_size)
    key_hash = hashlib.sha256(key).digest()

    ciphertext = b''

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        cipher_block = xor_bytes(block, key_hash)
        ciphertext += cipher_block

    return ciphertext


def pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length)
    return data.encode() + padding





def generate_random_string(length):
    return secrets.token_hex(length // 2)


random_string = generate_random_string(64)


def main(token):
    key = bytes.fromhex(random_string)

    print("Key:", key)

    genesis_block = Block(0, "0", int(time.time()), "EncodedGenesisBlock", 0)
    blockchain = [genesis_block]

    for i in range(1, 5):
        encoded_transactions = base64.b64encode(
            f"Transaction_{i}".encode()).decode('utf-8')
        new_block = proof_of_work(blockchain[-1], encoded_transactions)
        blockchain.append(new_block)

    all_blocks = get_all_blocks(blockchain)

    blockchain_string = blockchain_to_string(all_blocks)
    encrypted_blockchain = encrypt(blockchain_string, token, key)

    print("Encrypted Blockchain:", encrypted_blockchain)


if __name__ == "__main__":
    text = sys.argv[1]
    main(text)

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def decrypt(ciphertext, token_length, key):
    """
    Decrypt the ciphertext using the same key and block size as encryption.
    Removes the inserted token and padding.
    """
    block_size = 16
    key_hash = hashlib.sha256(key).digest()
    
    # Decrypt blocks
    plaintext = b''
    for i in range(0, len(ciphertext), block_size):
        cipher_block = ciphertext[i:i + block_size]
        block = xor_bytes(cipher_block, key_hash)
        plaintext += block
    
    # Remove padding
    padding_length = plaintext[-1]
    plaintext = plaintext[:-padding_length]
    
    # Convert to string
    decrypted_text = plaintext.decode()
    
    # Remove inserted token
    midpoint = (len(decrypted_text) - token_length) // 2
    original_text = decrypted_text[:midpoint] + decrypted_text[midpoint + token_length:]
    
    return original_text

# Modified main function to use the provided data
def main():
    key = b'\x8e\xdc\x08\xb8S\xee6\x0c\xf5\xfd\xceP\x15\xbf\xf6\xe2\x90\xf3\xd7F?,!\x1c\xb0D\x0cO\xcc\x04q\xb8'
    encrypted_blockchain = b"\xb4\xc8\xbd\xec@A\xbd-\x1d\xfd\x16\xe1\xe3sW\x18\xb1\x99\xea\xb8\x15\x10\xe8{\x19\xacE\xb3\xb4w\nH\xe7\x9d\xea\xe9EC\xb9(N\xa8\x14\xe1\xb7t]\x1c\xb7\xc8\xb9\xbaAF\xea}L\xadF\xb4\xb1&\n\x19\xac\xcc\xbc\xedGI\xef~\x16\xab\x10\xb6\xb7'\x0cN\xe0\xca\xee\xba\x15D\xbcz\x17\xfa\x17\xe3\xe0sY\x14\xe5\xca\xb5\xecAB\xea{\x1e\xffD\xe4\xb0%\x0cO\xb0\xc9\xee\xefC\x12\xeb|N\xff\x16\xe8\xb4'[\x15\xe0\xd1\xbc\xec\x10F\xe8q\x17\xa8\x10\xe1\xedu\\N\xb6\xc5\xef\xba\x10@\xe8y\x1a\xadC\xe3\xb0p\nO\xb0\xce\xfc\xb5\x15\x1e\xcd\x1di\xb5B\xbc\xba \x05s\xb2\xaf\xde\xb4 \x18\xdc+{\xffQ\xb3\x8d\x1c6y\xeb\xb1\xbc\xaeBH\xed\x01p\xbfc\xaa\xb8\t4V\xc3\xb7\xd3\xe8G\x12\xbfy\x1c\xfd\x11\xad\xe4r\\\x1f\xb5\xc8\xbf\xeeCC\xefy\x18\xadC\xb1\xe3uXM\xe7\xc4\xe9\xeb\x17\x12\xeb{\x1b\xf7\x15\xb6\xf8s^\x1c\xe7\xca\xba\xe5\x10A\xb8-\x18\xffA\xe4\xe7u]J\xb1\xcf\xb9\xef\x12C\xbd+L\xfd\x19\xe6\xed'XN\xe0\xcf\xe9\xef\x17@\xbczI\xa8\x18\xb1\xe1vV\x1d\xe5\xcb\xbf\xec\x12\x15\xec|L\xabD\xb4\xb0n^\x1c\xb8\x98\xea\xea\x10A\xec/\x1c\xfa\x17\xb6\xecp\x08J\xb9\xc4\xed\xeb\x10\x17\xb6+\x1c\xf6\x11\xe5\xe0s\x0bI\xe3\xca\xb9\xbaGH\xb6}\x18\xf7A\xe0\xe5{X\x1f\xb4\x99\xe9\xbe@H\xbf*I\xfd\x14\xb6\xe7 l."

    import re

    # Try to decrypt with different token lengths
    for token_length in range(1, 50):  # Try reasonable token lengths
        try:
            decrypted = decrypt(encrypted_blockchain, token_length, key)
            # Search for picoCTF{...} pattern
            flag_match = re.search(r'picoCTF{[^}]*}', decrypted)
            if flag_match:
                print(flag_match.group(0))
                  # Exit once we find the flag
        except Exception as e:
            continue

    print("\nNo flag found in any decryption attempt")

if __name__ == "__main__":
    main()