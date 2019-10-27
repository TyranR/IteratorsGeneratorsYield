import hashlib

def md5_func(mystring):
    """
    Принимает строку, возвращает её md5 хэш
    """
    print
    return hashlib.md5(mystring.encode('utf-8')).hexdigest()