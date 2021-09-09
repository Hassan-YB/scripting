import os
import sys, getopt

src_folder='sp1_13_stories'
out_folder='sp1_13_full_annotated'
files_list=os.listdir(src_folder)
for files in files_list:
        with open(os.path.join(src_folder,files),encoding="utf-8") as f:
                file_data=[]
                file_data.append("## "+files[:files.index('.')])      
                for line in f:
                        line=line.replace('\n','').strip()
                        if '*' in line:
                                line='\n'+line+":"
                        elif '-' in line:
                                line='\n\t'+line
                        file_data.append(line)
        with open(os.path.join(out_folder,files.replace('.txt','.md')),'w',encoding="utf-8") as of:
                of.write(''.join(file_data))               
