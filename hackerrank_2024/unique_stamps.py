total_stamps = int(input())

unique_countries = set()

for _ in range(total_stamps):
    unique_countries.add(input())

print(len(unique_countries))


