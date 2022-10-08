try:
    num = 15/0
    print(num)
except:
    print('something went wrong')
finally:
    print('this is done')