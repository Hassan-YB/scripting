import csv
import sys

filename = sys.argv[1]
with open(f"{filename}", encoding="utf8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    f = open(f"output.txt","w", encoding="utf-8")
    for row in csv_reader:
        count = row[2].split()
        i = 0
        for y in count:
            i += 1
        f.write(f'{row[2]}\t{i}')
        f.write("\n")

        
