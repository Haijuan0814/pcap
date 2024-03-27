
text = input('Enter:')

if len(text) < 1:
    print("It's not a palindrome")
else:
    text = text.lower()
    reverse = text[::-1]
    if text == reverse:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
