import pandas as pd
import matplotlib.pyplot as plt


def plot_frequency():
    data = pd.read_excel("/home/ryon/code/python/MCM/data.xlsx")
    prevalency = data["Number of  reported results"]
    prevalency.plot().invert_xaxis()
    plt.show()

def count_words():
    data = pd.read_excel("/home/ryon/code/python/MCM/data.xlsx")
    words = data["Word"]
    vowels = {
        "a": 0, "e": 0, "i": 0, "o": 0, "u": 0
    }
    for word in words:
        for vowel in ("a", "e", "i", "o", "u"):
            vowels[vowel] += word.count(vowel)
    plt.bar(vowels.keys(), vowels.values())
    plt.show()

count_words()