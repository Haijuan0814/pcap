
pattern={
    0:'###\n# #\n# #\n# #\n###',
    1:'  #\n  #\n  #\n  #\n  #',
    2:'###\n  #\n###\n#  \n###',
    3:'###\n  #\n###\n  #\n###',
    4:'# #\n# #\n###\n  #\n  #',
    5:'###\n#  \n###\n  #\n###',
    6:'###\n#  \n###\n# #\n###',
    7:'###\n  #\n  #\n  #\n  #',
    8:'###\n# #\n###\n# #\n###',
    9:'###\n# #\n# #\n  #\n###',
}

def led(number : int) -> str:
    lights = []
    for s in str(number):
        num = int(s)
        if 9 >= num >= 0:
            lights.append(pattern[num].split('\n'))
    
    for i in range(5):
        for light in lights:
            print(light[i] , end=' ')
            
        print()
    
led(1233456789)
            
        