def count_digits(n):
    count=0
    while n>0: 
        rem= n%10 
        count+=1
        n//=10 
    return count 
    
print(count_digits(345))
