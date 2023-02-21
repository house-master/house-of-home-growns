import bcrypt

def generate_hash(input: str) -> bytes:
    bytes = input.encode('utf-8')
    # generating the salt
    salt = bcrypt.gensalt()

    # Hashing the password
    return bcrypt.hashpw(bytes, salt)



def verify(hash: bytes, input: str) -> bool:
    # encoding user password
    input_bytes = input.encode('utf-8')

    # checking password
    return bcrypt.checkpw(input_bytes, hash)

