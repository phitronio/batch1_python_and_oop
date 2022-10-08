# with open('message.txt', 'a') as fileWrite:
#     fileWrite.write('I love python')

with open('message.txt', 'r') as fileRead:
    text = fileRead.read()
    print(text)