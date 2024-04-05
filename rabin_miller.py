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

n =  46099
test = is_prime_rabin_miller(n)
print(f"Nombre {n} est premier  : {test}")