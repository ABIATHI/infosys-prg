#PF-Assgn-31
def check_palindrome(word):
    i=word[::-1]
    if i==word:
        status=True
    else:
        status=False
    return(status)    
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
