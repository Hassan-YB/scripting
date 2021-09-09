import os

src_folder="sp1_13_full_annotated"
out_folder="sp1_13_nlu"
files_list=os.listdir(src_folder)
intent_sentences={}
for f in files_list:
        with open(os.path.join(src_folder,f),encoding="utf-8") as input_file:
                for line in input_file:
                        if "*" in line:
                                line=line.replace('\n','')
                                line=line.replace('*','').strip()
                                tokens=line.split(":")
                                if tokens[0] in intent_sentences:
                                        intent_sentences[tokens[0]].append(tokens[1])
                                else:
                                        intent_sentences[tokens[0]]=[]
                                        intent_sentences[tokens[0]].append(tokens[1])

for k,v in intent_sentences.items():
       with open(os.path.join(out_folder,k+".txt"),"w",encoding="utf-8") as f:
            f.write('\n'.join(v))
        
