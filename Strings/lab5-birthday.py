

def countBirthday(birthday):
    if not birthday.isdigit():
        return False
    
    sum = 0
    for num in birthday:
        sum += int(num)
    
    res = 0
    for x in str(sum):
        res += int(x)
    return res
    
birthday = input("Input your Birthday:")
res = countBirthday(birthday)
if not res:
    print("Invalid Birthday")
else:
    print(res)
        
    