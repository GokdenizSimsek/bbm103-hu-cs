import sys
mid_row = int(sys.argv[1])          # it gives middle row's number of diamond
row = 1


def diamond(number):
    global row
    if row > number*2 - 1:
        return
    elif row < number:             # upper part of middle row
        print((number - row) * " " + (row*2-1) * "*")
        row += 1
        diamond(number)
    elif row == number:             # at the middle row
        print((number * 2 - 1) * "*")
        row += 1
        diamond(number)
    else:                           # lower part of middle row
        print((row - number) * " " + ((number*2 - 1) - 2*(row - number)) * "*")
        row += 1
        diamond(number)


diamond(mid_row)
