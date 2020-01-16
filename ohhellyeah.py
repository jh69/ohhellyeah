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


def createword(worddict):
    if randint(0, 100) > worddict["probability"]:
        return ""
    returnthis = ""
    for char in worddict["characters"]:
        if len(char[0]) > 1:
            if randint(0, 100) < char[1]:
                returnthis += char[0]
        else:
            if char[1] > 89:
                returnthis += char[0]
            while randint(0, 100) < char[1]:
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
    if randint(0, 100) < 75:
        punctuation = "!"
        while randint(0, 100) < 90:
            result += punctuation

    if randint(0, 100) < 50:
        result = result.upper()
    return result


while True:
    print(ohhellyeahbaby(words))
    time.sleep(1)
