# GÖKDENİZ ŞİMŞEK / 2210356067
def CREATECATEGORY():
    if ask_n:
        category = line[15:-1].split()          #to make a list by separating from spaces
    else:
        category = line[15:].split()
    if category[0] not in categories.keys():         #check if it created before or not
        categories[category[0]] = {}
        seats = category[1].split("x")          #to get values next to the x
        sea_num = int(seats[0])*int(seats[1])
        for row in list(string.ascii_uppercase[:int(seats[0])]):        #imported string library to use string.ascii command
            for column in range(int(seats[1])):
                column = str(column)
                categories[category[0]][row+column] = "X"   #set value 'X' for next part
        print("The category {} having {} seats has been created\n".format(category[0],sea_num), end='')
        with open("output.txt","a",encoding ="utf-8") as output_doc:
            output_doc.write("The category {} having {} seats has been created\n".format(category[0],sea_num))
    else:
        print("Warning: Cannot create the category for the second time. The stadium has already {}\n".format(category[0]), end='')
        with open("output.txt","a",encoding ="utf-8") as output_doc:
            output_doc.write("Warning: Cannot create the category for the second time. The stadium has already {}\n".format(category[0]))
def SELLTICKET():
    if ask_n:
        tickets = line[11:-1].split()
    else:
        tickets = line[11:].split()
    output_sell = ""
    if tickets[2] in categories:
        for seat in range(3, len(tickets)):
            if tickets[seat].find("-") == -1:       #to check for multiple selection (C9-12 etc.)
                try:
                    if not categories[str(tickets[2])][tickets[seat]] == "X":       #checking for it sold before this process
                        output_sell = output_sell + "Warning: The seat {} cannot be sold to {} since it was already sold!\n".format(tickets[seat],tickets[0])
                    else:
                        if tickets[1] == "student":
                            categories[str(tickets[2])][tickets[seat]] = "S"
                        elif tickets[1] == "full":
                            categories[str(tickets[2])][tickets[seat]] = "F"
                        else:
                            categories[str(tickets[2])][tickets[seat]] = "T"
                        output_sell = output_sell + "Success: {} has bought {} at {}\n".format(tickets[0], tickets[seat], tickets[2])
                except KeyError:
                    output_sell = output_sell + "Error: The category '{}' has less column or row (or both of them) than the specified index {}!\n".format(tickets[2],tickets[seat])
            else:
                try:
                    plc_hyp = tickets[seat].find("-")
                    first_seat = int(tickets[seat][1:plc_hyp])              #before the "-" sign
                    last_seat = int(tickets[seat][plc_hyp+1:])              #after the "-" sign
                    a = True
                    for i in range(first_seat, last_seat+1):                #first loop is for checking any warning
                        seats = str(tickets[seat][0])+str(i)
                        if not categories[str(tickets[2])][seats] == "X":
                            output_sell = output_sell + "Warning: The seats {} cannot be sold to {} due some of them have already been sold!\n".format(tickets[seat],tickets[0])
                            a = False               #if any seat is sold before it makes value of "a" False
                            break
                    if a:               #if there is no warning situation it sells desired tickets
                        for i in range(first_seat, last_seat + 1):
                            seats = str(tickets[seat][0]) + str(i)
                            if tickets[1] == "student":
                                categories[str(tickets[2])][seats] = "S"
                            elif tickets[1] == "full":
                                categories[str(tickets[2])][seats] = "F"
                            else:
                                categories[str(tickets[2])][seats] = "T"
                        output_sell = output_sell + "Success: {} has bought {} at {}\n".format(tickets[0],tickets[seat],tickets[2])
                except KeyError:
                    output_sell = output_sell +"Error: The category '{}' has less column or row (or both of them) than the specified index {}!\n".format(tickets[2],tickets[seat])
    else:
        output_sell = output_sell + "The purchase was unsuccessful due to the absence of {}.\n".format(tickets[2])
    print(output_sell, end='')
    with open("output.txt","a",encoding ="utf-8") as output_doc:
        output_doc.write(output_sell)
def CANCELTICKET():
    if ask_n:
        can_tick = line[13:-1].split()
    else:
        can_tick = line[13:].split()
    output_can = ""
    if can_tick[0] in categories:
        try:
            for i in range(1,len(can_tick)):
                if not categories[str(can_tick[0])][str(can_tick[i])] == "X":               #this means the seat is sold before and cancel function can work
                    categories[str(can_tick[0])][str(can_tick[i])] = "X"
                    output_can = output_can + "Success: The seat {} at '{}' has been canceled and now ready to sell again\n".format(can_tick[i],can_tick[0])
                else:
                    output_can = output_can + "Error: The seat {} at {} has already been free! Nothing to cancel\n".format(can_tick[i],can_tick[0])
        except KeyError:
            output_can = output_can + "Error: The category '{}' has less column or row (or both of them) than the specified index {}!\n".format(can_tick[0],can_tick[i])
    else:
        output_can = output_can + "The cancellation failed due to there being no {}.\n".format(can_tick[0])
    print(output_can, end='')
    with open("output.txt", "a",encoding ="utf-8") as output_doc:
        output_doc.write(output_can)
def BALANCE():
    if ask_n:
        balance = line[8:-1].split()
    else:
        balance = line[8:].split()
    output_bal = ""
    if balance[0] in categories:
        output_bal = output_bal + "Category report of '{}'\n--------------------------------\n".format(balance[0])
        values = list(categories[balance[0]].values())                  #to check the values(values are "X", "S", "F" or "T")
        stu_tic = values.count("S")
        full_tic = values.count("F")
        sea_tic = values.count("T")
        total_revenue = stu_tic*10 + full_tic*20 + sea_tic*250
        output_bal = output_bal + "Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} Dollars\n".format(stu_tic,full_tic,sea_tic,total_revenue)
    else:
        output_bal = output_bal + "The 'Balance' function could not be performed because there is no category named '{}'.".format(balance[0])
    print(output_bal, end='')
    with open("output.txt", "a",encoding ="utf-8") as output_doc:
        output_doc.write(output_bal)
def SHOWCATEGORY():
    if ask_n:
        cat_info = line[13:-1].split()
    else:
        cat_info = line[13:].split()
    output_sho = ""
    if cat_info[0] in categories:
        output_sho = output_sho + "Printing category layout of {}\n".format(cat_info[0])
        keys = list(categories[cat_info[0]].keys())                 #to get list of seats (A0,A1,...,Z25 etc.)
        last_key = keys[::-1][0]                                    #to find the number and letter of last seat
        last_key_let = last_key[0]                                  #it get letter of last seat
        last_key_num = int(last_key[1:])                            #it get number of last seat
        letters = list(string.ascii_uppercase)[::-1]                #to select the letter from the letter of last seat to "A"
        let_num = letters.index(last_key_let)                       #the index of letter of last seat
        for let in letters[let_num:]:
            output_sho = output_sho + "{} ".format(let)
            for num in range(last_key_num+1):
                output_sho = output_sho + "{}  ".format(categories[cat_info[0]][let+str(num)])
            output_sho = output_sho + "\n"
        for nums in range(last_key_num+1):
            if nums < 10:                       #to leave 2 spaces before single-digit numbers and 1 space for double-digit numbers
                output_sho = output_sho + "  {}".format(nums)
            else:
                output_sho = output_sho + " {}".format(nums)
        output_sho = output_sho + "\n"
    else:
        output_sho = output_sho + "The 'Show Category' function could not be performed because there is no category named '{}'.\n".format(cat_info[0])
    print(output_sho, end='')
    with open("output.txt","a",encoding ="utf-8") as output_doc:
        output_doc.write(output_sho)
def input_doc():
    global line, ask_n
    while True:
        first_three_letter = line[0:3]
        if "\n" in line:                            #to check for "\n" at the end of the line
            ask_n = True
        else:
            ask_n = False
        if first_three_letter == "CRE":
            CREATECATEGORY()
            line = input_document.readline()
        elif first_three_letter == "SEL":
            SELLTICKET()
            line = input_document.readline()
        elif first_three_letter == "CAN":
            CANCELTICKET()
            line = input_document.readline()
        elif first_three_letter == "BAL":
            BALANCE()
            line = input_document.readline()
        elif first_three_letter == "SHO":
            SHOWCATEGORY()
            line = input_document.readline()
        else:
            break
import string, sys
categories = {}
ask_n = True                #checking for is sentence include \n
output_doc = open("output.txt","w",encoding ="utf-8")                   #for creating output.txt document
output_doc.close()
try:
    input_file = sys.argv[1]
    input_document = open(input_file, "r", encoding="utf-8")
    line = input_document.readline()
    input_doc()
    input_document.close()
except:
    pass
