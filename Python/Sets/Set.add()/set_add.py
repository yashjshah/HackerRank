# Enter your code here. Read input from STDIN. Print output to STDOUT

country_stamps = int(input())

countries = set()

for _ in range(country_stamps):
    countries.add(input())

print(len(countries))
