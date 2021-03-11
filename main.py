import os

# Dictionary consisting of the strings to be replaced
# key - the string to be replaced
# value - the string to be replaced with
replaceDict = {}


# method to replace the strings/words
def replaceStrings(line, destfile):
    for key in replaceDict:
        if key in line:
            line = line.replace(key, replaceDict[key])
    destfile.write(line)


# to iterate through the folder containing the '.python' files
for filename in os.listdir(source):
    if filename.endswith(".py"):
        # to write to a destination file
        destfile = open(source + '\\Fixed\\' + filename, "a")
        # to read the source file
        with open(source + '\\' + filename) as infile:
            # to read line by line
            for line in infile:
                replaceStrings(line, destfile)
        destfile.close()
