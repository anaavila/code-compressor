############################################
#
# Program: CSS and HTML compressor Filter #1. 
# Frist Filter.
# compressFilter2.py must be built second.
#
# @Author Ana Avila (github.com/anaavila)
#
# @Date September 2018
#
# @Description
# Filter #1
# Simple program that removes line breaks of
# a CSS or HTML file into a single line of code.
#
#
############################################

fileToRead = "myOriginalFile.html"
fileToWrite = "filter-1.html"

rf = open(fileToRead, 'r')
fileData = rf.read()
listData = fileData.split("\n")

writeFile = open(fileToWrite, 'w')

# print(fileData)

print("Original file: " + fileToRead)
print("First filtered file: " + fileToWrite)

for i in listData:
	print(i, end="")
	writeFile.write(i)
