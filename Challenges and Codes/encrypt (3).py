import math
import random

def long_to_bytes(n):
    if n == 0:
        return b'\x00'
    
    bytearray_result = bytearray()
    while n > 0:
        bytearray_result.append(n & 0xFF)
        n >>= 8
    
    return bytes(reversed(bytearray_result))

def inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    
    x = random.randint(1, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1
    
    # Define the function f(x) = (x^2 + c) % n
    f = lambda x: (x*x + c) % n
    
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
        
        if d == n:
            # Failed with these values, try again with new random values
            return pollard_rho(n)
    
    return d

def factor_n(N):
    """
    Factor N into its prime components p and q
    Try multiple factorization methods
    """
    # Try Pollard's rho algorithm
    try:
        p = pollard_rho(N)
        if p > 1 and N % p == 0:
            q = N // p
            return p, q
    except:
        pass
    
    # Try Fermat's factorization for completeness
    try:
        a = math.isqrt(N)
        b_squared = a*a - N
        
        # Limit iterations to prevent infinite loops
        max_iterations = 1000000
        iterations = 0
        
        while not is_perfect_square(b_squared) and iterations < max_iterations:
            a += 1
            b_squared = a*a - N
            iterations += 1
            
        if iterations < max_iterations:
            b = math.isqrt(b_squared)
            p = a + b
            q = a - b
            return p, q
    except:
        pass
    
    raise Exception("Factorization failed. For a real 1024-bit RSA key, this is expected.")

def is_perfect_square(n):
    """Check if n is a perfect square"""
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n

def decrypt_rsa(N, e, ciphertext):
    """
    Decrypt an RSA encrypted message given N, e, and the ciphertext
    """
    # Factor N to find p and q
    p, q = factor_n(N)
    
    # Calculate phi(N) = (p-1)*(q-1)
    phi = (p-1) * (q-1)
    
    # Calculate private key d = e^(-1) mod phi(N)
    d = inverse(e, phi)
    
    # Decrypt ciphertext: m = c^d mod N
    m = pow(ciphertext, d, N)
    
    # Convert number back to text
    try:
        plaintext = long_to_bytes(m).decode('utf-8')
    except UnicodeDecodeError:
        plaintext = f"[Binary data, hex representation: {long_to_bytes(m).hex()}]"
    
    return plaintext

# Example usage
if __name__ == "__main__":
    N = 20297080746551533950310171063102208111516251367018322047128542764704356415306577127576303893333842168411485207194989908528743415017887992425345647451800774
    e = 65537
    ciphertext = 9146089830084942925221152758612027866026085373842283757646651044500815408085968114062147076487868133416785202942565616220750286233916498696594067493760619
    
    try:
        plaintext = decrypt_rsa(N, e, ciphertext)
        print(f"Decrypted message: {plaintext}")
    except Exception as ex:
        print(f"Decryption failed: {ex}")
        print("For a real 1024-bit RSA key, factorization would require advanced methods.")