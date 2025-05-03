from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
public_key = key.publickey()
encryptor = PKCS1_OAEP.new(public_key)
decryptor = PKCS1_OAEP.new(key)

message = "Hello RSA!"
rsa_encrypted = encryptor.encrypt(message.encode())
rsa_decrypted = decryptor.decrypt(rsa_encrypted).decode()

print("\n✅ RSA Encrypted:", rsa_encrypted)
print("✅ RSA Decrypted:", rsa_decrypted)
