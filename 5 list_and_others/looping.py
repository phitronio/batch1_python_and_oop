from re import sub


numbers = [ 12, 45, 65, 23, 89, 78, 11, 10]
nums = {12, 45, 56, 45, 12, 89}
numbers_tuple = 12, 45, 56, 45, 12, 89
marks = { 'physics': 12, 'chemistry': 45, 'math': 56 }
# total = sum(numbers)
total = 0
for num in numbers:
    total += num
#     # print(i)
print(total)

for i, num in enumerate(numbers):
    print(i, num)

for num in nums:
    total += num
print(total)

for num in numbers_tuple:
    total += num

print(total)

for mark in marks:
    val = marks[mark]
    # print(mark, val)

# for subject, mark in marks.items():
#     print(subject, mark)


country = 'Bangladesh'
for char in country:
    print(char)