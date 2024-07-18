def primenumber(num):
    is_prime = True
    
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
        else:
            is_prime = True
    
    if is_prime == True:
        print("It is prime number")
    else:
        print("It is not prime number")
        
        
n = primenumber(3)

# print(n)
