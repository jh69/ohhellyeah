import time
from random import randint

words = [
    {"prob": 99, "chars": [("o", 95), ("h", 90)]},
    {"prob": 90, "chars": [("hell", 101), ("l", 90)]},
    {"prob": 95, "chars": [("yeah", 101), ("y", 95), ("e", 94), ("a", 90), ("h", 80)]},
    {"prob": 80, "chars": [("baby", 101), ("y", 60)]},
]


def r(rnd=100):
    return randint(0, rnd)


def createword(worddict):
    if r() > worddict["prob"]:
        return ""
    returnthis = ""

    for char in worddict["chars"]:
        if len(char[0]) > 1:
            if r() < char[1]:
                returnthis += char[0]
        else:
            while r() < char[1]:
                returnthis += char[0]
    return returnthis


def ohhellyeahbaby(wordsdict):
    result = " ".join([createword(word) for word in wordsdict]).strip()

    while "  " in result:
        result = result.replace("  ", " ")

    punctuation = "."
    if r() < 75:
        punctuation = "!"

    while r() < 90:
        result += punctuation

    if r() < 40:
        result = result.upper()

    return result


while True:
    print(ohhellyeahbaby(words))
    time.sleep(1)
