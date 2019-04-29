# code_compressor
Removes line breaks and indentations of a CSS or HTML file into a single line of code
with the purpose to make your program to run faster.

See 'myOriginalFile.html' and 'myCompressedFile.html' to view code compressing results.
'myOriginalFile.html' is 105 lines of code, whth a size of 2,162 bytes. 
After it gets compressed 'myCompressedFile.html' it gets a size of 1,912 bytes.
105 lines of code is a small program, but as your code gets larger, you'll notice
the difference in size of bytes that makes a big difference when your html code loads.

compressFilter1.py must be built first.

compressFilter2.py must be built second.


Inlcude the file that you'll like to compress on the same folder as the programs

For variable 'fileToWrite2' on compressFilter2.py, put a different name than the original uncompressed file 'fileToRead2' from compressFilter1.py if you'll like to create a new file or want to avoid modifying the original uncompressed file on 'fileToRead2' from compressFilter1.py.
