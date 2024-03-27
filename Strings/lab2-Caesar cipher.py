

text = input('Input one line of text to encrypt:')
shift = input('Input the shift number (Allow 1 to 25):')
shiftCheck = False

while not shiftCheck:
    if not shift.isdigit():
        print("Invalid Shift Number")
        shift = input('Input the shift number (Allow 1 to 25):')
    elif int(shift) < 1 or int(shift) > 25:
        print("Shift Number out of the range")
        shift = input('Input the shift number (Allow 1 to 25):')
    else:
        shiftCheck = True
        
cipher = ''
print(int(shift))
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + int(shift)
    if code > ord('Z'):
        code = ord('A') + ord('Z') - code
    cipher += chr(code)
print(cipher)
