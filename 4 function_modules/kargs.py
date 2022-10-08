def full_name(f_name, l_name):
    name = f'{f_name} {l_name}'
    return name

name = full_name(l_name='chowdhury', f_name='Choto')
# print(name)

def long_name (**kargs):
    print (kargs)

def full_name(f_name, l_name):
    name = f'{f_name} {l_name}'
    return name

name = full_name(l_name='chowdhury', f_name='Choto')
# print(name)



def name_mixed (first, last, **name_parts):
    print(first, last, name_parts)


name = name_mixed(first='chowdhury', last='Choto', middle = 'majari')
print(name)


def all_types (first, *args, **kargs):
    print(first)
    for word in args:
        print(word)
    print(kargs)
    for key, value in kargs.items():
        print(key, value)


all_types('abd', 'ddd', 'kjk', 'lll', 'pp', name='Abul', father='babul')