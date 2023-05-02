from Crypto.Cipher import AES
import base64
def encrypt_message(message):
    secret_key = b'mysecretkey12345'
    aes = AES.new(secret_key, AES.MODE_ECB)
    padded_message = message.encode('utf-8')
    padded_message += b"\0" * (AES.block_size - len(padded_message) % AES.block_size)
    encrypted_message = aes.encrypt(padded_message)
    return base64.b64encode(encrypted_message).decode()