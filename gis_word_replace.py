# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 3 - Problem 3
# Purpose: parse a file and replace uppercase words with lowercase
# Input: GIS_is_the_best.txt
# Output: GIS_is_the_best_fixed.txt

# open and read the file, create variable for split list
gis_file = open("C:/Users/Jacob/Desktop/LAB 3/GIS_is_the_best.txt", "r")
gis_file_fix = open("C:/Users/Jacob/Desktop/LAB 3/GIS_is_the_best_fixed.txt", "w+")
file_list = gis_file.read()
ord_list = file_list.split(' ')
for word in ord_list
	i = int(ord_list.index(word))
	if word == 'Science':
		del ord_list[i]
		ord_list.insert(i,'Systems')
	elif word == "science"
		del ord_list[i]
		ord_list.insert(i,'systems')
join_obj = ' '
gis_file_fix.write(join_obj.join(ord_list))
print "Done!"
gis_file.close()
gis_file_fix.close()