def fizz_buzz(numbers):
    
    for i in range(len(numbers)):
        num = numbers[i]
            
        
        if num % 3 == 0:
            numbers[i] ='fizz'
            
        if num % 5 == 0:
            
            numbers[i] ='buzz'
            
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = 'fizzbuzz'
            
numbers = [3,9,5,10,15,75]
fizz_buzz(numbers)
print(numbers)