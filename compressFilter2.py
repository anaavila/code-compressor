############################################
#
# Program: CSS and HTML compressor Filter 2. 
# Second Filter (Final Filter).
# compressFilter1.py must be built first.
#
# @Author Ana Avila (github.com/anaavila)
#
# @Date September 2018
#
# @Description
# Filter #2
# Simple program that removes indentations of a CSS or HTML file.
#
# note:
# for variable 'fileToWrite2'
# put a different name than the original uncompressed file 'fileToRead2'
# from compressFilter1.py if you'll like to create a new file or want 
# to avoid modifying the original uncompressed file on 'fileToRead2' 
# from compressFilter1.py.
#
############################################

import os

fileToRead2 = "filter-1.html"
fileToWrite2 = "myCompressedFile.html"

rf2 = open(fileToRead2, 'r')
fileData2 = rf2.read()
listData2 = fileData2.split(" ")

writeFile2 = open(fileToWrite2, 'w')

print("First filtered file: " + fileToRead2)
print("Second filtered file: " + fileToWrite2)

secondFilter = fileData2.replace("	", "");
print(secondFilter)
writeFile2.write(secondFilter)

os.remove(fileToRead2)