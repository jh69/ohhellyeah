import time
from random import randint

words = [
    {"probability": 99, "characters": [("o", 95), ("h", 80)]},
    {
        "probability": 90,
        "characters": [("hell ", 95), ("y", 95), ("e", 94), ("a", 90), ("h", 80)],
    },
    {"probability": 80, "characters": [("baby", 101), ("y", 60)]},
]


def r(rnd=100):
    return randint(0, rnd)


def createword(worddict):
    if r() > worddict["probability"]:
        return ""
    returnthis = ""
    for char in worddict["characters"]:
        if len(char[0]) > 1:
            if r() < char[1]:
                returnthis += char[0]
        else:
            if char[1] > 89:
                returnthis += char[0]
            while r() < char[1]:
                returnthis += char[0]
    return returnthis


def ohhellyeahbaby(wordsdict):
    results = []
    for word in wordsdict:
        results.append(createword(word))

    result = " ".join(results).strip()
    while "  " in result:
        result = result.replace("  ", " ")

    punctuation = "."
    if r() < 75:
        punctuation = "!"
        while r() < 90:
            result += punctuation

    if r() < 50:
        result = result.upper()
    return result


while True:
    print(ohhellyeahbaby(words))
    time.sleep(1)
