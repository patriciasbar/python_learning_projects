def fizzBuzz(n):
    for i in range(1, n+1):
        mult_3 = i % 3
        mult_5 = i % 5
        if mult_3 == 0 and mult_5 == 0:
            print ("FizzBuzz")
        elif mult_3 == 0 :
            print("Fizz")
        elif mult_5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    n = int(input("n: "))
    fizzBuzz(n)


