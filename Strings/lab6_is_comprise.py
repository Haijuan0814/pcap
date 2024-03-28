
def is_comprise(str1 , str2):
    if len(str1) > len(str2):
        return False
    index = str2.find(str1)
    if index == -1:
        return False
    else:
        return True

text1 = input('Input first:')
text2 = input('Input sencond:')
if is_comprise(text1 , text2):
    print('Yes')
else:
    print('No')