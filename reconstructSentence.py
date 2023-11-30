"""

reconstructSentence.py
by David Melanson

for IoT Homework 10 Problem 1
takes 2 arguments, the names of each input file being used to reconstruct
outputs output.txt that contains the reconstructed sentence

example invocation: python3 reconstructSentence.py input1.txt input2.txt

"""

import sys

#open file to be written to
f = open('output.txt', 'w')
#read both files into a concatenate list of strings
#this reverses the first list being read in and leaves the second the way it is
words = (open(sys.argv[1]).read().split()[::-1] + open(sys.argv[2]).read().split())
#store list size
len = len(words)
#this uses a list comprehension to join the words from each end of the list, then joins this list with an empty list
#then writes the string out to the file f opened above
# "" instantiates a new list rather than doing that on its own line
f.write("".join([f"{words[i]} {words[len-i-1]} " for i in range(int(len/2))]))
#if the list is odd, write final element to file
if len%2:
    f.write(words[int(len/2)])
f.close()