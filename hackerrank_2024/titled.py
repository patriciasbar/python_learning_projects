import re 
def solve(s):
    s_titled = " ".join([letter.title() if letter.isalpha() else letter for letter in re.split("\s|\s\s?", s)])
    return s_titled
