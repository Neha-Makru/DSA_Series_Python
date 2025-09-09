def digits(n):
    while n>0: 
        rem= n%10 
        print(rem, end=" ") 
        n//=10 
    
digits(345)
