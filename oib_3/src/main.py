from gen_key import generation_key, encryption_key
from encrypt import encryption
from decrypt import decryption
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
    with open('../settings.json', mode='w') as fp:
        json.dump(settings, fp)
    with open('../settings.json') as json_file:
        json_data = json.load(json_file)

    iv = os.urandom(16)

    while True:
        print("\ngenerate keys - g")
        print("encrypt text - e")
        print("decrypt text - d")
        print("escape - q")
        choice = input("Chose g,e,d or q: ")
        if choice == "g":
            generation_key(settings)
            encryption_key(settings)

        elif choice == "e":
            encryption(settings, iv)

        elif choice == "d":
            decryption(settings, iv)
        elif choice == "q":
            break
        else:
            print("not found")
