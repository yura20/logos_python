text = input("enter your word :")

def palindrome(text=""):
    text1 = text
    text2 = text[::-1]
    if text1 == text2:
        print('{palin} is palindrome'.format(palin = text1))
    else:
        print("{palin} isn't palindrome".format(palin = text1))
        
palindrome(text)