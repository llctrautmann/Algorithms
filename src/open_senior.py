def open_or_senior(data):
    
    output = []
    
    for i in range(len(data)):
            if data[i][0] >= 55 and data[i][1] > 7:
                output.append("Senior")
            else:
                output.append("Open")
    
    
    return output
