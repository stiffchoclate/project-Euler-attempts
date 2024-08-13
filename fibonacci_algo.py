def fibonnaci(n):
    terms = [0,1]
    summation = 0
    
    #assume terms are zero indexed
    #n is the position of the term wanted

    #generate the terms in the se
    while n != 1:
        length = len(terms)
        terms.append(terms [length-1] + terms[length-2])
        n = n - 1

    #sum of terms
    for x in terms:
        if x % 2 == 0:
            next
        else:
            summation = summation + x
    return summation
    

def fibonacci_limit():
    terms = [1,2]
    summation = 0
    while terms[-1] < 4*(10**6):
        length = len(terms)
        a = terms [length-1]#1 2
        b = terms[length-2] #0 1
        terms.append(a + b)
    for x in terms:
        if x % 2 != 0:
            next
        else:
            summation = summation + x
    print (terms)
    return summation

print(fibonacci_limit())
        
    
        
        
     
