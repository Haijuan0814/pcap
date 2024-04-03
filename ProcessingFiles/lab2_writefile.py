
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
    
    letters = sorted(letters.items() , key = lambda x: x[1])         
    for ch in letters:
        print(f"{ch} -> {letters[ch]}")
        
    
    # Write the sorted histogram to a file with the same name but with '.hist' suffix
    output_file = src + '.hist'
    with open(output_file, 'w') as file:
        for char, count in letters:
            file.write(f"{char}: {count}\n")
            
    print(f"Histogram generated and saved to {output_file}")
            
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

