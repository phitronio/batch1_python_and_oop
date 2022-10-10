numbers = [ 12, 45, 65, 23, 89, 78, 11]


odd_numbers = []
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)

# print(odd_numbers)

odd_numbers2 = [num for num in numbers if num %2 == 1 if num % 5 == 0]
# print(odd_numbers2)

names = ['sakib', 'sabbir', 'salman']
ages = [37, 32, 21]

pairs = [ (name, age) for name in names for age in ages if age < 25]
# print(pairs)

for name in names:
    print(name)
    for age in ages:
        if age < 25:
            print(name, age)
