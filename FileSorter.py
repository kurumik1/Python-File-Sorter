import os
import time
import sys

directory = os.getcwd()
print("Using Directory " + directory)
time.sleep(1)
inpute = input("Word = ")
number = 1
fileEX = "." + input("File Extension = .")

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
            fileExt = os.path.splitext(filename)[1]
            if fileExt == fileEX:
                print(os.getcwd())
                if not f == os.path.realpath(sys.argv[0]):
                    newname = os.path.join(directory, inpute + str(number) + fileExt)
                    number = number + 1
                    print(filename + " => " + inpute + str(number) + fileExt)
                    os.rename(f, newname)
                else:
                    print("Ignoring Self.")
    else:
        print(filename + " isn't a file!") 