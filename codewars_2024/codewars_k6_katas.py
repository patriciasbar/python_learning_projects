from collections import Counter

def spin_words(sentence):
    reversed_sentence = ""
    reversed_sentence += "".join(" ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split()]))
    return reversed_sentence.strip()


def who_likes_it(names):
    if len(names) == 0:
        return f"no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


def find_it(seq):
    count_numbers = Counter(seq)
    for key, value in count_numbers.items():
        if value % 2 != 0:
            return key
        







