# return masked string
def maskify(cc):
    '''
    I need to take any input check the length of the input and convert any values except the last four into hashtags
    '''
    
    target = str(cc)
    target_length = len(target)
    l = [a for a in target]
    
    for i in range(len(l)-4):
        l[i] = "#"
            
    l = tuple(l)
    
    output = "".join(l)
    return(output)

# return masked string IF STRING AS INPUT
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
