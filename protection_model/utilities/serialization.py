from struct import pack

def serialize_8_bit_int(n: int) -> bytes:
    """
        Serializes the given integer to an 8-bit integer in little-endian. 
    """
    return pack("<B", n) 
    
def serialize_16_bit_int(n: int) -> bytes:
    """
        Serializes the given integer to a 16-bit integer in little-endian. 
    """
    return pack("<H", n)   

def serialize_64_bit_int(n: int) -> bytes:
    """
        Serializes the given integer to a 64-bit integer in little-endian. 
    """
    return pack("<Q", n)

