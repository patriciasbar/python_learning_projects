def average(array):
    unique_numbers = set(array)
    return f"{sum(unique_numbers)/len(unique_numbers):.3f}"
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
