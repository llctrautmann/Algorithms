def interlockable(a, b):
    
    x = list(format(a, 'b'))
    y = list(format(b, 'b'))
    
    x = x[::-1]
    y = y[::-1]
    
    if len(x) >= len(y):
        for i in range(len(y)):
            if int(y[i]) + int(x[i]) == 2:
                return(False)
            else:
                pass
            
    if len(x) < len(y):
        for i in range(len(x)):
            if int(y[i]) + int(x[i]) == 2:
                return(False)
            else:
                pass
    
    return(True)
            
