def narcissistic(value):
    num = str(value)
    a = len(num)
    result = [int(a) for a in str(num)]

    val = []
    for i in range(len(result)): 
        val.append(int(result[i])**int(a))

    if sum(val) == value:
        return "T"
    else:
        return "F"
