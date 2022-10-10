numbers = [ 12, 45, 65, 23, 89, 78, 11]
numbers_iter = iter(numbers)
try:
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print('I am exploring iterator')
    print('I am confused about it')
    print(next(numbers_iter))
    print(next(numbers_iter))
    print('doing something else now')
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
except StopIteration:
    print('iteration is stopped')

