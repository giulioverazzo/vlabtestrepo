import datetime
import sys
import shutil

if len(sys.argv) != 2:
    print("Errore, devi specificare un file di input")
    exit(-1)

input = sys.argv[1]
output = "output.txt"

shutil.copyfile(input, output)

with open(output, "a") as outputfile:
    cur_timestamp = str(datetime.datetime.now())
    outputfile.write("\n"+cur_timestamp)


