def digitize(n):
    digits_list = []
    if isinstance(n, int) and n >= 0:
        n = str(n)
        digits_list = [int(digit) for digit in n[::-1]]
        return digits_list


def sort_gift_code(code):
    code_list = []
    if isinstance(code, str) and len(code) <= 26:
        code_list = [letter for letter in code]
        sorted_code = "".join(letter for letter in sorted(code_list))
        return sorted_code
    else:
        return f"Invalid Input"
    

def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i += 1
    return res


def build_string(*args):
    return "I like {0}!".format(",".join(args))


def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) // 3
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"


def get_count(sentence):
    vowels = "aeiou"
    vowel_count = 0
    for letter in sentence:
        if letter.lower() in vowels:
            vowel_count += 1
    return vowel_count


def stringy(size):
    string = ""
    if isinstance(size, int):
        if size == 0:
            return "0"
        else:
            for _ in range(1, size):
                if string.endswith("0"):
                    string += "1"
                else:
                    string += "0"
            return string


def two_decimal_places(number):
    return f"{number:.3f}"[:-1]
    

def disemvowel(string_):
    vowels = 'aeiou'
    string = ''
    string = ''.join([letter for letter in string_ if not letter.lower() in vowels])
    return string


def square_digits(num):
    squared_digits = ''.join([str(int(digit) ** 2) for digit in str(num)])
    return int(squared_digits)


def high_and_low(numbers):
    numbers_list = [int(num) for num in numbers.split()]
    return f"{max(numbers_list)} {min(numbers_list)}"


def descending_order(num):
    substr_num_list = [n for n in str(num)]
    inverted_num = "".join([num for num in sorted(substr_num_list, reverse=True)])
    return int(inverted_num)


def filter_list(l):
    new_list = [num for num in l if not isinstance(num, str)]
    return new_list


def get_middle(s):
    middle = len(s) // 2
    if len(s) % 2 == 0:
        return s[middle -1:middle + 1]
    else:
        return s[middle]

def accum(st):
    count = 1
    accum = ""
    for letter in st:
        accum += (letter*count).title() + "-"
        count += 1    
    return accum.removesuffix("-")
        
#ChatGPT proposed solution when I was reviewing my code for Pythonic fashion /
#it gave me a simplified version of it and got some better understanding of it
def accum(st):
    return '-'.join((letter * (i + 1)).title() for i, letter in enumerate(st))


def is_square(n):  
    if n < 0: #if negative
        return False
    else:
        product =  int(n ** 0.5)
        return product * product == n


def open_or_senior(data):
    member_category = []
    senior_min_age = 55
    min_handicap = 7

    for age, handicap in data:
        if age >= senior_min_age and handicap > min_handicap:
            member_category.append("Senior")
        else:
            member_category.append("Open")
    return member_category

#ChatGPT proposed solution when I was reviewing my code for Pythonic fashion /
#it gave me a simplified version of it and got some better understanding of it
def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]
