def digital_root(n):
    ls = sum([int(a) for a in str(n)])  
    
    print(ls)
    
    if ls < 10:
        return(ls)
    else:
        return(digital_root(ls)) 
        '''
        All python function returns None if it doesn't terminate by a return statement. 
        In your case, you successfully called the recursion but you discarded the result in the else part. 
        And after the if-block, the default return None is implicitly executed.
        
        Therefore it is necessary to add the return function before calling the recursive function. 
        '''
        
