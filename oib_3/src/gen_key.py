import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def generation_key(settings):
    """ Функция для генерации ключей """

    symmetric_key = os.urandom(16)

    with open(settings['symmetric_key'], 'wb') as sym_key_file:
        sym_key_file.write(symmetric_key)

    asymmetric_keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = asymmetric_keys
    public_key = asymmetric_keys.public_key()

    public_pem = settings['public_key']
    with open(public_pem, 'wb') as public_out:
        public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                 format=serialization.PublicFormat.SubjectPublicKeyInfo))

    private_pem = settings['private_key']
    with open(private_pem, 'wb') as private_out:
        private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                    encryption_algorithm=serialization.NoEncryption()))


def encryption_key(settings):
    """ Функция шифрования симметричного ключа открытым ключом """

    with open(settings['symmetric_key'], 'rb') as key_file:
        symmetric_key = key_file.read()

    with open(settings['public_key'], 'rb') as pem_in:
        public_bytes = pem_in.read()
    public_key = load_pem_public_key(public_bytes)
    symmetric_enc_key = public_key.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                       algorithm=hashes.SHA256(),
                                                                       label=None))

    with open(settings['symmetric_key'], 'wb') as key_file:
        key_file.write(symmetric_enc_key)


def decryption_key(settings, symmetric_key):
    """ Функция дешифрования симметричного ключа закрытым ключом """

    with open(settings['private_key'], 'rb')as pem_in:
        private_bytes = pem_in.read()
    private_key = load_pem_private_key(private_bytes, password=None,)
    decrypted_sym_key = private_key.decrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                        algorithm=hashes.SHA256(),
                                                                        label=None))
    return decrypted_sym_key
