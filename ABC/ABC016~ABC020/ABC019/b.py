s = input()
result = ''
start_index = 0

for i in range(len(s)):
    try:
        if s[i] == s[i+1]:
            pass
        else:
            result += (s[start_index] + (str(i-start_index+1)))
            start_index = i + 1
    except:
        result += (s[start_index] + (str(i-start_index+1)))
        break
    
print(result)
