def Find_Email_Address(target):
    import re
    target = target.replace(" ","")
    return re.findall(r'[\w.-]+@[\w.-]+',target)
