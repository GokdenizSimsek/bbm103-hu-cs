import sys
infos = {}
inf_stu = []
try:
    file_name = sys.argv[1]
    with open(file_name, "r", encoding="utf-8") as file:
        students = file.readlines()
        file.close()
    for i in range(0, len(students)):
        inf_stu.append(students[i][:-1].split(":"))
        infos[inf_stu[i][0]] = inf_stu[i][1].split(",")
        keys = list(infos.keys())
    names = sys.argv[2]
    names = names.split(",")
    print(names)
    for i in range(len(names)):
        try:
            print("Name: {}, University: {},{}".format(names[i],infos[names[i]][0],infos[names[i]][1]))
        except:
            print("No record of ‘{}’ was found!".format(names[i]))
except:
    pass