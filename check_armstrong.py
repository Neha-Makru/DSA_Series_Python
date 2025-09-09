def check_arm(n):
    sum, ori= 0,n
    size=len(str(n))
    while n>0: 
        rem= n%10 
        sum+=rem**size
        n//=10 
    if sum==ori: 
        return "Armstrong Number"
    else: 
        return "Not an Armstrong Number"
    
print(check_arm(1634))
