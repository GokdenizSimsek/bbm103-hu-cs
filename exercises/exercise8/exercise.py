elements = input("Enter the 10 numbers for elements of list:")
the_list = [int(nums) for nums in elements.split()]
total = 0
def max_min_ave(list):
    def average(list):
        global total
        if len(list) == 0 :
            return total/10
        else:
            total += int(list[0])
            return average(list[1:])
    max_num = sorted(list)[-1]
    min_num = sorted(list)[0]
    return "Maximum number of elements: " + str(max_num) + "\nMinumum number of elements: " + str(min_num) + "\nAverage of numbers: " + str(average(list))

print(max_min_ave(the_list))
