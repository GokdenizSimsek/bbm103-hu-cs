import sys
mid_row = int(sys.argv[1])
row_num = mid_row*2 - 1
output = [(mid_row - row) * " " + (row*2-1) * "*" if row <= mid_row else (row - mid_row) * " " + ((mid_row*2 - 1) - 2 * (row - mid_row)) * "*" for row in range(1, row_num+1)]

for rows in output:
    print(rows)
