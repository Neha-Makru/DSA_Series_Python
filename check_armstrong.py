def check_arm(n):
    sum, ori= 0,n
    while n>0: 
        rem= n%10 
        sum+=rem**3
        n//=10 
    if sum==ori: 
        return "Armstrong Number"
    else: 
        return "Not an Armstrong Number"
    
print(check_arm(153))
