def create():
    global create_done, creat_not_done
    if ask_n:
        infos = line[7:-1].split(", ")
    else:
        infos = line[7:].split(", ")
    if infos not in patients:
        patients.append(infos)
        create_done = "Patient {} is recorded.\n".format(infos[0])
        return create_done
    else:
        creat_not_done = "Patient {} cannot be recorded due to duplication.\n".format(infos[0])
        return creat_not_done
def remove():
    global remove_done, remove_not_done
    if ask_n:
        pat_rem = line[7:-1]
    else:
        pat_rem = line[7:]
    patient2 = False     #for checking if the patient is in the patients list
    for i in range(len(patients)):
        patients_name = patients[i][0]
        if patients_name == pat_rem :
            patient2 = True
            patients.pop(i)
            remove_done = "Patient {} is removed.\n".format(patients_name)
            return remove_done
        else:
            pass
    if patient2 == False:
        remove_not_done = "Patient {} cannot be removed due to absence.\n".format(pat_rem)
        return remove_not_done
def calculate_probability(ratio):
    plc_den = ratio[3].find("/")
    num_rat = float(ratio[3][:plc_den])
    den_rat = float(ratio[3][plc_den+1:])
    ratio = float(ratio[1])
    ratio2 = 1 - ratio
    tolerance = ratio2 * den_rat
    real_ratio = tolerance + num_rat
    probability = num_rat/real_ratio*100
    return probability
def probability():
    global probability_done, probability_not_done
    if ask_n:
        pat_pro = line[12:-1]
    else:
        pat_pro = line[12:]
    patient = False     #for checking if the patient is on the patients list
    for i in range(len(patients)):
        patients_name = patients[i][0]
        if patients_name == pat_pro:
            patient = True
            prob = str(calculate_probability(patients[i]))
            if int(float(prob)) == float(prob[:5]):
                prob = int(prob[:2])
            else:
                prob = float(prob[:5])
            probability_done = "Patient {} has a probability of {}% of having {}.\n".format(patients_name,prob,patients[i][2])
            return probability_done
        else:
            pass
    if patient == False:
        probability_not_done = "Probability for {} cannot be calculated due to absence.\n".format(pat_pro)
        return probability_not_done
def recommendation():
    global treatment, not_treatment, not_exist_treatment
    if ask_n:
        pat_rec = line[15:-1]
    else:
        pat_rec = line[15:]
    patient1 = False     #for checking if the patient is on the patients list
    for i in range(len(patients)):
        patients_name = patients[i][0]
        if patients_name == pat_rec:
            patient1 = True
            tre_risk = float(patients[i][5])*100
            if calculate_probability(patients[i]) >= tre_risk:
                treatment = "System suggests {} to have the treatment.\n".format(pat_rec)
                return treatment
            else:
                not_treatment = "System suggests {} NOT to have the treatment.\n".format(pat_rec)
                return not_treatment
    if patient1 == False:
        not_exist_treatment = "Recommendation for {} cannot be calculated due to absence.\n".format(pat_rec)
        return not_exist_treatment
def list():
    out_list = "Patient\t"+"Diagnosis\t"+"Disease\t\t\t"+"Disease\t\t"+"Treatment\t\t"+"Treatment\n"+"Name\t"+"Accuracy\t"+"Name\t\t\t"+"Incidence\t"+"Name\t\t\t"+"Risk\n"+73*"-"+"\n"
    for i in range(len(patients)):
        per_accuracy = str(float(patients[i][1])*100)
        if len(per_accuracy) == 4:
            per_accuracy = per_accuracy + "0"
        per_accuracy = per_accuracy + "%"
        per_risk = str(int(float(patients[i][5])*100))+"%"
        if len(patients[i][0]) < 4:
            out_list = out_list + patients[i][0]+"\t\t"+per_accuracy+"\t\t"
            if len(patients[i][2]) < 12:
                out_list = out_list + patients[i][2]+"\t\t"+patients[i][3]+"\t"
                if len(patients[i][4]) < 8:
                    out_list = out_list + patients[i][4]+"\t\t\t"+per_risk+"\n"
                elif 8 <= len(patients[i][4]) < 12:
                    out_list = out_list + patients[i][4] + "\t\t" + per_risk + "\n"
                elif 12 <= len(patients[i][4]) < 16:
                    out_list = out_list + patients[i][4] + "\t" + per_risk + "\n"
                else:
                    out_list = out_list + patients[i][4] + per_risk + "\n"
            else:
                out_list = out_list + patients[i][2]+"\t"+patients[i][3]+"\t"
                if len(patients[i][4]) < 8:
                    out_list = out_list + patients[i][4] + "\t\t\t" + per_risk + "\n"
                elif 8 <= len(patients[i][4]) < 12:
                    out_list = out_list + patients[i][4] + "\t\t" + per_risk + "\n"
                elif 12 <= len(patients[i][4]) < 16:
                    out_list = out_list + patients[i][4] + "\t" + per_risk + "\n"
                else:
                    out_list = out_list + patients[i][4] + per_risk + "\n"
        else:
            out_list = out_list + patients[i][0]+"\t"+per_accuracy+"\t\t"
            if len(patients[i][2]) < 12:
                out_list = out_list + patients[i][2] + "\t\t" + patients[i][3] + "\t"
                if len(patients[i][4]) < 8:
                    out_list = out_list + patients[i][4] + "\t\t\t" + per_risk + "\n"
                elif 8 <= len(patients[i][4]) < 12:
                    out_list = out_list + patients[i][4] + "\t\t" + per_risk + "\n"
                elif 12 <= len(patients[i][4]) < 16:
                    out_list = out_list + patients[i][4] + "\t" + per_risk + "\n"
                else:
                    out_list = out_list + patients[i][4] + per_risk + "\n"
            else:
                out_list = out_list + patients[i][2] + "\t" + patients[i][3] + "\t"
                if len(patients[i][4]) < 8:
                    out_list = out_list + patients[i][4] + "\t\t\t" + per_risk + "\n"
                elif 8 <= len(patients[i][4]) < 12:
                    out_list = out_list + patients[i][4] + "\t\t" + per_risk + "\n"
                elif 12 <= len(patients[i][4]) < 16:
                    out_list = out_list + patients[i][4] + "\t" + per_risk + "\n"
                else:
                    out_list = out_list + patients[i][4] + per_risk + "\n"
    return out_list
def output_doc(returning_value):
    with open("doctors_aid_outputs.txt", "a", encoding="utf-8") as doc_aid_outs:
        doc_aid_outs.write(returning_value)
def input_doc():
    global line, ask_n
    while True:
        first_three_letter = line[0:3]
        if "\n" in line:
            ask_n = True
        else:
            ask_n = False
        if first_three_letter == "cre":
            output_doc(create())
            line = doc_aid_file.readline()
        elif first_three_letter == "rem":
            output_doc(remove())
            line = doc_aid_file.readline()
        elif first_three_letter == "lis":
            output_doc(list())
            line = doc_aid_file.readline()
        elif first_three_letter == "pro":
            output_doc(probability())
            line = doc_aid_file.readline()
        elif first_three_letter == "rec":
            output_doc(recommendation())
            line = doc_aid_file.readline()
        else:
            break
patients = []
ask_n = True     #checking for is sentence include \n
doc_aid_outs = open("doctors_aid_outputs.txt","w",encoding ="utf-8")     #for creating output.txt document
doc_aid_outs.close()
doc_aid_file = open("doctors_aid_inputs.txt","r",encoding ="utf-8")
line = doc_aid_file.readline()
input_doc()
doc_aid_file.close()