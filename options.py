import time
from funcs import splitter

def options_intro():
    print("Welcome to; File contents reader!")
    print("With this programm.. you'll be able to read the exact number of contents of the specific file.")
    print("- - -")
    print("Please choose one of the options;")
    print("1. Start programm")
    print("2. End programm")
    ans = input("> ")
    if ans == "1":
        options_oneContinue()
    elif ans == "2":
        print("Exiting ")
        for i in range(3):
            time.sleep(0.5)
            print(".")
        print("Goodbye!")
        exit(0)

def options_oneContinue():
        print("Input text...")
        txt = input("> ")
        if txt != "" or txt != None:
            pass
