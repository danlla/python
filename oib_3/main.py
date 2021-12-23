import json
import os

if __name__ == '__main__':
    settings = {
        'initial_file': 'text.txt',
        'encrypted_file': 'encrypted.txt',
        'decrypted_file': 'decrypted.txt',
        'symmetric_key': 'symmetric_key.txt',
        'public_key': 'public_key.pem',
        'private_key': 'private_key.pem',

    }
    with open('settings.json', 'w') as fp:
        json.dump(settings, fp)
    with open('settings.json') as json_file:
        json_data = json.load(json_file)

    iv = os.urandom(16)

    while True:
        print("generate keys - k")
        print("encrypt text - e")
        print("decrypt text - d")
        ch = input("Chose k,e or d ")
        if ch == "k":
            generation_key(settings, 16)
            encryption_key(settings)
            break

        elif ch == "e":
            encryption(settings, iv)

        elif ch == "d":
            decryption(settings, iv)
        else:
            print("Not found")