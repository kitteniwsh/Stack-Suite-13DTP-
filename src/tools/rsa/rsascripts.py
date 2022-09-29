from Cryptodome.Util.number import long_to_bytes, bytes_to_long, inverse
import owiener
from Cryptodome.PublicKey import RSA
import gmpy2

import func_timeout


def decr(c):
    """Takes a integer c and converts to bytes format"""
    try:
        return long_to_bytes(c)
    except:
        # Incorrect type or c does not decode properly
        return "Malformed input"


def ntfermat(f, max_wait):
    """
    Takes in arguments [f] and max wait time.
    Runs fermatfactor with arguements [f] for a maximum of max_wait seconds
    Will return "" if timed out
    """
    try:
        return func_timeout.func_timeout(max_wait, fermatfactor, args=[f])
    except func_timeout.FunctionTimedOut:
        pass
    return ""


def hexx(n):
    """
    Takes in a decimal integer n and converts to hexadecimal
    Will return Malformed input if incorrect chars are used
    """
    if(type(n) == int):
        return hex(n)

    if(type(n) == str):
        try:
            # Convert to bytes, and then to hexadecimal
            return n.encode('utf-8').hex()
        except:
            return "Malformed input"
    else:
        return "Malformed input"


def enc(m):
    """Takes in a str(m), and converts to a decimal integer"""
    try:
        return bytes_to_long(m.encode())
    except:
        return "Malformed input"


def iroot(k, n):
    """
    Fast integer root algorithm
    Returns n root k
    """
    x, y = n, n + 1
    while x < y:
        y = x
        z = (k - 1) * y + (n // pow(y, k - 1))
        x = z // k
    return x


def parseHex(x):
    """
    Returns x if x is a decimal integer
    Converts x to decimal if x is a hexadecimal integer
    Returns Malformed input if no input is provided, or a invalid string. 
    """
    if(x is None):
        return "Malformed input"
    if (type(x) == str):
        if(x[:2] == "0x"):
            try:
                return int(x, 16)
            except ValueError:
                return "Malformed input"
        else:
            try:
                return int(x)
            except ValueError:
                return "Malformed input"
    else:
        return x


def rsaEncrypt(n, e, m):
    """
    Input:
    Public modulus n
    Public exponent e
    Message to be encrypted

    Output:
    Rsa encrypted decimal integer of the message
    """
    n, e = (parseHex(i) for i in [n, e])
    if("Malformed input" in (n, e)):
        return "Malformed input"
    c = enc(m)
    return pow(c, e, n)


def rsaDecrypt(n, d, c):
    """
    Input:
    Private exponent d
    Public modulus n
    Ciphertext

    Output:
    Decrypted ciphertext (ascii)
    """
    n, d, c = [parseHex(i) for i in [n, d, c]]
    print(n, d, c)
    if("Malformed input" in (n, d, c)):
        return "Malformed input"
    m = pow(c, d, n)
    return decr(m)


def totFromPQ(p, q, e):
    """
    Input:
    Primes P and Q
    Public exponent e

    Output:
    Carmichael's totient function on p, q and e

    """
    p, q, e = [parseHex(i) for i in [p, q, e]]
    if("Malformed input" in (p, q, e)):
        return "Malformed input"
    phi = (p - 1) * (q - 1)
    return inverse(e, phi)


def minuteE(e, c, n):
    """
    returns m when the encrypted message is less than modulus
    This is because it doesnt wrap around, so a simple cube root works
    """

    e, c, n = [parseHex(i) for i in [e, c, n]]
    if("Malformed input" in (n, e, c)):
        return "Malformed input"
    try:
        assert e == 3
        assert pow(c, e) < n

    except AssertionError:
        return ""

    m = iroot(3, c)
    return decr(m)


def wiener(e, n, c):
    """
    Performs wieners attack on e, n and c
    My implementation was a bit too slow, so I used an optimized one
    from the owiener library
    """
    e, n, c = [parseHex(i) for i in [e, n, c]]
    if("Malformed input" in (n, e, c)):
        return "Malformed input"
    d = owiener.attack(e, n)
    if d:
        return rsaDecrypt(n, d, c)
    else:
        return ""


def fermatfactor(n):
    """
    Attempts to factor N using fermat factorization
    """
    n = parseHex(n)
    if("Malformed input" in [n, ""]):
        return "Malformed input"
    a = gmpy2.isqrt(n) + 1
    b = a * a - n
    while not gmpy2.is_square(b):
        a = a + 1
        b = a * a - n
    b = gmpy2.isqrt(b)
    return (int(a + b), int(a - b))


def pemmish(x):
    """returns n, e, p, q, d as applicable"""
    if(x is not None):
        try:
            pk = RSA.importKey(x)
        except ValueError or TypeError:
            return "Incorrect format"
        if(pk.has_private()):
            return [pk.n, pk.e, pk.p, pk.q, pk.d]
        else:
            return [pk.n, pk.e]
    else:
        return "Awaiting input"
