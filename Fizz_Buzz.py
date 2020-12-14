def fiz_buz(lst):
    
    for num in lst:
        
        if num % 3 == 0 and num % 5 == 0:
            print('\nfizzbuzz : ',num)
            continue
        
        if num % 3 == 0:
            print('\nfizz : ',num)
            
        if num % 5 == 0:
            print('\nbuzz : ',num)
            

            

            
lst = [3,6,10,20,15,45]
fiz_buz(lst)