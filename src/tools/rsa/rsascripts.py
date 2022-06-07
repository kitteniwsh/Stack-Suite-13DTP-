from Cryptodome.Util.number import long_to_bytes, bytes_to_long, inverse
import owiener
from Cryptodome.PublicKey import RSA
import base64

def decr(c):
    try:
        return long_to_bytes(c)
    except:
        return "Malformed input"

def hexx(n):
    if(type(n)==int):
        return hex(n)
    if(type(n)==str):
        try:
            return n.encode('utf-8').hex()
        except:
            return "Bad input"
    else:
        return "Malformed input"


def enc(m):
    try:
        return bytes_to_long(m.encode())
    except:
        return "Malformed input"
def iroot(k, n):
        x, y = n, n + 1
        while x < y:
            y = x
            z = (k - 1) * y + (n // pow(y, k - 1))
            x = z // k
        return x

def parseHex(x):
    if(x is None):
        return "Malformed input"
    if (type(x) == str ):
        if( x[:2] == "0x"):
            return int(x, 16)
        else:
            try:
                return int(x)
            except:
                return "Malformed input"
    else:
        return x
def rsaEncrypt(n, e, m):
    n, e = (parseHex(i) for i in [n, e])
    if("Malformed input" in (n, e)):
       return "Malformed input"
    c = enc(m)
    return pow(c, e, n)

def rsaDecrypt(n, d, c):
    n, d, c = [parseHex(i) for i in [n, d, c]]
    print(n, d, c)
    if("Malformed input" in (n, d, c)):
       return "Malformed input"
    m = pow(c, d, n)
    return decr(m)

def totFromPQ(p, q, e):
    p, q, e = [parseHex(i) for i in [p, q, e]]
    if("Malformed input" in (p, q, e)):
       return "Malformed input"
    phi = (p - 1) * (q - 1)
    return inverse(e, phi)

def minuteE(e, c, n):
    e, c, n = [parseHex(i) for i in [e, c, n]]
    """ returns m when the encrypted message is less than modulus"""
    if("Malformed input" in (n, e, c)):
       return "Malformed input"
    try:
        assert pow(c, e) < n
        assert e ==3
    except AssertionError:
        return "Attack not applicable"
    
    m = iroot(3, c)
    return decr(m)
def wiener(e, n, c):
    e, n, c= [parseHex(i) for i in [e, n, c]]
    if("Malformed input" in (n, e, c)):
       return "Malformed input"
    d = owiener.attack(e, n)
    if d:
        return rsaDecrypt(n, d, c)
    else:
        return "Attack not applicable"


def pemmish(x):
    """returns n, e, p, q, d as applicable"""
    try:
        pk = RSA.importKey(x)
    except ValueError or TypeError:
        return "Incorrect format"
    if(pk.has_private()):
        return [pk.n, pk.e, pk.p, pk.q, pk.d]
    else:
        return [pk.n, pk.e]
