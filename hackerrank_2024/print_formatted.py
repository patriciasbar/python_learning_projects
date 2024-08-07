def print_formatted(number):
    width = len(bin(number)[2:])
    for n in range(1, number + 1):
        print(f"{n:>{width}} {oct(n).upper()[2:]:>{width}} {hex(n).upper()[2:]:>{width}} {bin(n)[2:]:>{width}}")
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)