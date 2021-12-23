from gen_key import decryption_key
from cryptography.hazmat.primitives import padding as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encryption(setting: dict, iv: bytes):
    """ Функция шифрования текста симметричным ключом """

    with open(setting['symmetric_key'], mode='rb') as key_file:
        key = key_file.read()
    ds_key = decryption_key(setting, key)

    with open(setting['initial_file'], mode='r', encoding='UTF-8') as file:
        res = file.read()

    pad = pd.ANSIX923(128).padder()
    text = bytes(res, 'UTF-8')
    padded_text = pad.update(text) + pad.finalize()
    cipher = Cipher(algorithms.SEED(ds_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(padded_text) + encryptor.finalize()

    with open(setting['encrypted_file'], 'wb') as encrypted_file:
        encrypted_file.write(encrypted_text)
