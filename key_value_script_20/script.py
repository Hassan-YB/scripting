import codecs

#Global Variables
dict = {}

#Intializing keys of a dict
def intialize_dict(list):
    for str in list:
        index = str.split("\t")
        dict[index[0]] = []
    return dict

#Asserting values in keys of a dict
def def_dict(list):
    for str in list:
        index = str.split("\t")
        dict[index[0]].append(index[1])
    return dict


with codecs.open("file.txt","r",encoding="utf-8") as f:
    lines = f.read().splitlines()

    dict = intialize_dict(lines)
    dict = def_dict(lines)

    keys = dict.keys()

    f = open("output.txt","w",encoding="utf-8")
    r = open("results.txt","w",encoding="utf-8")
    for k in keys:
        list = dict[f'{k}']
        count = 1
        for str in list:
            if count <= 20:
                f.write(str)
                f.write("\n")
                count += 1
            else:
                break    
        #count values per key
        index = 0
        for cnt in list:
            index += 1
        r.write(f"Key:{k} , Count:{index}")
        r.write("\n")
    f.close()
    r.close()
    

