# def do_something(x, y):
#     print(f'x: {x} y: {y}')

# do_something(12, 45)
# do_something('tomato', 'onion')

def do_something(work):
    print('Start the work')
    work()
    print('Done with the work')


def practice_coding():
    print('I am practicing Python')

def learning_python():
    print('learning python class')

do_something(practice_coding)
do_something(learning_python)