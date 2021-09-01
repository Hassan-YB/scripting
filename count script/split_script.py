import codecs

#Global Variables
dict = {}
dict1 = {} #30%
dict2 = {} #50% of 30%
dict3 = {} #50% left of 30%

#Intializing keys of a dict
def intialize_dict(list):
    for str in list:
        index = str.split("\t")
        dict[index[1]] = []
        dict1[index[1]] = []
        dict2[index[1]] = []
        dict3[index[1]] = []
    return dict

#Asserting values in keys of a dict
def def_dict(list):
    for str in list:
        index = str.split("\t")
        dict[index[1]].append(index[0])
    return dict

def percentage_output_30(key,per,o,dict):
    f4 = open(f"Results_Test_Seg_30_{o}.txt","w",encoding="utf-8")
    f4.write(f"Results of seg {o} of 30%\n")
    Total = 0
    for k in key:
        if int(k) <= 15:
            
            list = dict[f'{k}']
            count = 0
            for i in list:
                count += 1
            percentage = int(count * per)
            print(percentage)
            value = 0
            Total = Total + count
            f4.write(f"key:{k} , Values:{count}")
            f4.write("\n")
            f = open(f"Test_Seg_30_{o}_1/{k}.txt","w",encoding="utf-8")
            f2 = open(f"Test_Seg_30_{o}_2/{k}.txt","w",encoding="utf-8")
            f3 = open(f"Test_Seg_30_{o}_3/{k}.txt","w",encoding="utf-8")
            
            for str in list:
                if value <= percentage:
                    f.write(str)
                    f.write("\n")
                    value += 1
                elif value <= (percentage + percentage):
                    f2.write(str)
                    f2.write("\n")
                    value += 1
                else:
                    f3.write(str)
                    f3.write("\n")
                    value += 1
            f.close()
            f2.close()
            f3.close()
        else:
            pass
    f4.write(f"Total = {Total}")
    f4.close()

def percentage_output(key,per):
    for k in key:
        if int(k) <= 15:
            list = dict1[f'{k}']
            count = 0
            for i in list:
                count += 1
            percentage = int(count * per)
            print(percentage)
            value = 0
            f = open(f"Test_Seg_30_1/{k}.txt","w",encoding="utf-8")
            f2 = open(f"Test_Seg_30_2/{k}.txt","w",encoding="utf-8")
            for str in list:
                if value <= percentage:
                    dict2[k].append(str)
                    f.write(str)
                    f.write("\n")
                    value += 1
                else:
                    dict3[k].append(str)
                    f2.write(str)
                    f2.write("\n")
                    value += 1
            f.close()
            f2.close()
        else:
            pass


with codecs.open("output.txt","r",encoding="utf-8") as f:
    results = open("results.txt","w")
    lines = f.read().splitlines()
    

    dict = intialize_dict(lines)
    dict = def_dict(lines)

    keys = dict.keys()

    results.write("30% of dataset results\n")

    for k in keys:
        if int(k) <= 15:
            f = open(f"Test_Seg_30/{k}.txt","w",encoding="utf-8")
            list = dict[f'{k}']
            count = 0
            for i in list:
                count += 1
            percentage = int(count * 0.3)
            results.write(f"key:{k} , Values:{percentage}")
            results.write("\n")
            value = 0
            for str in list:
                if value <= percentage:
                    f.write(str)
                    f.write("\n")
                    dict1[k].append(str)
                    dict[k].remove(str)
                    value += 1
                else:
                    break
            f.close()

    results.write("\n")
    results.write("70% Remaining unused dataset\n")

    for i in keys:
        f = open(f"Train_Seg_70/{i}.txt","w",encoding="utf-8")
        list = dict[i]
        count = 0
        for y in list:
            count += 1
        results.write(f"key{i}: Values:{count}")
        results.write("\n")
        for str in list:
            f.write(str)
            f.write("\n")
        f.close()
    
    results.close()
    percentage_output(keys,0.5)
    percentage_output_30(keys,0.33,1,dict2)
    percentage_output_30(keys,0.33,2,dict3)