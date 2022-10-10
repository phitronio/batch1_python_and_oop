numbers = [12, 45, 56, 45, 12, 89]
# print(numbers)
# set
nums = {12, 45, 56, 45, 12, 89}
# print(nums)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(77)
numbers_set.add(45)
numbers_set.remove(12)
print(len(numbers_set))