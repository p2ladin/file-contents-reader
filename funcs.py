
def splitter(a):
    b = a.split()
    return b

def counter_word(a: list) -> int:
    count = 0
    amt = len(a)
    for i in range(amt):
        count += 1
    return count
