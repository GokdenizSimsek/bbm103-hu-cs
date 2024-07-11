import sys
try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
except IndexError:
    print("IndexError: number of input files less than expected.")
except Exception:
    print("kaBOOM: run for your life!")
else:
    try:
        with open(file1, "r", encoding="utf-8") as f1:
            list1 = f1.readlines()
    except IOError:
        try:
            with open(file2,"r",encoding="utf-8") as f2:
                f2.close()
            print(f"IOError: cannot open {file1}")
        except IOError:
            print(f"IOError: cannot open {file1} and {file2}")
        except Exception:
            print("kaBOOM: run for your life!")
    else:
        try:
            with open(file2,"r",encoding="utf-8") as f2:
                list2 = f2.readlines()
        except IOError:
            print(f"IOError: cannot open {file2}")
        except Exception:
            print("kaBOOM: run for your life!")
        else:
            for i in range(len(list1)):
                list1[i] = list1[i].strip()
                ope_list = list1[i].split(" ")
                print("------------")
                try:
                    for j in range(len(ope_list)):
                        if int(float(ope_list[j])) + 0.5 <= float(ope_list[j]):
                            ope_list[j] = int(float(ope_list[j])) + 1
                        else:
                            ope_list[j] = int(float(ope_list[j]))
                except ValueError:
                    string = "ValueError: only numeric input is accepted.\nGiven input:"
                    for inputs in ope_list:
                        string += " " +str(inputs)
                    print(string)
                except Exception:
                    print("kaBOOM: run for your life!")
                else:
                    result = []
                    try:
                        for k in range(ope_list[2],ope_list[3] + 1):
                            if k % ope_list[0] == 0 and k % ope_list[1] != 0:
                                result.append(k)
                    except ZeroDivisionError:
                        string = "ZeroDivisionError: You can’t divide by 0.\nGiven input:"
                        for inputs in ope_list:
                            string += " " + str(inputs)
                        print(string)
                    except IndexError:
                        string = "IndexError: number of operands less than expected.\nGiven input:"
                        for inputs in ope_list:
                            string += " " + str(inputs)
                        print(string)
                    except Exception:
                        print("kaBOOM: run for your life!")
                    else:
                        try:
                            string_ope = ""
                            for inputs in result:
                                string_ope += " " + str(inputs)
                            print(f"My Result:\t\t{string_ope.strip()}\nResults to compare:\t{list2[i].strip()}")
                            assert list2[i].strip() == string_ope.strip()
                            print("Goool!!!")
                        except AssertionError:
                            print("Assertion Error: results don’t match.")
                        except Exception:
                            print("kaBOOM: run for your life!")
finally:
    print("˜ Game Over ˜")