import csv
import sys
import codecs

filename = sys.argv[1]
with open(f"{filename}", encoding="utf8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    count = 1
    for row in csv_reader:
        if any(map(str.isdigit, row[0])):
            f = open(f"output3/{row[0]}.txt","w", encoding="utf-8")
            f.write(f'{row[1]}\t{row[2]}')
            f.write("\n")
        elif count == 1:
            count = 2
            pass
        else:
            f.write(f'{row[1]}')
            f.write("\n")

        
