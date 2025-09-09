def check_pal(n):
    rev, ori=0, n
    while n>0: 
        rem= n%10 
        rev=rev*10 + rem
        n//=10 
    if rev==ori: 
        return "Palindrome"
    else: 
        return "Not a Palindrome"
    
print(check_pal(7898))
