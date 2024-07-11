import sys

try:
    numbers = sys.argv[1].split(",")
    i = 1
    while len(numbers) > i:
        numbers.pop(i)
        i += 1
    i = 2
    while len(numbers) > i:
        numbers.pop(i)
        i += 2
    i = 6
    while len(numbers) > i:
        numbers.pop(i)
        i += 6
    print("Output:",*numbers)
except:
    pass