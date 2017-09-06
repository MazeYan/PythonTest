def happy():
    print("Happy birthday to you!")

def happyB(name):
    happy()
    happy()
    print("Happy birthday, dear {}!".format(name))
    happy()

happyB('Maze')
print()
happyB('Silence')
