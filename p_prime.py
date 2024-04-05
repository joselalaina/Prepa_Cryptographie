import random

def is_prime_rabin_miller(n, k=50):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # Décomposer n - 1 en (2^r) * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Effectuer k itérations du test de Rabin-Miller
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # N'est pas premier
    
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  # Assurer le bit le plus significatif et le moins significatif à 1
        if is_prime_rabin_miller(num):
            return num

n_bits = 1024
prime = generate_prime(n_bits)
print(f"Nombre premier de {n_bits} bits : {prime}")