import string
import random
import os


class Encryption:
    def __init__(self, obj):
        self.phrase = obj

    def encrypt(self):
        y = list(map(str, self.phrase))
        encrypted_message = ""
        a = []
        with open("key.txt", "r") as FILE:
            lines = FILE.readlines()
            for line in lines:
                if line.startswith("=="):
                    x = line.split("=")
                    x = [s.replace("\n", "") for s in x]
                    x[0] = "="
                    x.pop(1)
                    a.append(x)
                else:
                    x = line.split("=")
                    x = [s.replace("\n", "") for s in x]
                    a.append(x)
        for i in y:
            for x in a:
                if i == x[0]:
                    encoded_letter = x[1]
                    encrypted_message += encoded_letter
        return encrypted_message


class Decryption:
    def __init__(self, msg: str, length: int):
        self.phrase = msg
        self.length = length

    def decrypt(self):
        x = [
            " ".join(
                self.phrase[i : i + self.length]
                for i in range(0, len(self.phrase), self.length)
            )
        ]
        x = x[0].split(" ")
        decrypted_message = ""
        a = []
        with open("key.txt", "r") as FILE:
            lines = FILE.readlines()
            for line in lines:
                if line.startswith("=="):
                    k = line.split("=")
                    k = [s.replace("\n", "") for s in k]
                    k[0] = "="
                    k.pop(1)
                    a.append(k)
                else:
                    k = line.split("=")
                    k = [s.replace("\n", "") for s in k]
                    a.append(k)
        for i in x:
            for element in a:
                if i == element[1]:
                    decrypted_letter = element[0]
                    decrypted_message += decrypted_letter
        if len(decrypted_message) == 0:
            pass
        else:
            return decrypted_message


def rnd(x):
    return "".join(
        random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase, k=x
        )
    )


def writefile():
    alphabets = string.ascii_letters
    numbers = string.digits
    punctuation = string.punctuation
    with open("key.txt", "w") as FILE:
        for i in alphabets:
            FILE.write(f"{i}={str(rnd(10))}\n")
        for i in numbers:
            FILE.write(f"{i}={str(rnd(10))}\n")
        for i in punctuation:
            FILE.write(f"{i}={str(rnd(10))}\n")
        FILE.write(f"={str(rnd(10))}\n")


try:
    with open("key.txt") as f:
        if os.stat("key.txt").st_size == 0:
            writefile()
            print("New Key Created")
        else:
            pass
except IOError:
    file = open("key.txt", "x")
    writefile()
    print("New Key Created")
