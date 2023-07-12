l = ['7m3j4ik2a','5M0L8P1','asdf','M21d1r32']

import re

def string_expansion(s):
    pattern = r'\d'  # Regular expression pattern to match any digit
    if not bool(re.search(pattern, s)):
        return s
    
    # Find first non-digit characters
    begin = ''
    for char in s:
        if char.isdigit():
            break
        begin += char

    numbers = [str(x) for x in range(0,10)]
    out = []
    result = []

    for i in range(len(s)):
        obj = [s[i]]
        j = 1

        if s[i] not in numbers:
            continue

        while  i + j < len(s) and s[i + j] not in numbers:
            obj.append(s[i + j])
            j += 1

        out.append(''.join(obj))

    for i in out:
        num = int(i[0])
        char = i[1:]

        for i in range(len(char)):
            result.append(num * char[i])
            
    return begin + ''.join(result)

for i in range(len(l)):
  print(string_expansion(l[i]))
