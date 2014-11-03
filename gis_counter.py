# Created by: Jacob Milner
# Assignment: TGIS 501A - Lab 3 - Problem 2
# Purpose: count the number of specified words and total words in a file
# Input: GIS_is_the_best.txt
# Output: N/A (Read Only)


# open and read the file
gis_file = open("C:/Users/Jacob/Desktop/LAB 3/GIS_is_the_best.txt", 'r')
file_list = gis_file.read()

# start word counts at zero
systems_count = 0
science_count = 0
other_words = 0

# evaluates all words as lowercase, loop to count specific words and total words
for word in file_list.split(' '):
	if word.lower() == 'systems':
		systems_count += 1
	elif word.lower() == 'science':
		science_count += 1
	else:
		other_words += 1
total_words = systems_count + science_count + other_words

print "Systems = ", str(systems_count)
print "Science = ", str(science_count)
print "Total Words = ", str(total_words)

gis_file.close()