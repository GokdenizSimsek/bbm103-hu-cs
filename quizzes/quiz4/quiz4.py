import sys
try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    messages = {}
    with open(input_file,"r",encoding= "utf-8") as input:
        while True:
            line = input.readline()
            if line == "":
                break
            else:
                a = line.find("\n")
                if a != -1:
                    line = line[:-1]
                line_list = line.split("\t")
                line_list[0] = int(line_list[0])
                line_list[1] = int(line_list[1])
                if line_list[0] not in messages:
                    messages[line_list[0]] = {}
                messages[line_list[0]][line_list[1]] = line_list[2]
        input.close()
    keys = list(messages.keys())
    mes_num = 1
    with open(output_file,"w",encoding= "utf-8") as output:
        output.close()
    for i in sorted(keys):
        with open(output_file,"a",encoding= "utf-8") as output:
            output.write("Message\t{}\n".format(mes_num))
        sentences = list(messages[i].keys())
        for j in sorted(sentences):
            with open(output_file, "a", encoding="utf-8") as output:
                output.write("{}\t{}\t{}\n".format(i,j,messages[i][j]))
        mes_num += 1
except:
    pass