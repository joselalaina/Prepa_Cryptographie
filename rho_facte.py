import random

lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


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


def bezout(a, b):
    s, t, u, v = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, s, t, b, u, v = b, u, v, a - q * b, s - q * u, t - q * v
    return (a, s, t) if a>0 else (-a, -s, -t)

def pollard_rho(n: int):
    
    f_ = lambda z, n: (z*z + 1)%n
    y, x, d = 1, 1, 1
    while d==1:
        x = f_(x, n)
        y = f_(f_(y, n), n)
        if x-y!=0:
            d = bezout(n, (x-y)%n)[0]

    return d

def factor(n:int):

    k, l, m, o = 0, 0, 0, 0

    while n%2==0 and n>2:
        n //= 2
        k += 1

    while n%3==0 and n>3:
        n //= 3
        l += 1

    while n%5==0 and n>5:
        n //= 5
        m += 1

    while n%7==0 and n>7:
        n //= 7
        o += 1

    if (n in lowPrimes) or (n>60 and is_prime_rabin_miller(n, 50)):
        return "2*"*k + "3*"*l + "5*"*m + "7*"*o + f"{n}"
    p = pollard_rho(n)
    n //= p
    return f'{p}*' + "2*"*k + "3*"*l + "5*"*m + "7*"*o + factor(n)

print(factor(29419067978592848576612174))
