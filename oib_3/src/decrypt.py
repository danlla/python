from gen_key import decryption_key
from cryptography.hazmat.primitives import padding as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def decryption(setting: dict, iv: bytes):
    """ Функция дешифрования текста симметричным ключом """

    with open(setting['symmetric_key'], mode='rb') as key_file:
        key = key_file.read()
    sym_key = decryption_key(setting, key)

    with open(setting['encrypted_file'], mode='rb') as encrypted_file:
        enc_text = encrypted_file.read()

    cipher = Cipher(algorithms.SEED(sym_key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    dc_text = decryptor.update(enc_text) + decryptor.finalize()
    unpad = pd.ANSIX923(128).unpadder()
    unpadded_text = unpad.update(dc_text) + unpad.finalize()
    res = unpadded_text.decode('UTF-8')

    with open(setting['decrypted_file'], mode='w') as dec_file:
        dec_file.write(res)
