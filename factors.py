n=int(input("Enter the number: "))
for i in range(1,int(n**0.5)+1): 
    if n%i==0:
        print(i, end=" ")
        if n/i!=i:
            print(n//i, end=" ")
