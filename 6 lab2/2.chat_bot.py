""" Chatbot.

    steps:
    1. input/listen
    2. process/decide
    3. output/talkback
"""


greet_words = ['hi', 'hello', 'yo', 'hey']
bye_words   = ['bye', 'tata', 'hasta la vista']
bad_words   = ['dog', 'pocha']

def listen():
    return input("Say something: ")

def decide(command):
    # print(command)
    command = command.lower()
    broken_words = command.split(" ")
    # print(broken_words)

    for word in broken_words:
        if word in greet_words:
            talkback("Hi man")
            break

        elif word in bye_words:
            talkback("Tata bye bye")
            break

        elif word in bad_words:
            talkback("You are a bad guy. Behave yourself!")
            break

def talkback(response):
    print(response)


if __name__ == '__main__':
    # print(__name__)
    while True:
        command = listen()
        decide(command)