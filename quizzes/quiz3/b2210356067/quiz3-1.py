import sys
try:
    result = 0
    num_1 = int(sys.argv[1])
    num_2 = int(sys.argv[2])
    step_1 = num_1**num_2
    def sum_dig():
        global result, step_1
        while step_1 // 10 != 0:
            a = step_1 % 10
            result = result + a
            step_1 = step_1 // 10
        result += step_1
        return result

    while step_1 // 10 != 0:
        sum_dig()
        if result // 10 != 0:
            step_1 = result
            result = 0
            sum_dig()
    print(result)
except:
    pass