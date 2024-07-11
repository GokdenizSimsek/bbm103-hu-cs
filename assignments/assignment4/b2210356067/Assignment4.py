import sys
pla1_board = {}
pla2_board = {}
board1 = {}
board2 = {}
ships1 = {"Carrier":"-", "Battleship": {"B1": "-", "B2": "-"}, "Destroyer": "-", "Submarine": "-", "Patrol Boat": {"P1": "-", "P2": "-", "P3": "-", "P4": "-"}}
ships2 = {"Carrier":"-", "Battleship": {"B1": "-", "B2": "-"}, "Destroyer": "-", "Submarine": "-", "Patrol Boat": {"P1": "-", "P2": "-", "P3": "-", "P4": "-"}}
letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def output(a):
    with open("Battleship.out", "a", encoding="utf-8") as bat_out:
        bat_out.write(a)
    print(a,end="")

def def_ships(ship,point,direction,pla_board):
    point_list = point.split(",")
    if ship[0] == "B":
        if direction == "right":
            for i in letter[letter.index(point_list[1]):letter.index(point_list[1]) + 4]:
                pla_board[point_list[0]+i] = ship
        elif direction == "down":
            for j in range(4):
                pla_board[str(int(point_list[0])+j)+point_list[1]] = ship
    elif ship[0] == "P":
        if direction == "right":
            for i in letter[letter.index(point_list[1]):letter.index(point_list[1]) + 2]:
                pla_board[point_list[0]+i] = ship
        elif direction == "down":
            for j in range(2):
                pla_board[str(int(point_list[0])+j)+point_list[1]] = ship

def board_print(board_1, board_2):
    board_out = "Player1's Hidden Board\t\tPlayer2's Hidden Board\n  A B C D E F G H I J\t\t  A B C D E F G H I J\n"
    for i in range(1, 11):
        if i < 10:
            board_out += f"{i} "
            for j in letter:
                board_out += f"{board_1[str(i) + j]} "
            board_out = board_out[:-1]
            board_out += f"\t\t{i} "
            for j in letter:
                board_out += f"{board_2[str(i) + j]} "
            board_out = board_out[:-1]
            board_out += "\n"
        else:
            board_out += f"{i}"
            for j in letter:
                board_out += f"{board_1[str(i)+j]} "
            board_out = board_out[:-1]
            board_out += f"\t\t{i}"
            for j in letter:
                board_out += f"{board_2[str(i) + j]} "
            board_out = board_out[:-1]
            board_out += "\n\n"
    return board_out

def ship_print():
    ship_out = ""
    for i in ships1:
        if i == "Battleship":
            ship_out += f"{i}\t"
            for j in sorted(list(ships1[i].values()), reverse=True):
                ship_out += f"{j} "
            ship_out = ship_out[:-1]
            ship_out += f"\t\t\t\t{i}\t"
            for j in sorted(list(ships2[i].values()), reverse=True):
                ship_out += f"{j} "
            ship_out = ship_out[:-1]
            ship_out += "\n"
        elif i == "Patrol Boat":
            ship_out += f"{i}\t"
            for j in sorted(list(ships1[i].values()), reverse=True):
                ship_out += f"{j} "
            ship_out = ship_out[:-1]
            ship_out += f"\t\t\t{i}\t"
            for j in sorted(list(ships2[i].values()), reverse=True):
                ship_out += f"{j} "
            ship_out = ship_out[:-1]
            ship_out += "\n"
        elif i == "Carrier":
            ship_out += f"{i}\t\t{ships1[i]}\t\t\t\t{i}\t\t{ships2[i]}"
            ship_out += "\n"
        else:
            ship_out += f"{i}\t{ships1[i]}\t\t\t\t{i}\t{ships2[i]}"
            ship_out += "\n"
    return ship_out

def check_ship(playerboard, ship):
    if not "B1" in playerboard.values():
        ship["Battleship"]["B1"] = "X"
    if not "B2" in playerboard.values():
        ship["Battleship"]["B2"] = "X"
    if not "P1" in playerboard.values():
        ship["Patrol Boat"]["P1"] = "X"
    if not "P2" in playerboard.values():
        ship["Patrol Boat"]["P2"] = "X"
    if not "P3" in playerboard.values():
        ship["Patrol Boat"]["P3"] = "X"
    if not "P4" in playerboard.values():
        ship["Patrol Boat"]["P4"] = "X"
    if not "C" in playerboard.values():
        ship["Carrier"] = "X"
    if not "S" in playerboard.values():
        ship["Submarine"] = "X"
    if not "D" in playerboard.values():
        ship["Destroyer"] = "X"

try:                                            # checking for any mistakes and print kaBOOM
    file_1 = sys.argv[1]
    file_2 = sys.argv[2]
    f_in_1 = sys.argv[3]
    f_in_2 = sys.argv[4]
    try:
        with open(file_1, "r", encoding="utf-8") as ply1:
            ply1.close()
    except IOError:
        try:
            with open(file_2, "r", encoding="utf-8") as ply1:
                ply1.close()
        except IOError:
            try:
                with open(f_in_1, "r", encoding="utf-8") as pl1in:
                    pl1in.close()
            except IOError:
                try:
                    with open(f_in_2, "r", encoding="utf-8") as pl2in:
                        pl2in.close()
                    print(f"IOError: input files {file_1}, {file_2}, {f_in_1} are not reachable.")
                except IOError:
                    print(f"IOError: input files {file_1}, {file_2}, {f_in_1}, {f_in_2} are not reachable.")
            else:
                try:
                    with open(f_in_2, "r", encoding="utf-8") as pl2in:
                        pl2in.close()
                    print(f"IOError: input files {file_1}, {file_2} are not reachable.")
                except IOError:
                    print(f"IOError: input files {file_1}, {file_2}, {f_in_2} are not reachable.")
        else:
            try:
                with open(f_in_1, "r", encoding="utf-8") as pl1in:
                    pl1in.close()
            except IOError:
                try:
                    with open(f_in_2, "r", encoding="utf-8") as pl2in:
                        pl2in.close()
                    print(f"IOError: input files {file_1}, {f_in_1} are not reachable.")
                except IOError:
                    print(f"IOError: input files {file_1}, {f_in_1}, {f_in_2} are not reachable.")
            else:
                try:
                    with open(f_in_2, "r", encoding="utf-8") as pl2in:
                        pl2in.close()
                    print(f"IOError: input files {file_1} is not reachable.")
                except IOError:
                    print(f"IOError: input files {file_1}, {f_in_2} are not reachable.")
    else:
        try:
            with open(file_2, "r", encoding="utf-8") as ply1:
                ply1.close()
        except IOError:
            try:
                with open(f_in_1, "r", encoding="utf-8") as pl1in:
                    pl1in.close()
            except IOError:
                try:
                    with open(f_in_2, "r", encoding="utf-8") as pl2in:
                        pl2in.close()
                    print(f"IOError: input files {file_2}, {f_in_1} are not reachable.")
                except IOError:
                    print(f"IOError: input files {file_2}, {f_in_1}, {f_in_2} are not reachable.")
            else:
                try:
                    with open(f_in_2, "r", encoding="utf-8") as pl2in:
                        pl2in.close()
                    print(f"IOError: input files {file_2} is not reachable.")
                except IOError:
                    print(f"IOError: input files {file_2}, {f_in_2} are not reachable.")
        else:
            try:
                with open(f_in_1, "r", encoding="utf-8") as pl1in:
                    pl1in.close()
            except IOError:
                try:
                    with open(f_in_2, "r", encoding="utf-8") as pl2in:
                        pl2in.close()
                    print(f"IOError: input files {f_in_1} is not reachable.")
                except IOError:
                    print(f"IOError: input files {f_in_1}, {f_in_2} are not reachable.")
            else:
                try:
                    with open(f_in_2, "r", encoding="utf-8") as pl2in:
                        pl2in.close()
                except IOError:
                    print(f"IOError: input files {f_in_2} is not reachable.")
                else:
                    with open("Battleship.out", "w", encoding="utf-8") as bat_out:
                        bat_out.close()
                    with open(file_1, "r", encoding="utf-8") as ply1:
                        for nums1 in range(1, 11):
                            line1 = ply1.readline()
                            if line1 != "":
                                line1 = line1.strip().split(";")
                                for j in range(len(line1)):
                                    if len(line1[j]) > 1:
                                        raise Exception
                                    elif line1[j] == "":                    # to place "-" sign in the spaces
                                        line1[j] = "-"
                                for i in range(len(letter)):
                                    pla1_board[str(nums1) + letter[i]] = line1[i]       # to create player's board
                        with open("OptionalPlayer1.txt", "r", encoding="utf-8") as opt1:
                            for h in range(6):
                                line_1 = opt1.readline().strip().split(":")
                                ship = line_1[0]
                                line_1 = line_1[1].split(";")
                                point = line_1[0]
                                direction = line_1[1]
                                def_ships(ship, point, direction, pla1_board)
                    with open(file_2, "r", encoding="utf-8") as ply1:
                        for nums2 in range(1, 11):
                            line2 = ply1.readline()
                            if line2 != "":
                                line2 = line2.strip().split(";")
                                for j in range(len(line2)):
                                    if len(line2[j]) > 1:
                                        raise Exception
                                    elif line2[j] == "":                    # to place "-" sign in the spaces
                                        line2[j] = "-"
                                for i in range(len(letter)):
                                    pla2_board[str(nums2) + letter[i]] = line2[i]       # to create player's board
                        with open("OptionalPlayer2.txt", "r", encoding="utf-8") as opt2:
                            for h in range(6):
                                line_2 = opt2.readline().strip().split(":")
                                ship = line_2[0]
                                line_2 = line_2[1].split(";")
                                point = line_2[0]
                                direction = line_2[1]
                                def_ships(ship, point, direction, pla2_board)
                    with open(f_in_1, "r", encoding="utf-8") as p1in:
                        p1in_list = p1in.readline().split(";")
                        p1in_list = p1in_list[:-1]
                    with open(f_in_2,"r", encoding="utf-8") as p2in:
                        p2in_list = p2in.readline().split(";")
                        p2in_list = p2in_list[:-1]
                    for z in list(pla1_board.keys()):                       # creating hidden boards
                        board1[z] = "-"
                    for x in list(pla2_board.keys()):
                        board2[x] = "-"
                    values1 = list(pla1_board.values())
                    values2 = list(pla2_board.values())
                    pla1_tot = "B1" in values1 or "B2" in values1 or "C" in values1 or "D" in values1 or "P1" in values1 or "P2" in values1 or "P3" in values1 or "P4" in values1 or "S" in values1
                    pla2_tot = "B1" in values2 or "B2" in values2 or "C" in values2 or "D" in values2 or "P1" in values2 or "P2" in values2 or "P3" in values2 or "P4" in values2 or "S" in values2
                    k = 0           # indexes to get Player1's moves (it is increasing after all rounds)
                    j = 0           # indexes to get Player2's moves (it is increasing after all rounds)
                    n = 1           # to count the rounds of game (it is increasing after all rounds)
                    output("Battle of Ships Game\n\n")
                    output(f"Player1's Move\n\nRound : {n}\t\t\t\t\tGrid Size: 10x10\n\n")
                    output(board_print(board1, board2))
                    output(ship_print())
                    while (pla1_tot and pla2_tot) and k < len(p1in_list):
                        try:
                            pla1_cho = p1in_list[k]
                            point_check = pla1_cho.split(",")
                            output("\nEnter your move: " + pla1_cho + "\n")
                            if len(point_check[0]) < 1 or len(point_check[1]) < 1:                  # to check is there any element both side of ","
                                raise IndexError
                            str(point_check[1])
                            int(point_check[0])
                            if len(point_check) > 2 or len(point_check[1]) > 1:                     # checking for multiple "," and checking for any mistakes about letters (for ex. 1,AB)
                                raise ValueError
                            pla1_cho = pla1_cho.split(",")
                            point = pla1_cho[0] + pla1_cho[1]
                            assert point in pla1_board.keys()
                            assert board2[point] == "-"
                        except IndexError:
                            output("IndexError: Invalid move made.")
                            k += 1
                            continue
                        except ValueError:
                            output("ValueError: Invalid move made.")
                            k += 1
                            continue
                        except AssertionError:
                            output("AssertionError: Invalid Operation.")
                            k += 1
                            continue
                        else:
                            if pla2_board[point] != "-":
                                board2[point] = "X"
                                pla2_board[point] = "X"
                            else:
                                board2[point] = "O"
                                pla2_board[point] = "O"
                            check_ship(pla2_board, ships2)
                            output(f"\nPlayer2's Move\n\nRound : {n}\t\t\t\t\tGrid Size: 10x10\n\n")
                            output(board_print(board1, board2))
                            output(ship_print())
                            while pla2_tot and j < len(p2in_list):
                                try:
                                    pla2_cho = p2in_list[j]
                                    point_check = pla2_cho.split(",")
                                    output("\nEnter your move: " + pla2_cho + "\n")
                                    if len(point_check[0]) < 1 or len(point_check[1]) < 1:
                                        raise IndexError
                                    str(point_check[1])
                                    int(point_check[0])
                                    if len(point_check) > 2 or len(point_check[1]) > 1:
                                        raise ValueError
                                    pla2_cho = pla2_cho.split(",")
                                    point = pla2_cho[0] + pla2_cho[1]
                                    assert point in pla2_board
                                    assert board1[point] == "-"
                                except IndexError:
                                    output("IndexError: Invalid move made.")
                                    j += 1
                                    continue
                                except ValueError:
                                    output("ValueError: Invalid move made.")
                                    j += 1
                                    continue
                                except AssertionError:
                                    output("AssertionError: Invalid Operation.")
                                    j += 1
                                    continue
                                else:
                                    if pla1_board[point]!= "-":
                                        board1[point] = "X"
                                        pla1_board[point] = "X"
                                        check_ship(pla1_board, ships1)
                                        break                   # to continue with first player's move
                                    else:
                                        board1[point] = "O"
                                        pla1_board[point] = "0"
                                        check_ship(pla1_board, ships1)
                                        break
                            j += 1
                            k += 1
                            n += 1
                            values1 = list(pla1_board.values())  # checking for while loop's conditions
                            values2 = list(pla2_board.values())
                            pla1_tot = "B1" in values1 or "B2" in values1 or "C" in values1 or "D" in values1 or "P1" in values1 or "P2" in values1 or "P3" in values1 or "P4" in values1 or "S" in values1
                            pla2_tot = "B1" in values2 or "B2" in values2 or "C" in values2 or "D" in values2 or "P1" in values2 or "P2" in values2 or "P3" in values2 or "P4" in values2 or "S" in values2
                            if not pla1_tot or not pla2_tot:
                                break
                            output(f"\nPlayer1's Move\n\nRound : {n}\t\t\t\t\tGrid Size: 10x10\n\n")
                            output(board_print(board1, board2))
                            output(ship_print())
                    for keys in pla1_board.keys():
                        if pla1_board[keys] in ["P1","P2","P3","P4"]:
                            pla1_board[keys] = "P"
                        if pla1_board[keys] in ["B1","B2"]:
                            pla1_board[keys] = "B"
                    for keys in pla2_board.keys():
                        if pla2_board[keys] in ["P1","P2","P3","P4"]:
                            pla2_board[keys] = "P"
                        if pla2_board[keys] in ["B1","B2"]:
                            pla2_board[keys] = "B"
                    values1 = list(pla1_board.values())
                    values2 = list(pla2_board.values())
                    pla1_tot = "B1" in values1 or "B2" in values1 or "C" in values1 or "D" in values1 or "P1" in values1 or "P2" in values1 or "P3" in values1 or "P4" in values1 or "S" in values1
                    pla2_tot = "B1" in values2 or "B2" in values2 or "C" in values2 or "D" in values2 or "P1" in values2 or "P2" in values2 or "P3" in values2 or "P4" in values2 or "S" in values2
                    if not pla1_tot and not pla2_tot:
                        output("\nPlayer1 Wins!\nPlayer2 Wins!\nIt is a Draw!\n\nFinal Information\n\n")
                        output(board_print(pla1_board, pla2_board))
                        output(ship_print())
                    elif not pla1_tot:
                        output("\nPlayer2 Wins!\n\nFinal Information\n\n")
                        output(board_print(pla1_board, pla2_board))
                        output(ship_print())
                    elif not pla2_tot:
                        output("\nPlayer1 Wins!\n\nFinal Information\n\n")
                        output(board_print(pla1_board, pla2_board))
                        output(ship_print())
except Exception:
    output("kaBOOM: run for your life!")