# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 3 - Problem 1
# Purpose: rename files and file types in a directory
# Input: directory "text_files"
# Output: directory "text_files"

filepath = ("C:/Users/Jacob/Desktop/LAB 3/")

for root, dirs, files in os.walk(filepath):
	for f in files:
		f = f.lower()
		fil = f.split('.')
		if fil[1] == "txt":
			os.rename(filepath + f, "file_" + f)
		else:
			os.rename(filepath + f, "file_" + fil[0] + ".txt")
print "Great Success!"