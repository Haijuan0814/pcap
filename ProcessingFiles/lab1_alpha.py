
from os import strerror

srcname = input("Enter the file name: ")
try:
    src = open(srcname, 'r')
    letters = []
    for line in open(srcname, 'r'):
        for ch in line:
            if ch.isalpha():
                ch = ch.lower()
                letters[ch] = letters.get(ch , 0) + 1
                
    for ch in sorted(letters):
        print(f"{ch} -> {letters[ch]}")
            
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

