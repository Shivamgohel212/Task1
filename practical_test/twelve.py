def fibonacci():
    a = 0     
    b = 1      

    while True:
        yield a        
        a, b = b, a+b 

gen = fibonacci()
print(next(gen))  
print(next(gen))  
print(next(gen))  
print(next(gen))  
print(next(gen))  