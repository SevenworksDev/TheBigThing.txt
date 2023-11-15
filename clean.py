print("TheBigThing.txt Cleaner - Created by: sevenworks.eu.org")
with open("thebigthing.txt", "r") as infile: lines = infile.readlines()
unique = list(dict.fromkeys(lines))
with open("thebigthing_cleaned.txt", "w") as outfile: outfile.writelines(unique)