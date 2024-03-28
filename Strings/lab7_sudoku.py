

def isSudoku(numbers):
    # check each row and column
    for i in range(9):
        if sorted(numbers[i]) != list(range(1, 10)):
            return False
        if sorted([numbers[j][i] for j in range(9)]) != list(range(1, 10)):
            return False
    
    # check each sub         
    for i in range(0,9,3):
        for j in range(0,9,3):
            sub = []
            for k in range(3):
                sub.extend(numbers[i+k][j:j+3])
            if sorted(sub) != list(range(1, 10)):
                return False
                
    return True
            

# Read Sudoku board from user input
sudoku = []
print("Enter the Sudoku board (9 rows, each containing 9 digits):")
for _ in range(9):
    row = input().strip()
    if len(row) != 9 or not row.isdigit():
        print("Invalid input. Please enter 9 digits for each row.")
        exit()
    sudoku.append([int(digit) for digit in row])

# Check if the Sudoku board is valid
if isSudoku(sudoku):
    print("Yes")
else:
    print("No")
        
   
        