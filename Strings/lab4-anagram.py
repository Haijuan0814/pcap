

def is_anagram(text1 , text2):
    if not text1 or not text2:
        return False
    
    text1 = text1.replace(' ','')
    text2 = text2.replace(' ','')
    
    if len(text1) != len(text2):
        return False
        
    text1 = sorted(text1.lower())
    text2 = sorted(text2.lower())
    if text1 == text2:
        return True
    else:
        return False


text1 = input('Input first text:')
text2 = input('Input second text:')
res = is_anagram(text1 , text2)
if res:
    print("Anagrams")
else:
    print("Not anagrams")
    